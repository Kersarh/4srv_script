@echo off
setlocal
chcp 1251

:start
echo.
set /p option1="[Warning]: [y/n]: "
if /i not defined option1 (cls& goto start)
if /i "%option1%"=="y" (echo yes& goto YES)
if /i "%option1%"=="n" (echo no& goto NO)
Echo �� ��������� ������ ����� �������& pause& cls& goto start
:YES
echo �� ������� ��!
pause
goto Next

:NO
echo �� ������� ���!
pause
goto Next


:Next
echo ����������� ���������
pause
