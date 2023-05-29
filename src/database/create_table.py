from src.database.db import get_connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS questions
                          (ID INT PRIMARY KEY,
                          text_question TEXT,
                          answer_question VARCHAR(255),
                          date_created DATE); '''

    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    print("Таблица успешно создана в PostgreSQL")
