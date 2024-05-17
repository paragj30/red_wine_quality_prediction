from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlproject.pipelines.prediction import PredictionPipeline, CustomData
from mlproject.exception import CustomException
import sys
from mlproject import logger

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")



@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            data = CustomData(
                 fixed_acidity =float(request.form['fixed_acidity']),
                 volatile_acidity =float(request.form['volatile_acidity']),
                 citric_acid =float(request.form['citric_acid']),
                 residual_sugar =float(request.form['residual_sugar']),
                 chlorides =float(request.form['chlorides']),
                 free_sulfur_dioxide =float(request.form['free_sulfur_dioxide']),
                 total_sulfur_dioxide =float(request.form['total_sulfur_dioxide']),
                 density =float(request.form['density']),
                 pH =float(request.form['pH']),
                 sulphates =float(request.form['sulphates']),
                 alcohol =float(request.form['alcohol']))
       
            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictionPipeline()
            logger.info("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            logger.info(f'Prediction Result: {results}')
            return render_template('results.html', prediction = str(results))

            
        except Exception as e:
            CustomException(e, sys)
            return 'Something is wrong with code'

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)