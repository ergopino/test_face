from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import api, models


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
