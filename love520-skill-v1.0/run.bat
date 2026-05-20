
@echo off
chcp 65001 &gt;nul
echo 💖 正在启动520浪漫表白技能...
echo.

cd /d "%~dp0"
python simple_run.py

if errorlevel 1 (
    echo.
    echo ❌ 启动失败！请确保已安装Python和PyQt5:
    echo    pip install PyQt5
    echo.
    pause
)
