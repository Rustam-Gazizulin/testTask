from flask import Flask
from config import config
from routes import victorina


app = Flask(__name__)


def page_not_found(error):
    return '<h1>Страница не найдена.</h1>', 404




if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(victorina.main, url_prefix='/api/victorina')

    app.register_error_handler(404, page_not_found)
    app.run()
