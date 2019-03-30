from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
##remove when in production

from app import api


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
