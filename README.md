# FlaskSQLAlchemy

1. Buat venv (python3 -m venv venv)
2. Masuk venv (source venv bin activate)
3. Buat file .env (Konfigurasikan FLASK_APP(file py yang menjadi main), Konfigurasikan DB(DB_HOST,DB_DATABASE,DB_USERNAME,DB_PASSWORD))
4. Buat file config.py (class config yang isinya SQLALCHEMY_DATABASE_URI)
4. Buat folder app
5. Buat folder controllers dan models didalam folder app
6. Buat file user.py pada models(import db)
7. Buat file __init__.py pada folder app(buat koneksi dengan flask,sqlalchemy,app.config.from_object(Config),migrate,import model,import routes)
8. Pada terminal(flask db init, flask db migrate -m "", flask db upgrade)