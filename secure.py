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


# connect to the database

# SAFE SEARCH FUNCTION

# check input is valid (must be text, at least 2 characters, no < > ;)
# stop if input is bad

# use ? to make query safe (prevents SQL injection)
# add % for searching part of the name
# run query and get results


# SAFE LOGIN FUNCTION

# check username is not empty and has no spaces
# stop if username is bad

# check password is at least 6 characters
# stop if password is bad

# use ? to make login query safe
# run query safely and get one result


# TEST CASES

# attack tests (these should fail)

# normal valid inputs (these should work)

# bad inputs (these should be rejected)
