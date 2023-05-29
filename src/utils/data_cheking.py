from database.db import get_connection


# Функция для получения списка уникальных id из Базы данных
def get_id_database():
    id_database = []
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id FROM questions")
        resultset = cursor.fetchall()
    for num in resultset:
        id_database.append(num[0])

    return id_database


