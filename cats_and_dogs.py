from flask import Flask, escape, url_for, request, render_template, send_from_directory
from tensorflow.keras.preprocessing.image import load_img
from werkzeug.utils import secure_filename
import os
import model_cnd 

app = Flask(__name__)
cur_dir = os.getcwd()

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		try:
			img = request.files['load_img']
			img_path = '/static/images/' + secure_filename(img.filename)
			img.save(cur_dir+img_path)
			answer = model_cnd.run_example(cur_dir+img_path)
			return render_template('index.html', method=request.method, answer=answer, load_img=img_path)

		except Exception as e:
			print(e)
			answer = 'Please, select image!'
			return render_template('index.html', method=request.method, answer=answer)
		
	return render_template('index.html', method=request.method)



