@echo off
rem usage: push_to_github.bat https://github.com/<user>/<repo>.git
if "%~1"=="" (echo usage: push_to_github.bat ^<repo-url^> & exit /b 1)
cd /d "%~dp0"
git init -b main
git add -A
git commit -m "wave 3 start: prompts, checks, cards, refs"
git remote add origin %1
git push -u origin main
pause
