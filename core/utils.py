import pickle
from typing import Optional
import glob

import joblib
import pandas as pd


def predict_car_price(df: pd.DataFrame):
    result = joblib.load('C:\\Users\\PC\\price_prediction\\price_prediction_notebook\\first_estimation.pkl')

    return result.predict(df)
