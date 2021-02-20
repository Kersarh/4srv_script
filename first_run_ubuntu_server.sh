#!/bin/bash

# Обновление ОС
apt-get update
apt-get upgrade -y
apt-get dist-upgrade -y
apt-get install -y python3
apt-get install -y net-tools

# Дополнительные архиваторы
apt-get install -y p7zip-rar p7zip-full rar unrar unace arj cabextract file-roller zip unzip
# Для разработки
apt-get install -y tree redis-server libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-pip python3-pip python3-dev python-imaging python3-lxml libxslt-dev python-libxml2 python-libxslt1 libffi-dev libssl-dev python-dev gnumeric libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libfreetype6-dev libcurl4-openssl-dev
#
apt-get install -y nano mosh tmux htop git curl wget gcc build-essential make

#
apt-get install -y supervisor nginx

# Локали
export LANGUAGE=ru_RU.UTF-8
export LANG=ru_RU.UTF-8
export LC_ALL=ru_RU.UTF-8
sudo locale-gen ru_RU.UTF-8

#
sudo dpkg --configure -a

# Небольшая чистка
apt-get autoremove -y
apt-get autoclean -y
apt-get clean -y
apt-get install -f -y

# # fish вместо Bash
# apt install fish
# set fish_greeting ""
# chsh -s /usr/bin/fish
# # fish_config

# ZSH вместо Bash
apt install zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
chsh -s /usr/bin/zsh


# Beep о завершении
echo $'\a'