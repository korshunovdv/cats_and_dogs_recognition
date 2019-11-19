from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
 
# load model 
model =  load_model('final_model.h5')
# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(224, 224))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 224, 224, 3)
	# center pixel data
	img = img.astype('float32')
	return img
 
# load an image and predict the class
def run_example(img,model=model):
	# load the image
	img = load_image(img)
	# load model
	model = model
	# predict the class
	result = model.predict(img)
	# return result[0][0]
	if result[0][0] == 0:
		return 'It\'s cat!'
	else:
		return 'It\'s dog!'