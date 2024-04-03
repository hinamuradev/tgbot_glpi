from mysql.connector import connect, Error

try:
    with connect(
        host="172.16.2.10",
        user='bot',
        password='password',
        database="glpi",
    ) as connection:
        select_glpi_tickets_query = "SELECT name, date, content, users_id_recipient FROM glpi_tickets LIMIT 4"
        select_glpi_users_id_query = "SELECT"
        with connection.cursor() as cursor:
            cursor.execute(select_glpi_tickets_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)


user_id_recipient_raw = [row[3] for row in result]    #user_id_recipient raw all
name_raw = [row[0] for row in result]     #name
date_raw = [row[1] for row in result]     #date
content_raw = [row[2] for row in result]    #content
user_id = str(user_id_recipient_raw[0])
name = str(name_raw[0])
date = str(date_raw[0])
content = str(content_raw[0])


def output_tickets_in_bot():
    return "Поступила новая заявка.\nПользователь: " + user_id + "\n" + "Ее название " + name + "\nВремя: " + date + "\nОписание " + content


print(output_tickets_in_bot())
