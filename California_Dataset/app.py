from flask import Flask, render_template, request, jsonify
import pickle as pk
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve the input values from the form
        try:
            Tv = float(request.form['tv_budget'])
            Radio = float(request.form['radio_budget'])
            Newspaper = float(request.form['newspaper_budget'])

            # Load the uploaded pickle file (model)
            file = request.files['model_file']
            model = pk.load(file)

            # Prepare the input for prediction
            input_data = np.array([[Tv, Radio, Newspaper]])

            # Make prediction
            predicted_sales = model.predict(input_data)

            # Return the result to the user
            return render_template('index1.html', predicted_sales=f"Predicted sales: ${predicted_sales[0]:.2f}")
        except Exception as e:
            return render_template('index1.html', error=f"Error: {str(e)}")
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
