# myapp/model_utils.py
import joblib
import pandas as pd
import numpy as np
from sklearn import set_config
import warnings

warnings.filterwarnings('ignore')
set_config(display='diagram',transform_output='pandas')


pipeline = joblib.load('./savedModels/full_pipeline.joblib')


def predict(sample):
    print('\n--Predict--\n')
    
    column_mapping = {
        'user_id':'User ID' ,
        'user_name':'User Name',
        'driver_name':'Driver Name',
        'car_condition':'Car Condition',
        'weather':'Weather',
        'traffic_condition':'Traffic Condition'}
    sample = sample.rename(columns=column_mapping)
    print('\n--sample--\n',sample)
    prediction = pipeline.predict(sample)
    print('\n--prediction--\n',prediction)
    # Make a prediction
    prediction = prediction.reshape(-1,1)
    prediction = np.expm1(prediction)
    print('\n--Corrected Prediction--:\t',prediction)
    return prediction
