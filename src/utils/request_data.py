import requests


# Функция запроса данных с АПИ и конвертация для БД
def request_to_api(url_api: str, count_questions: int):
    response = requests.get(f'{url_api}{count_questions}')
    data = response.json()
    output_data = []
    for obj in data:
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
    return output_data

