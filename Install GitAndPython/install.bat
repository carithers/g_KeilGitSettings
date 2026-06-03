@echo off
chcp 65001 >nul
title 环境配置脚本启动器

:: 获取当前批处理文件所在的完整路径
:: set "SCRIPT_PATH=%~dp0GitAndPy.ps1"
set "SCRIPT_PATH=%~dp0GitAndPy"

:: 检查 ps1 文件是否存在
if not exist "%SCRIPT_PATH%" (
    echo [错误] 找不到 GitAndPy！
    echo 请确保本 bat 文件和 GitAndPy 放在同一个文件夹下。
    echo.
    pause
    exit /b
)

echo 正在请求管理员权限以运行环境配置脚本...
echo 如果弹出“用户账户控制”窗口，请点击“是”。

:: 启动下载安装脚本GitAndPy.ps1
:: powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File \"%SCRIPT_PATH%\"' -Verb RunAs"

:: 启动下载安装脚本GitAndPy, 绕过后缀检测，读取纯文本并在内存中执行
powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command \"Invoke-Expression (Get-Content -Raw -LiteralPath ''%SCRIPT_PATH%'')\"' -Verb RunAs"

exit