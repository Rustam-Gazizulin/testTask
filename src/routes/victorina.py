import os

from flask import Blueprint, jsonify, request, render_template, redirect

from models.entities.victorina import Questions
from models.victorina_model import VictorinaModel
from utils.request_data import request_to_api

main = Blueprint('victorina_blueprint', __name__)
api_url = os.getenv('API_URL')


# Вывод списка вопросов
@main.route('/', methods=['GET'])
def get_questions():
    try:
        questions = VictorinaModel.get_questions()
        return render_template('list_question.html', data=questions)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Вывод 1 вопроса по указанному id
@main.route('/<id>')
def get_question(id):
    try:
        question = VictorinaModel.get_question(id)
        if question is not None:
            return render_template('retrieve_page.html', quest=question)
        else:
            return jsonify({"error": "Такого вопроса нет в базе данных"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Добавление вопросов в БД
@main.route('/add', methods=['POST', 'GET'])
def add_question():
    if request.method == 'POST':
        count = request.form['count']
        if count != '':
            list_question = request_to_api(api_url, int(count))
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
        else:
            return render_template('generate.html')
        return redirect('/api')
    return render_template('generate.html')


# Обновление данных существующего вопроса
@main.route('/update/<id>', methods=['POST', 'GET'])
def update_question(id):
    question = VictorinaModel.get_question(id)

    if request.method == 'POST':
        id = question['id']
        answer_question = request.form['answer_question']
        text_question = request.form['text_question']
        date_created = request.form['date_created']
        quest = Questions(id, answer_question, text_question, date_created)

        VictorinaModel.update_question(quest)

        return redirect('/api')

    return render_template('update_page.html', question=question)


# Удаление из БД вопроса по ID
@main.route('/delete/<id>')
def delete_question(id):
    try:
        question = Questions(id)

        affected_rows = VictorinaModel.delete_question(question)
        if affected_rows == 1:
            # return render_template('delete_question.html')
            return redirect('/api')
        else:
            return jsonify({"message": "Ошибка такого фильма нет в базе данных"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
