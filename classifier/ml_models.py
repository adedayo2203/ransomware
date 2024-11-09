import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

# Load the trained models
rf_model = joblib.load('./models/hypertuned_rf_model.joblib') 
nb_model = joblib.load('./models/hypertuned_nb_model.joblib')

def predict_ransomware(features, model_type='rf'):
    features = np.array(features).reshape(1, -1)
    if model_type == 'rf':
        prediction = rf_model.predict(features)
    elif model_type == 'nb':
        prediction = nb_model.predict(features)
    else:
        raise ValueError("Invalid model type. Choose 'rf' or 'nb'.")
    return "Benign" if prediction[0] == 1 else "Malicious"