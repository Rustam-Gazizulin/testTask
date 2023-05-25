import os

from flask import Blueprint, jsonify, request
from src.models.victorina_model import VictorinaModel
from src.models.entities.victorina import Questions
from src.utils.request_data import request_to_api

main = Blueprint('victorina_blueprint', __name__)
api_url = os.getenv('API_URL')


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
@main.route('/add/<count>', methods=['POST'])
def add_question(count):
    list_question = request_to_api(api_url, count)
    for quest in list_question:
        try:
            answer_question = quest['answer_question']
            text_question = quest['text_question']
            date_created = quest['date_created']
            id = quest['id']
            question = Questions(id, answer_question, text_question, date_created)

            affected_rows = VictorinaModel.add_question(question)

            if affected_rows == 1:
                continue
            else:
                return jsonify({"message": "Ошибка создания вопроса проверьте корректность полей"}), 500

        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    return 'Вопросы сгенерированы'


# Обновление данных существующего вопроса
@main.route('/update/<id>', methods=['PUT'])
def update_question(id):
    try:
        answer_question = request.json['answer_question']
        text_question = request.json['text_question']
        date_created = request.json['date_created']
        question = Questions(id, answer_question, text_question, date_created)

        affected_rows = VictorinaModel.update_question(question)

        if affected_rows == 1:
            return jsonify(question.id)
        else:
            return jsonify({"message": "Ошибка обновления такого вопроса нет в базе"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Удаление из БД вопроса по ID
@main.route('/delete/<id>', methods=['DELETE'])
def delete_question(id):
    try:
        question = Questions(id)

        affected_rows = VictorinaModel.delete_question(question)
        if affected_rows == 1:
            return jsonify(question.id)
        else:
            return jsonify({"message": "Ошибка такого фильма нет в базе данных"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
