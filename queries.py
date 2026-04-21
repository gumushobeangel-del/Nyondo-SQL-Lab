import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

print("A:", conn.execute("SELECT * FROM products").fetchall())

print("B:", conn.execute("SELECT name, price FROM products").fetchall())

print("C:", conn.execute("SELECT * FROM products WHERE id = 3").fetchall())

print("D:", conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall())

print("E:", conn.execute("SELECT * FROM products ORDER BY price DESC").fetchall())

print("F:", conn.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall())

conn.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit()

print("G:", conn.execute("SELECT * FROM products").fetchall())