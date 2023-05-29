# testTask
___
## Description
Простое Flask API зарашивает данные(вопросы для проведения интелектуальной викторины) со стороннего API, количество вопросов определяет сам пользователь при GET запросе. Приложение валидирует
полученные данные и сохраняет в базу данных postgresQL, также приложение делет проверку на повторяющиеся вопросы если вопрос уже был ранее сахранен в БД приложение будет самостоятельно делать
повторные запросы на получение новых данных пока не наберт указанное пользователем количество уникальных вопросов. 
## install
- Скопировать репозиторий на ПК
- Запустить командой docker-compose up -d

### Функционал
GET - localhost:api/ # Получить список вопросов сохраненных в БД  

POST - localhost:api/<int>  # Запустить генерацию вопросов с последующим сохранением БД  
  
GET - localhost:api/<id> # Запросить из БД конкретный вопрос по его уникальному ID  
  
PUT - localhost:api/update/<id> # Внести правки в сохраненном в БД вопросе  
  
DELETE - localhost:api/<id> # Удалить вопрос из БД


