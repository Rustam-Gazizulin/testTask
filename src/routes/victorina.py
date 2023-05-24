from flask import Blueprint, jsonify
from src.models.victorina_model import VictorinaModel


main = Blueprint('victorina_blueprint', __name__)


@main.route('/')
def get_question():
    try:
        questions = VictorinaModel.get_victorina()
        return jsonify(questions)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
