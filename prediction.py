import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import joblib


def get_prediction(vars):
	xt = np.array(vars)
	xt = xt.reshape(1,-1)
	# load the model from disk
	loaded_model = joblib.load("finalized_model_rf1.sav")
	result = loaded_model.predict(xt)
	print(result)
	return result