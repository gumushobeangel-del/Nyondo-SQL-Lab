import sqlite3

# I connect to my database
conn = sqlite3.connect('nyondo_stock.db')


# This function is used to search for products safely
def search_product_safe(name):
    
    # I first check if the input is valid
    # It must be a string, at least 2 characters, and should not contain dangerous characters
    if not isinstance(name, str) or len(name) < 2 or any(c in name for c in "<>;"):
        print("Invalid input")
        return None
    
    # I use a parameterized query to avoid SQL injection
    # The % signs help me search for names that contain the input (not exact match only)
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, ('%' + name + '%',)).fetchall()
    
    # I return all matching products
    return rows


# This function handles login securely
def login_safe(username, password):

    # I check if the username is valid
    # It should be a string, not empty, and should not contain spaces
    if not isinstance(username, str) or not username or " " in username:
        print("Invalid username")
        return None

    # I check if the password is valid
    # It must be a string and at least 6 characters long
    if not isinstance(password, str) or len(password) < 6:
        print("Invalid password")
        return None

    # I use a parameterized query to safely check the user in the database
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    
    # I return the user if found
    return row


# TESTING MY FUNCTIONS

# I test SQL injection attempts to make sure my system is safe
print("Test 1:", search_product_safe("' OR 1=1--"))
print("Test 2:", search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print("Test 3:", login_safe("admin'--", "anything"))
print("Test 4:", login_safe("' OR '1'='1", "' OR '1'='1"))

# I test normal valid inputs
print("Valid:", search_product_safe("cement"))

# I test invalid inputs to confirm they are rejected
print("Reject empty:", search_product_safe(""))
print("Reject script:", search_product_safe("<script>"))

# I test login cases
print("Valid login:", login_safe("admin", "admin123"))
print("Reject short password:", login_safe("admin", "ab"))
print("Reject space username:", login_safe("ad min", "pass123"))