from src.database.db import get_connection
from src.models.entities.victorina import Questions


class VictorinaModel:

    @classmethod
    def get_victorina(self):
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
