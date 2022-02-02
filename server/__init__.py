from flask import Flask, request, jsonify

global model

def assign_model(model_):
	print("Assign invoked")
	global model
	model = model_
	print(model)
	run_flask()


assign_model = assign_model

flask_server = Flask(__name__, static_url_path='', static_folder='../static')

@flask_server.route('/')
def hello_world():
	print("ENDPOINT")
	print(model)
	model.generate("Some str")

	# from ..run import Singltone
	 
	return flask_server.send_static_file('./index.html')

def run_flask():
	print("run flask")
	flask_server.run(host= '0.0.0.0',debug=True)
