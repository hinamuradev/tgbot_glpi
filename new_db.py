import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host=ID_HOST, user=ID_NAME, passwd=ID_PASS, database=DB)

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
