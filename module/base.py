import sqlite3
from pathlib import Path


def init():
    DB_NAME = 'db.sqlite3'
    MAIN_PATH = Path(__file__).parent.parent
    global db, cur
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cur = db.cursor()


def create_table():
    """
        Функция для создания таблицы sqlite3
    """
    cur.execute(
        """CREATE TABLE IF NOT EXISTS cars(
            title TEXT,
            price TEXT,
            link FLOAT)
        """
    )
    db.commit()


def done_cars():
    """
        Функция для заполнения таблицы
    """
    cur.execute("""INSERT INTO cars(
        title,
        price,
        link)
        VALUES
        """)
    db.commit()


def get_data():
    cur.execute(
        """
        SELECT * FROM  cars
        """
    )
    return cur.fetchall()