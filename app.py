from flask import Flask
from src.config import config
from src.database.create_table import create_table
from src.routes import victorina


app = Flask(__name__)

create_table()


@app.route('/')
def page_not_found():
    return '<h1>Стартовая страница</h1>'


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(victorina.main, url_prefix='/api')

    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5050)
