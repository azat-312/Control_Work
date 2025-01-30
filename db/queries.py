CREATE_TABLE_products = """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    product_id TEXT
    )
"""



INSERT_products_query = """
    INSERT INTO products(name_product, category, size, price, photo, product_id)
    VALUES (?, ?, ?, ?, ?, ?)
"""
