from flask import Flask, request, render_template
import numpy as np
from src.CarPrice.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            car_age = int(request.form['car_age'])
            Present_Price = float(request.form['Present_Price'])
            Kms_Driven = int(request.form['Kms_Driven'])
            Kms_Driven2 = np.log(Kms_Driven)
            Owner = int(request.form['Owner'])
            Fuel_Type_Petrol = 1 if request.form['Fuel_Type_Petrol'] == 'Petrol' else 0
            Fuel_Type_Diesel = 1 - Fuel_Type_Petrol
            Seller_Type_Individual = 1 if request.form['Seller_Type_Individual'] == 'Individual' else 0
            Transmission_Mannual = 1 if request.form['Transmission_Mannual'] == 'Manual' else 0

            # Create a CustomData instance
            custom_data = CustomData(
                Present_Price=Present_Price,
                Kms_Driven=Kms_Driven2,
                Owner=Owner,
                car_age=car_age,
                Fuel_Type='Petrol' if Fuel_Type_Petrol == 1 else 'Diesel',
                Seller_Type='Individual' if Seller_Type_Individual == 1 else 'Dealer',
                Transmission='Manual' if Transmission_Mannual == 1 else 'Automatic'
            )

            # Create a PredictPipeline instance
            pipeline = PredictPipeline()

            # Get the data as a DataFrame
            data_as_df = custom_data.get_data_as_dataframe()

            # Make a prediction using the pipeline
            prediction = pipeline.predict(data_as_df)

            # Check if the prediction is negative
            if prediction < 0:
                return render_template('index.html', prediction_text="Sorry, you cannot sell this car")

            # Display the prediction
            return render_template('index.html', prediction_text="You can sell the car at {:.2f}".format(prediction[0]))

        except Exception as e:
            return render_template('index.html', prediction_text="Error: {}".format(e))

if __name__ == "__main__":
    application.run(debug=True)
