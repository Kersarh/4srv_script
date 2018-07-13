"""
UFW
"""

import os


def main():
    """ Main func """
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("========================================")
        print("                 UFW")
        print("========================================")
        print("1. Install")
        print("2. Allow port")
        print("3. Deny port")
        print("4. Remove rule")
        print("5. Status")
        print("7. Reset")
        print("8. Logs")
        print("9. Start/Stop")
        print("0. Exit")
        print(">>> Warning! Check ports for SSH !!! <<<")

        i = input("Select: ")
        if i == "1":
            inst_ufw()
        elif i == "2":
            ufw_allow()
        elif i == "3":
            ufw_deny()
        elif i == "4":
            ufw_del_rules()
        elif i == "5":
            ufw_status()
        elif i == "6":
            ufw_reset()
        elif i == "7":
            ufw_reset()
        elif i == "8":
            ufw_log()
        elif i == "9":
            ufw_restart()
        elif i == "0":
            return 0
    return 1


def inst_ufw():
    """ Установка и открытие базовых портов """
    os.system("apt-get install ufw")
    ports = [22, 80, 443]
    ufw_def_allow(ports)
    print("Ports {} opened!".format(ports))
    print(">>> Warning! Check ports for SSH !!! <<<")


def ufw_def_allow(port):
    """ Дефолтное назначение портов"""
    for i in port:
        os.system("ufw allow %s" % i)
        print("Открыт порт %s" % i)


def ufw_allow():
    """ Открыть порт """
    i = input("Allow port (N = exit):")
    if i in ["n", "N"]:
        pass
    else:
        os.system("ufw allow %s" % i)


def ufw_deny():
    """ Закрыть порт """
    i = input("Deny port (N = exit):")
    if i in ["n", "N"]:
        pass
    else:
        os.system("ufw deny %s" % i)


def ufw_restart():
    """ Перезапуск """
    print("1. enable")
    print("2. disable")
    print("3. reload")
    print("0. Exit")
    i = input("Select: ")
    if i == "1":
        os.system("ufw enable")
    elif i == "2":
        os.system("ufw disable")
    elif i == "3":
        os.system("ufw reload")
    elif i == "0":
        return
    return


def ufw_status():
    """ Отобразить правило нумерованным списком """
    os.system("ufw status numbered")


def ufw_del_rules():
    """ Удалить правило по номеру """
    ufw_status()
    i = input("Delete rule number (N = exit):")
    if i in ["n", "N"]:
        pass
    else:
        os.system("ufw delete %s" % i)


def ufw_reset():
    """ Сброс правил """
    os.system("ufw reset")


def ufw_log():
    """ Отобразить логи """
    os.system("tail -f /var/log/ufw.log")


# Также можно разрешить доступ к порту с определенных компьютеров или сетей.
# sudo ufw allow proto tcp from 192.168.0.1 to any port 22
# в начало списка для высшего приоритета
# ufw insert 1 deny from 123.45.67.89

if __name__ == "__main__":
    main()
