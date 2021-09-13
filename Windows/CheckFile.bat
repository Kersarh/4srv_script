chcp 1251
@echo off
setlocal

set file1="C:\Backup\MyFIle_%date%.txt"
set kat1="D:\Backup\"

set errlog="errLog_Check.bat.log"
set viewlog="C:\Users\Администратор\Desktop\errLog.log"

if not exist %file1% echo Дата: %date% Время: %time% Ошибка: в папке %kat1% файлы не найдены >> %errlog%

echo. >> %errlog% 
copy %errlog% %viewlog% /a