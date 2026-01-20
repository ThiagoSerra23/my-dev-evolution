@echo off
chcp 65001 > nul
echo --- Dev Daily Evolution: Execucao Manual ---
echo.

:: Executa o script Python
python scripts/auto_evolution.py

echo.
echo --- Preparando para enviar ao GitHub ---
echo.

:: Pega a mensagem do ultimo commit usando o script Python (mais seguro)
for /f "delims=" %%i in ('python scripts/get_commit_message.py') do set COMMIT_MSG=%%i

echo Mensagem do commit: %COMMIT_MSG%
echo.

:: Git commands
git pull
git add .
git commit -m "%COMMIT_MSG%"
git push

echo.
echo --- Concluido com sucesso! ---
pause
