import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host=config('POSTGRES_HOST'),
            user=config('POSTGRES_USER'),
            password=config('POSTGRES_PASSWORD'),
            database=config('POSTGRES_DB')
        )
    except DatabaseError as ex:
        raise ex


# connection = get_connection()
#
# cursor = connection.cursor()
# cursor.execute("SELECT id, text_question, answer_question, date_created FROM questions ORDER BY answer_question ASC")
# resultset = cursor.fetchall()
# create_table_query = '''CREATE TABLE mobile
#                       (ID INT PRIMARY KEY     NOT NULL,
#                       MODEL           TEXT    NOT NULL,
#                       PRICE         REAL); '''
# # Выполнение команды: это создает новую таблицу
# cursor.execute(create_table_query)
# connection.commit()
# print("Таблица успешно создана в PostgreSQL")
#
# cursor.execute("SELECT text_question FROM questions")
# result = cursor.fetchall()
# print(resultset)
