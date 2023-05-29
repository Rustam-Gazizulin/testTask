from flask import Flask
from database.create_table import create_table
from routes import victorina


app = Flask(__name__)

create_table()


@app.route('/')
def page_not_found():
    return '<h1>Стартовая страница</h1>'


if __name__ == '__main__':

    app.register_blueprint(victorina.main, url_prefix='/api')

    app.run(debug=True, host='0.0.0.0', port=5000)
