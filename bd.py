from mysql.connector import connect, Error

try:
    with connect(
        host="****",
        user='***',
        password='***',
        database="*****",
    ) as connection:
        select_glpi_tickets_query = "SELECT name, date, content, users_id_recipient FROM glpi_tickets LIMIT 4"
        with connection.cursor() as cursor:
            cursor.execute(select_glpi_tickets_query)
            result = cursor.fetchall()
            print("Name     Date     Content    User_id")
            for row in result:
                print("%s    %s     %s    %s" % (row[0], row[1], row[2], row[3]))
except Error as e:
    print(e)

#
# user_id_recipient_raw = [row[3] for row in result]    #user_id_recipient raw all
# name_raw = [row[0] for row in result]     #name
# date_raw = [row[1] for row in result]     #date
# content_raw = [row[2] for row in result]    #content
# user_id = str(user_id_recipient_raw[0])
# name = str(name_raw[0])
# date = str(date_raw[0])
# content = str(content_raw[0])
#
# def output_tickets_in_bot():
#     return "Поступила новая заявка.\nПользователь: " + user_id + "\n" + "Ее название " + name + "\nВремя: " + date + "\nОписание " + content
#
#
# print(output_tickets_in_bot())
