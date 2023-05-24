from src.database.db import get_connection
from src.models.entities.victorina import Questions


class VictorinaModel:
    @classmethod
    def get_questions(self):
        try:
            connection = get_connection()
            questions = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, text_question, answer_question, date_created FROM questions")
                resultset = cursor.fetchall()

                for row in resultset:
                    question = Questions(row[0], row[1], row[2], row[3])
                    questions.append(question.to_json())
            connection.close()
            return questions

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_question(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, text_question, answer_question, date_created FROM questions WHERE id = %s", (id,))
                row = cursor.fetchone()

                question = None
                if row != None:
                    question = Questions(row[0], row[1], row[2], row[3])
                    question = question.to_json()

            connection.close()
            return question

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_question(self, question):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO questions (id, text_question, answer_question, date_created) 
                        VALUES (%s, %s, %s, %s)""", (question.id, question.text_question, question.answer_question,
                                                     question.date_created))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_question(self, question):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM questions WHERE id = %s", (question.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)