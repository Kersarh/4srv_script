#!/usr/bin/python3
""" Start scrypt for repo """
import os

import fail2ban.fail2ban as f2b
import squid.install_squid as squid
import ts3srv.ts3srv as ts_inst
import ufw.ufw as ufw
import other.sys_func as sys_func


def main():
    """ Main func """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print("           Main Menu")
        print("========================================")
        print("  1 - System info")
        print("  2 - Install")
        print("  0 - Exit")

        i = input("\n  Select: ")

        if i == "1":
            sys_func.main()

        elif i == "2":
            inst()

        elif i == "0":
            print("Удачи!")
            return 0
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def inst():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print("           Install")
        print("========================================")
        print("--- Proxy/VPN ---")
        print("1. Squid proxy")
        print("2. OpenVpn (GitHub:Nyr)")
        print("3. IPsek VPN (GitHub:hwdsl2)")
        print("--- Security ---")
        print("4. Fail2ban")
        print("5. UFW")
        print("--- Other ---")
        print("6. TS3 server")
        print("0. Exit")

        i = input("\n  Select: ")

        if i == "1":
            squid.main()

        elif i == "2":
            os.system(
                "wget https://git.io/vpn -O openvpn-install.sh && bash openvpn-install.sh"
            )

        elif i == "3":
            os.system(
                "wget https://git.io/vpnsetup -O vpnsetup.sh && sudo sh vpnsetup.sh"
            )

        elif i == "4":
            f2b.main()

        elif i == "5":
            ufw.main()

        elif i == "6":
            ts_inst.main()

        elif i == "0":
            print("Удачи!")
            return
    return


if __name__ == "__main__":
    main()
