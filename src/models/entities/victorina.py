from src.utils.date_format import DateFormat

class Questions:

    def __init__(self, id, text_question=None, answer_question=None, date_created=None) -> None:
        self.id = id
        self.text_question = text_question
        self.answer_question = answer_question
        self.date_created = date_created

    def to_json(self):
        return {
            'id': self.id,
            'text_question': self.text_question,
            'answer_question': self.answer_question,
            'date_created': DateFormat.convert_date(self.date_created)
        }
