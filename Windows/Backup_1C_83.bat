chcp 1251
@echo off
setlocal

set kat=C:\Program Files (x86)\1cv8\8.3.17.1851

set base1=D:\FileDataBase

"%kat%\bin\1cv8.exe" CONFIG /F "%base1%" /DisableStartupMessages /DumpIB "D:\Backup\1c83_%date%.dt" /N ADMIN_LOGIN /P PASSWORD /OUT "D:\Backup\backup.log" -NoTruncate

echo %date% %time% >> mybackup.log
