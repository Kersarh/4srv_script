""" Squid installer """
import os
import re
import http.client
import ipaddress


def main():
    """ Menu """
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("========================================")
        print("             Squid proxy")
        print("========================================")
        print("1 - Install")
        print("2 - Add Users")
        print("3 - Config file")
        print("4 - Users edit")
        print("5 - Restart")
        print("6 - Clear cache")
        print("0 - Exit")

        i = input("Select: ")

        if i == "1":
            inst_prx()
        elif i == "2":
            new_user()
        elif i == "3":
            os.system("nano /etc/squid/squid.conf")
        elif i == "4":
            os.system("nano /etc/squid/passwd")
        elif i == "5":
            os.system("/etc/init.d/squid restart")
        elif i == "6":
            clear_cache()
        elif i == "0":
            return
    return


def inst_prx():
    """ install """
    # Устанавливаем необходимые модули
    os.system("apt-get update")
    os.system("apt-get -y install squid")
    os.system("apt-get -y squid-langpack")
    os.system("apt-get -y install apache2-utils")

    # Получаем внешний IP
    conn = http.client.HTTPConnection("eth0.me")
    conn.request("GET", "")
    my_ip = conn.getresponse().read().decode('utf-8').rstrip('\n')
    # Проверяем IP на кореектность
    ip_y = input(">>> Your IP? %s (y/n):" % my_ip)
    if len(ip_y) <= 0:
        ip_y = "Y"
    if ip_y not in ["y", "Y"]:
        while True:
            try:
                my_ip = input("Enter your IP:")
                ipaddress.ip_address(my_ip)
                break
            except Exception as exp:
                print(exp)

    # Копируем файл конфигурации
    output_file = open("/etc/squid/squid.conf", "w")
    temp_conf = open("./squid.conf").read()
    output_file.write(re.sub("##SRV_IP##", my_ip, temp_conf))
    output_file.close()
    os.system("squid -k shutdown")

    # создаем файл с паролями
    os.system("touch /etc/squid/passwd")
    new_user()


def new_user():
    """ add new user """
    # Создаем пользователя
    usr = input("New username:")
    os.system("htpasswd /etc/squid/passwd %s" % usr)
    # и перезапускаем систему
    os.system("/etc/init.d/squid restart")


def clear_cache():
    """ Clear cache """
    os.system("squid -k shutdown")
    os.system("squid -z reconfigure")
    os.system("squid -z")
    os.system("/etc/init.d/squid restart")


if __name__ == "__main__":
    main()
