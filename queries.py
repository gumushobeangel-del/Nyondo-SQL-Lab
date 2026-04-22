import sqlite3

# I connect to my database
conn = sqlite3.connect('nyondo_stock.db')


# A: I fetch all products from the table
print("A:", conn.execute("SELECT * FROM products").fetchall())


# B: I fetch only specific columns (name and price) instead of everything
print("B:", conn.execute("SELECT name, price FROM products").fetchall())


# C: I get a specific product using its ID (id = 3)
print("C:", conn.execute("SELECT * FROM products WHERE id = 3").fetchall())


# D: I search for products whose names contain the word "sheet"
# The % symbol allows partial matching
print("D:", conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall())


# E: I sort all products by price from highest to lowest
print("E:", conn.execute("SELECT * FROM products ORDER BY price DESC").fetchall())


# F: I sort by price (highest first) but only return the top 2 products
print("F:", conn.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall())


# I update the price of the product with id = 1
conn.execute("UPDATE products SET price = 38000 WHERE id = 1")

# I save (commit) the changes to the database
conn.commit()


# G: I fetch all products again to confirm the update was successful
print("G:", conn.execute("SELECT * FROM products").fetchall())