import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="172.16.2.10", user="bot", passwd="password", database="glpi")

# creating the cursor object
bot = myconn.cursor()

try:
    bot.execute("""
        SELECT name, date, content, users_id_recipient
        FROM glpi_tickets
        """)
    result = bot.fetchall()
    print("Name    id    Salary")
    for row in result:
        print("%s    %d    %d" % (row[0], row[1], row[2]))
except:
    myconn.rollback()

myconn.close()
