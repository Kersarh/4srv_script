chcp 1251
@echo off
setlocal

set file1="C:\Backup\MyFIle_%date%.txt"
set kat1="D:\Backup\"

set errlog="errLog_Check.bat.log"
set viewlog="C:\Users\�������������\Desktop\errLog.log"

if not exist %file1% echo ����: %date% �����: %time% ������: � ����� %kat1% ����� �� ������� >> %errlog%

echo. >> %errlog% 
copy %errlog% %viewlog% /a