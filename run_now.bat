@echo off
echo --- Dev Daily Evolution: Execucao Manual ---
echo.

:: Executa o script Python
python scripts/auto_evolution.py

echo.
echo --- Preparando para enviar ao GitHub ---
echo.

:: Pega a mensagem do ultimo commit gerado
set /p COMMIT_MSG=<scripts/last_commit_msg.txt

:: Git commands
git add .
git commit -m "%COMMIT_MSG%"
git push

echo.
echo --- Concluido com sucesso! ---
pause
