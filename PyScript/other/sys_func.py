"""
Набор системных команд
"""
import os


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("========================================")
        print("                 System")
        print("========================================")
        print("1. Updates / Clear")
        print("2. Users")
        print("3. Logs")
        print("0. Exit")

        i = input("Select: ")

        if i == "1":
            update()
        elif i == "2":
            UserCtl()
        elif i == "0":
            break


def update():
    print("========================================")
    print("           Updates / Clear")
    print("========================================")

    print("1. Update and Upgrade")
    print("2. Clear")

    i = input("Select: ")

    if i == "1":
        os.system("apt-get update")
        os.system("apt-get upgrade")
    elif i == "2":
        os.system("apt autoremove")
    elif i == "0":
        pass


class UserCtl(object):
    def __init__(self):
        print("__init__")
        self.user_start()

    def user_start(self):
        while True:
            print("========================================")
            print("             User Control")
            print("========================================")
            print("1. Info")
            print("2. Management")
            print("0. Exit")

            i = input("Select: ")
            if i == "1":
                self.user_info()
            elif i == "2":
                self.user_mng()
            elif i == "0":
                break

    def user_info(self):
        """ Users info """
        while True:
            print("========================================")
            print("             Users info")
            print("========================================")
            print("1. Users list")
            print("2. -> Only Names")
            print("3. Active Users")
            print("4. Login History")
            print("5. -> Last Login")
            print("0. Exit")

            i = input("Select: ")

            if i == "1":
                os.system("cat /etc/passwd")
            elif i == "2":
                os.system("sed 's/:.*//' /etc/passwd")
            elif i == "3":
                os.system("w")
            elif i == "4":
                os.system("last -a")
            elif i == "5":
                os.system("lastlog")
            elif i == "0":
                break

    def user_mng(self):
        while True:
            print("========================================")
            print("             User Management")
            print("========================================")
            print("1. Add user")
            print("2. Remove user")
            print("3. Add to group")
            print("4. Remove from group")
            print("5. Ban user")
            print("6. On/Off Root")
            print("0. Exit")

            i = input("Select: ")

            if i == "1":
                self.user_add()
            elif i == "2":
                self.user_del()
            elif i == "3":
                self.user_add_group()
            elif i == "4":
                self.user_rem_group()
            elif i == "5":
                self.user_ban()
            elif i == "6":
                pass
            elif i == "0":
                return
        return

    def user_add(self):
        print("Сreate new user")
        usr = input("User name: ")
        if not usr:
            pass
        else:
            os.system("useradd {}".format(usr))

    def user_del(self):
        print("Delete user")
        usr = input("User name: ")
        os.system("userdel - f - r {}".format(usr))

    def user_add_group(self):
        print("Add user to group")
        usr = input("User name: ")
        group = input("Group name: ")
        os.system("usermod -a -G {group} {usr}".format(group=group, usr=usr))

    def user_rem_group(self):
        print("Remove user from group")
        usr = input("User name: ")
        group = input("Group name: ")
        os.system("gpasswd - d {user} {group}".format(user=usr, group=group))

    def user_ban(self):
        print("Block user")
        usr = input("User name: ")
        os.system("passwd --lock %s" % usr)

    def root_en(self):
        print("On/Off root")
        i = input("On(1) or Off(2) or Exit(0):")
        if i == "1":
            os.system("passwd root")
        elif i == "2":
            os.system("passwd -l root")
        else:
            pass


def logs():
    print("========================================")
    print("             Logs")
    print("========================================")
    print("1. Last launch")
    print("2. Last record")
    print("3. Last collapse")
    print("4. journalctl -xe")
    print("5. Fail authorization")
    print("0. Exit")

    i = input("Select: ")
    if i == "1":
        os.system("journalctl - b")
    elif i == "2":
        os.system("journalctl - f")
    elif i == "3":
        os.system("journalctl - b - 1")
    elif i == "4":
        os.system("journalctl -xe")
    elif i == "5":
        os.system('grep "Failed password" /var/log/auth.log')
    elif i == "0":
        pass


if __name__ == "__main__":
    main()
