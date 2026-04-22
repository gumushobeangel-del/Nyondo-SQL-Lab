import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product_safe(name):
    
    if not isinstance(name, str) or len(name) < 2 or any(c in name for c in "<>;"):
        print("Invalid input")
        return None
    

    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, ('%' + name + '%',)).fetchall()
    return rows


def login_safe(username, password):

    if not isinstance(username, str) or not username or " " in username:
        print("Invalid username")
        return None

    if not isinstance(password, str) or len(password) < 6:
        print("Invalid password")
        return None

    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    return row



print("Test 1:", search_product_safe("' OR 1=1--"))
print("Test 2:", search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print("Test 3:", login_safe("admin'--", "anything"))
print("Test 4:", login_safe("' OR '1'='1", "' OR '1'='1"))

print("Valid:", search_product_safe("cement"))
print("Reject empty:", search_product_safe(""))
print("Reject script:", search_product_safe("<script>"))
print("Valid login:", login_safe("admin", "admin123"))
print("Reject short password:", login_safe("admin", "ab"))
print("Reject space username:", login_safe("ad min", "pass123"))


# I connect to the database
# I establish a secure connection to the database 


# SAFE SEARCH FUNCTION

# I check if the input is valid:
# it must be a string
# it must be at least 2 characters long
# it must not contain dangerous characters like < > 

# I use parameterized queries (? or %s depending on the database) to prevent SQL injection

# I use LIKE with % so I can search for partial matches

# I run the query safely and get the results


# SAFE LOGIN FUNCTION

# I check that the username is valid:
# it must not be empty
# it must not contain spaces

# I check that the password is valid:
# it must be at least 6 characters long
# it should be hashed before storing or checking

# I use parameterized queries (? or %s) to make the login query safe

# I run the query safely and return one matching user


# TEST CASES

# I test SQL injection attempts to make sure they fail

# I test normal valid inputs to make sure they work

# I test invalid inputs to make sure they are rejected