import snowflake.connector

# Establish connection
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT_NAME',  
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA',
    role='YOUR_ROLE'
)

# Create cursor and run query
cur = conn.cursor()
cur.execute("SELECT CURRENT_VERSION();")
print(cur.fetchone())

# Close connection
cur.close()
conn.close()
