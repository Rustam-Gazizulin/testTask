from flask import Blueprint, jsonify
from src.models.victorina_model import VictorinaModel


main = Blueprint('victorina_blueprint', __name__)


@main.route('/')
def get_questions():
    try:
        questions = VictorinaModel.get_questions()
        return jsonify(questions)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


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
