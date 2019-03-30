from app import app
from flask_restful import Api
from app.resources.resources import Recogn
## API Setup ##
api = Api(app)

# NOTE: maybe use 'url_for(...)' + concatenation instead of hard coding URIs

api.add_resource(Recogn,
				'/createUser',
				endpoint='createUser')


