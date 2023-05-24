from flask import Blueprint, jsonify, request
from src.models.victorina_model import VictorinaModel
from src.models.entities.victorina import Questions


main = Blueprint('victorina_blueprint', __name__)

# Вывод списка вопросов
@main.route('/')
def get_questions():
    try:
        questions = VictorinaModel.get_questions()
        return jsonify(questions)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Вывод 1 вопроса по указанному id
@main.route('/<id>')
def get_question(id):
    try:
        question = VictorinaModel.get_question(id)
        if question is not None:
            return jsonify(question)
        else:
            return jsonify({"error": "Такого вопроса нет в базе данных"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Добавление вопроса в БД самостоятельно
@main.route('/add', methods=['POST'])
def add_question():
    try:
        answer_question = request.json['answer_question']
        text_question = request.json['text_question']
        date_created = request.json['date_created']
        id = request.json['id']
        question = Questions(id, answer_question, text_question, date_created)

        affected_rows = VictorinaModel.add_question(question)

        if affected_rows == 1:
            return jsonify(question.id)
        else:
            return jsonify({"message": "Ошибка создания вопроса проверьте корректность полей"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
