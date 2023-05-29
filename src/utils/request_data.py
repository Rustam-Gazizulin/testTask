import requests

from utils.data_cheking import get_id_database


# Функция запроса данных с АПИ и конвертация для БД
def request_to_api(url_api: str, count_questions: int):
    id_database = get_id_database()
    output_data = []
    while int(count_questions) > 0:
        response = requests.get(f'{url_api}{count_questions}')
        data = response.json()
        count = 0
        for obj in data:
            if not obj.get("id") in id_database:
                id = obj.get("id")
                text_question = obj.get("question")
                answer_question = obj.get("answer")
                date_created = obj.get("created_at")
                extracted_data = {
                    "id": id,
                    "text_question": text_question,
                    "answer_question": answer_question,
                    "date_created": date_created
                }
                output_data.append(extracted_data)
            else:
                count += 1
                continue
        if count > 0:
            count_questions = count
        else:
            count_questions = 0
    return output_data

