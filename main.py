from flask import Flask, request, jsonify
from pydantic import BaseModel
import pandas as pd
import joblib

#charger le modele
model = joblib.load('diabetes_model.pkl')

class InputData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age : float

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Bienvenue sur l'API de prédiction du diabète!"

@app.route('/predict', methods=['POST'])
def predict():
    if not request.json:
        return jsonify({'error': 'No data provided'}), 400
    try:
        input_data = InputData(**request.json)
        input_data_df =pd.DataFrame([input_data.dict()])
        prediction = model.predict(input_data_df)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)
