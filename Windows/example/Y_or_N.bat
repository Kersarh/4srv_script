@echo off
setlocal
chcp 1251

:start
echo.
set /p option1="[Warning]: [y/n]: "
if /i not defined option1 (cls& goto start)
if /i "%option1%"=="y" (echo yes& goto YES)
if /i "%option1%"=="n" (echo no& goto NO)
Echo Не правильно сделан выбор задания& pause& cls& goto start
:YES
echo Вы выбрали да!
pause
goto Next

:NO
echo Вы выбрали нет!
pause
goto Next


:Next
echo Продолжение программы
pause
