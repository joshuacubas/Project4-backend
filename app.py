from flask import Flask
import models

DEBUG=True
PORT=8000

app = Flask(__name__)



@app.route('/')
def hello():
	return 'Hello, World. Testing ... 1 ... 2 ... 3'
	print('sdjfhskdj')


































if __name__=='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)