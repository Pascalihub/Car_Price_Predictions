from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.CarPrice.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

## Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            car_age = int(request.form['car_age'])
            Present_Price = float(request.form['Present_Price'])
            Kms_Driven = int(request.form['Kms_Driven'])
            Kms_Driven2 = np.log(Kms_Driven)
            Owner = int(request.form['Owner'])
            Fuel_Type_Petrol = 1 if request.form['Fuel_Type'] == 'Petrol' else 0
            Fuel_Type_Diesel = 1 - Fuel_Type_Petrol
            Seller_Type_Individual = 1 if request.form['Seller_Type'] == 'Individual' else 0
            Transmission_Mannual = 1 if request.form['Transmission'] == 'Manual' else 0

            # Create a CustomData instance
            custom_data = CustomData(
                Present_Price=Present_Price,
                Kms_Driven=Kms_Driven,
                Owner=Owner,
                car_age=car_age,
                Fuel_Type='Petrol' if Fuel_Type_Petrol == 1 else 'Diesel',
                Seller_Type='Individual' if Seller_Type_Individual == 1 else 'Dealer',
                Transmission='Manual' if Transmission_Mannual == 1 else 'Automatic'
            )
            
            # Assuming you have a predict method in your PredictPipeline class
            output = PredictPipeline().predict(custom_data)

            if output < 0:
                return render_template('home.html', prediction_text="Sorry you cannot sell this car")
            else:
                return render_template('home.html', prediction_text="You Can Sell The Car at {}".format(output))

        except Exception as e:
            return render_template('home.html', prediction_text="An error occurred: {}".format(str(e)))

if __name__ == "__main__":
    app.run(debug=True)
