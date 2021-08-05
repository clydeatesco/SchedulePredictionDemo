import numpy as np
from flask import Flask, request, jsonify, render_template, Markup
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	print("final features >>>>>>>>>>>>>>>>>> ")
	print(final_features)
	prediction = model.predict(final_features)

	output = np.round(prediction[0], 2)
	html = 'Schedule Prediction: {}'.format(output)
	totaldays = 'Total Days: {}'.format(output[0])
	totalhrs = 'Total Hours: {}'.format(output[1])

	return render_template('index.html', prediction_text=html, total_days=totaldays, total_hours=totalhrs)

if __name__ == "__main__":
	app.run(debug=True)
