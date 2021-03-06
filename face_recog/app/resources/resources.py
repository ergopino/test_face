import datetime
from app import app,db
from flask import abort,request
from flask_restful import Resource, reqparse, marshal, fields
import pandas as pd
import face_recognition
from scipy.spatial.distance import cdist



#### ---- RESOURCES ---- ###
# TODO: Error handling for duplicate DB PK data on POST
#	   (atm client gets splattered with ugly error messages)


#@app.route('/NS', methods=['GET'])

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
	return 'Flask Dockerized'

class Recogn(Resource):
	def get(self):
		return "lala"

@app.route('/picture', methods=['GET', 'POST'])
def pic():
	
	if request.method == 'GET':
		return 'Flask Dockerized'
	
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)

		file_image = request.files['file']

		if file_image.filename == '':
			return redirect(request.url)

		if file_image and allowed_file(file_image.filename):
	
			# Load the uploaded image file
			img = face_recognition.load_image_file(file_image)

			# Get face encodings for any faces in the uploaded image
			uploaded_faces = face_recognition.face_encodings(img)

			# Defaults for the result object
			faces_found = len(uploaded_faces)
			faces = []

			if faces_found:
				for face in uploaded_faces:
					print (face)
					#~ query = "INSERT INTO vectors (file, vec_low, vec_high) VALUES ('{}', CUBE(array[{}])))".format(
							#~ "lala",
							#~ ','.join(str(s) for s in face[0][0:128]),
						#~ )
					#~ db.execute(query)
		#if len(encodings) > 0:
			
	
	#~ def __init__(self):
		#~ self.reqparse = reqparse.RequestParser()
		#~ self.reqparse.add_argument('name', dest= 'name',
								   #~ required=True,
								   #~ type=str,
								   #~ help='No valid name provided for species')
		#~ super(SpeciesListAPI, self).__init__()

	#~ @auth_token_required
	#~ def post(self):
		#~ args = self.reqparse.parse_args(strict=True)
		#~ check_len(args['name'])
		#~ species = Species(args['name'])
		#~ db.session.add(species)
		#~ db.session.commit()
		#~ return marshal(species, species_fields), 201
		return "lala"


#### ---- AUXILIARY METHODS ---- ###

def is_picture(filename):
	image_extensions = ['png', 'jpg', 'jpeg', 'gif']
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in image_extensions


def get_all_picture_files(path):
	files_in_dir = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
	return [f for f in files_in_dir if is_picture(f)]


def remove_file_ext(filename):
	return splitext(filename.rsplit('/', 1)[-1])[0]

def calc_face_encoding(image):
	# Currently only use first face found on picture
	loaded_image = face_recognition.load_image_file(image)
	faces = face_recognition.face_encodings(loaded_image)

	# If more than one face on the given image was found -> error
	#~ if len(faces) > 1:
		#~ raise Exception(
			#~ "Found more than one face in the given training image.")

	# If none face on the given image was found -> error
	if not faces:
		raise Exception("Could not find any face in the given training image.")

	return faces,os.path.basename(image)


def load_images(path):
	col_names =  ['encondings', 'name']
	my_df  = pd.DataFrame(columns = col_names)
	files_in_dir = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
	
	for image in files_in_dir:
		faces,name=calc_face_encoding(image)
		for face in faces:
			my_df.loc[len(my_df)] = [face,name]
	
	return	


def detect_faces_in_image(file_stream):
	# Load the uploaded image file
	img = face_recognition.load_image_file(file_stream)

	# Get face encodings for any faces in the uploaded image
	uploaded_faces = face_recognition.face_encodings(img)

	# Defaults for the result object
	faces_found = len(uploaded_faces)
	faces = []

	if faces_found:
		
		for face in faces_found:
			
			dist = cdist( face, my_df, metric='euclidean')
			
		
		#~ face_encodings = list(faces_dict.values())
		#~ for uploaded_face in uploaded_faces:
			#~ match_results = face_recognition.compare_faces(
				#~ face_encodings, uploaded_face)
			#~ for idx, match in enumerate(match_results):
				#~ if match:
					#~ match = list(faces_dict.keys())[idx]
					#~ match_encoding = face_encodings[idx]
					#~ dist = face_recognition.face_distance([match_encoding],
							#~ uploaded_face)[0]
					#~ faces.append({
						#~ "id": match,
						#~ "dist": dist
					#~ })
	return
	
