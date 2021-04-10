call .venv\Scripts\activate.bat

set FLASK_APP=routes.py
set FLASK_ENV=development

flask run