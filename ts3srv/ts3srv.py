""" ts server """

import os
import subprocess
import tarfile
import time
import urllib.request


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================")
    print("            TS3 Server")
    print("========================================")
    print("1 - Install")
    print("2 - Remove")
    print("0 - Exit")

    ts = TS3Server()

    i = input("\n  Select: ")
    if i == "1":
        ts.installer()
    elif i == "2":
        ts.rem_ts()
    elif i == "0":
        pass


class TS3Server():
    def __init__(self):
        # Имя пользователя по умолчанию
        self.uname = "ts3server"
        # Откуда качаем сервер
        self.dwl = "http://dl.4players.de/ts/releases/3.1.3/teamspeak3-server_linux_amd64-3.1.3.tar.bz2"

    def updater(self):
        os.system("apt-get update")
        os.system("apt-get -y install python3-pip")
        os.system("pip3 install python-crontab")

    def add_user(self):
        self.uname = input("User name for TS3 server (ts3server):")
        if len(self.uname) <= 0:
            self.uname = "ts3server"

        print("Please wait...")
        f = os.system("sudo useradd -m -p password -s /sbin/nologin {}".format(
            self.uname))
        # 0 если все получилось иначе не равно нулю.
        if f != 0:
            a = input("Error! Failed to create a new user! Continue?(Y/N):")
            if a in ["y", "Y"]:
                pass
            else:
                exit()

    def download_ts(self, dwl):
        fname = os.path.basename(dwl)
        os.chdir("/home/{}".format(self.uname))
        # Качаем файл
        urllib.request.urlretrieve(dwl, fname)
        # Извлекаем
        tar = tarfile.open(fname, "r")
        tar.extractall()
        tar.close()
        # Удаляем скачанный файл
        os.system("rm %s" % fname)
        # Переименовываем извлеченную папку
        os.rename("teamspeak3-server_linux_amd64", "ts3server")

        # Задаем права
        os.chdir("/home/{}/ts3server".format(self.uname))
        os.system("chmod +x ts3server_minimal_runscript.sh")
        os.system("chmod +x ts3server_startscript.sh")
        os.system("chmod +x ts3server")
        os.system("touch .ts3server_license_accepted")

    def autorun(self):
        user = self.uname
        # Назначаем пользователя владельцем файлов
        os.chdir("/home")
        os.system("chown -R {user}:{user} {user}".format(user=user))
        os.chdir("{}".format(user))
        os.system("ls -la")

        # Добавляем в автозагрузку
        from crontab import CronTab
        my_cron = CronTab(user="{}".format(user))
        job = my_cron.new(
            command=
            "/home/{}/ts3server/ts3server_startscript.sh start license_accepted=1".
            format(user))
        job.every_reboot()
        my_cron.write()
        print(">>> crontab added! <<<")

    def installer(self):
        self.updater()

        print("\n\n	>>> Install TS3Server")
        print("Warning!!!")
        print("New user is created during installation!")
        print("Server access logs in the folder:")
        print("""/home/__TS_USER_NAME__/ts3setver_logs.txt\n\n""")

        # Добавляем нового пользователя для TS
        self.add_user()

        # Скачиваем файл
        self.download_ts(self.dwl)

        # Скрипт запуска и лог файл
        runscript = "/home/{user}/ts3server/ts3server_startscript.sh".format(
            user=self.uname)
        logfile = "/home/{user}/ts3server_logs.txt".format(user=self.uname)
        # Запускаем установку
        subprocess.Popen(
            [runscript, "start", "license_accepted=1"],
            stdout=open(logfile, "w+"),
            stderr=open(logfile, "w+"),
            shell=False)
        time.sleep(3)

        # Добавляем записи в автозагрузку
        self.autorun()

        # Перезапуск сервера
        os.system("{} restart".format(runscript))

        # Вывод логов
        lfile = open(logfile, "r")
        print(lfile.read())
        lfile.close()

    def rem_ts(self):
        self.uname = input("Enter the username for which TS was installed: ")
        if len(self.uname) <= 0:
            self.uname = "ts3server"

        # Останавливаем сервер
        os.system("sh /home/{}/ts3server/ts3server_startscript.sh stop".format(
            self.uname))
        # Освобождаем порт
        os.system("fuser -k 30033/tcp")
        # Удаляем каталог TS и пользователя
        os.chdir("/home/%s" % self.uname)
        os.system("rm -R ts3server")
        os.system("userdel -f -r %s" % self.uname)


if __name__ == "__main__":
    main()
