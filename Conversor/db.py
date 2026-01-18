import sqlite3

# Connect to the database
conn = sqlite3.connect('/var/www/conversor.htb/instance/users.db')
cursor = conn.cursor()

# Execute queries
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

print(results)

# Don't forget to close the connection when done
conn.close()