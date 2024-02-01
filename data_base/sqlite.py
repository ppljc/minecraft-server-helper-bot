# <---------- Python modules ---------->
import sqlite3


# <---------- Python modules ---------->
from utilities import logger


# <---------- Variables ----------->
filename = 'sqlite.py'
db_file = 'server.db'


# <---------- Starts connection ---------->
def sql_start() -> bool:
    try:
        global base, cur
        base = sqlite3.connect(database=db_file)
        cur = base.cursor()
        base.execute(
            'CREATE TABLE IF NOT EXISTS players'
            '(username TEXT, full_name TEXT, id INTEGER, nickname TEXT, date DATE, approval TEXT, admin BOOL)'
        )
        base.commit()
        return True
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='sql_start',
            exception=exc,
            content=''
        )
        return False


# <---------- Database operations ---------->
def insertCategory(category: str, percent_encoding: str) -> bool:
    try:
        cur.execute(
            'INSERT INTO categories (category, percent_encoding) VALUES (?, ?)',
            (category, percent_encoding)
        )
        base.commit()
        return True
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='insertCategory',
            exception=exc,
            content=''
        )
        return False


def insertKeyword(keyword: str) -> bool:
    try:
        cur.execute(
            'INSERT INTO keywords (keyword) VALUES (?)',
            (keyword,)
        )
        base.commit()
        return True
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='insertKeyword',
            exception=exc,
            content=''
        )
        return False


def insertProductCard(name: str, price: int, id: int, photo: str, category: str, keyword: str) -> bool:
    try:
        cur.execute(
            'INSERT INTO product_cards (name, price, id, photo, category, keyword, used) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (name, price, id, photo, category, keyword, False)
        )
        base.commit()
        return True
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='insertProductCard',
            exception=exc,
            content=''
        )
        return False


def insertContract(name: str, customer: str, customer_id: int, doer: str, doer_id: int, date: str, document: str, price: int) -> bool:
    try:
        cur.execute(
            'INSERT INTO contracts (name, customer, customer_id, doer, doer_id, date, document, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (name, customer, customer_id, doer, doer_id, date, document, price)
        )
        base.commit()
        return True
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='insertContract',
            exception=exc,
            content=''
        )
        return False


def select_where1(table: str, what: str, where: str, where_value: str):
    try:
        return cur.execute(
            f'SELECT {what} FROM {table} WHERE {where} = ?',
            (where_value,)
        ).fetchall()
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='select_where1',
            exception=exc,
            content=''
        )
        return False


def select_where2(table: str, what: str, where: str, where_value: str):
    try:
        return cur.execute(
            f'SELECT {what} FROM {table} WHERE {where} = ?',
            (where_value,)
        ).fetchall()
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='select_where1',
            exception=exc,
            content=''
        )
        return False


def select_where3(table: str, what: str, where_1: str, where_1_value: str, where_2: str, where_2_value: str, where_3: str, where_3_value: str):
    try:
        return cur.execute(
            f'SELECT {what} FROM {table} WHERE {where_1} = ? AND WHERE {where_2} = ? AND WHERE {where_3} = ?',
            (where_1_value, where_2_value, where_3_value)
        ).fetchall()
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='select_where3',
            exception=exc,
            content=''
        )
        return False


def select_all(table: str, what: str):
    try:
        return cur.execute(f'SELECT {what} FROM {table}').fetchall()
    except Exception as exc:
        logger.create_log(
            filename=filename,
            function='select_all',
            exception=exc,
            content=''
        )
        return False
