#!/bin/bash

echo "Скрипт обновит систему и установит некторые дополнения."
echo -n "Продолжить? (y/n) "
read item
case "$item" in
    y|Y) echo "Ввели «y», продолжаем..."
        ;;
    n|N) echo "Ввели «n», завершаем..."
        exit 0
        ;;
    *) echo "Ничего не ввели."
		exit 0
        ;;
esac

# Обновление ОС
apt-get update
apt-get upgrade -y
apt-get dist-upgrade -y
apt-get install -y python3
apt-get install -y net-tools

# Дополнительные архиваторы
apt-get install -y p7zip-rar p7zip-full rar unrar arj cabextract file-roller zip unzip
apt-get install -y nano mosh tmux htop git curl wget gcc build-essential make

# Мультимедия кодеки
apt-get install -y ubuntu-restricted-extras

#
sudo dpkg --configure -a

#Небольшая чистка
apt-get autoremove -y
apt-get autoclean -y
apt-get clean -y
apt-get install -f -y

#fish вместо Bash
# apt install fish
# set fish_greeting ""
# chsh -s /usr/bin/fish
# fish_config

#Модули наутилус
apt-get install -y nautilus-admin exe-thumbnailer
cd ~/Templates/
touch new-text.txt
nautilus -q

# Настройки гнома
apt-get install -y gnome-tweak-tool

# Beep о завершении
echo $'\a'