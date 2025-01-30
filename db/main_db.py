import sqlite3
from db import queries


db = sqlite3.connect('db/products.sqlite3')
cursor = db.cursor()


async def create_db():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_products)


async def sql_insert_products(name_product, category, size, price, photo, product_id):
    cursor.execute(queries.INSERT_products_query, (
        name_product, category, size, price, photo, product_id
    ))
    db.commit()
# CRUD - 1
# ==================================================================


def get_db_connection():
    conn = sqlite3.connect('db/product.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM products p 
    INNER JOIN product t ON p.product_id = t.product_id
    """).fetchall()
    conn.close()
    return products