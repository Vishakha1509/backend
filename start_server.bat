@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Starting Django server...
python manage.py runserver
pause







