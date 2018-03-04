@echo off

set SPATH=%~dp0
set XAML=%SPATH%\main.xaml

set UIROBOT=C:\Users\linhu\AppData\Local\UiPath\app-17.1.6522\uirobot.exe

%UIROBOT% /file %XAML%