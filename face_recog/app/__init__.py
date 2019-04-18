from flask import Flask
import postgresql
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

try:
	dbURI = app.config['PSQL_DATABASE_URI']
	db = postgresql.open(dbURI)
except:
	continue

#from app import api, models
from app import api


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
