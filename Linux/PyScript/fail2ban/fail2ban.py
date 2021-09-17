"""
Fail2Ban Install Script
"""
import os
import shutil


def main():
    """ Main menu """
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("========================================")
        print("             Fail2ban")
        print("========================================")
        print("  1 - Install")
        print("  2 - Status")
        print("  3 - Restart")
        print("  4 - Logs")
        print("  5 - Config")
        print("  9 - Uninstall")
        print("  0 - Exit")

        i = input("\n  Select:")
        if i == "1":
            inst_f2b()
        elif i == "2":
            status()
        elif i == "3":
            os.system("service fail2ban restart")
        elif i == "4":
            os.system("tail -f /var/log/fail2ban.log")
        elif i == "5":
            os.system("nano /etc/fail2ban/jail.d/defaults-debian.conf")
        elif i == "6":
            del_f2b()
        elif i == "0":
            return
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def inst_f2b():
    """ Install """
    os.system("apt-get update")
    os.system("apt-get install fail2ban")

    shutil.copyfile("defaults-debian.conf",
                    "/etc/fail2ban/jail.d/defaults-debian.conf")

    os.system("service fail2ban restart")
    os.system("fail2ban-client status")


def status(prot="sshd"):
    """ Status """
    os.system("fail2ban-client status {}".format(prot))


def del_f2b():
    """ Uninstall """
    os.system("apt-get remove fail2ban")
    i = input("clear iptables?(y/n):")
    if i in ["y", "Y"]:
        os.system("iptables -F")


if __name__ == "__main__":
    main()
