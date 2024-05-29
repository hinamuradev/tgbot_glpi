import html
import time
import requests
from mysql.connector import connect, Error

# Параметры подключения к базе данных
DATABASE_CONFIG = {
    'host': '',
    'user': '',
    'password': '',
    'database': '',
}

# Токен вашего Telegram бота
TOKEN = ''

# Идентификатор вашего чата с ботом
CHAT_ID = ''
last_query = None


def connect_to_database():
    try:
        connection = connect(**DATABASE_CONFIG)
        return connection
    except Error as e:
        print("Ошибка подключения к базе данных:", e)
        return None


def execute_query(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Error as e:
        print("Ошибка выполнения запроса:", e)
        return None


def send_telegram_message_to_group(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': '-1001259896915', 
        'text': html.unescape(message)  # Удаление HTML-тегов из сообщения
    }
    response = requests.post(url, json=params)
    if response.status_code != 200:
        print("Ошибка отправки сообщения:", response.text)


def check_for_new_queries():
    global last_query

    select_last_glpi_query = "SELECT name, date, content, users_id_recipient FROM glpi_tickets ORDER BY date DESC LIMIT 1"

    connection = connect_to_database()
    if connection:
        result = execute_query(connection, select_last_glpi_query)
        if result:
            if result != last_query:
                last_query = result
                name, date, content, users_id_recipient = result[0]
                contents = content.replace('&#60;p&#62;', '')
                message = f"Обнаружен новый запрос в базе данных glpi_tickets!\nИмя: {name}\nДата: {date}\nСодержание: {contents}\nID пользователя: {users_id_recipient}"
                send_telegram_message_to_group(message)
        # Закрытие соединения с базой данных
        connection.close()


# Цикл для проверки новых запросов каждые 10 секунд
while True:
    check_for_new_queries()
    time.sleep(10)
