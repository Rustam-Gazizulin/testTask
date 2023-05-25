from src.database.db import get_connection

connection = get_connection()
#
cursor = connection.cursor()
# cursor.execute("SELECT id, text_question, answer_question, date_created FROM questions ORDER BY answer_question ASC")
# resultset = cursor.fetchall()
create_table_query = '''CREATE TABLE questions
                      (ID INT PRIMARY KEY,
                      text_question TEXT,
                      answer_question VARCHAR(255),
                      date_created DATE); '''
# # Выполнение команды: это создает новую таблицу
cursor.execute(create_table_query)
connection.commit()
print("Таблица успешно создана в PostgreSQL")
#
# cursor.execute("SELECT text_question FROM questions")
# result = cursor.fetchall()
# print(resultset)