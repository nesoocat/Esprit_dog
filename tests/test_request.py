import requests

url_base = 'http://127.0.0.1:8000'

response = requests.get(f'{url_base}/')
print('GET / response:', response.text)

data_predict = {
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 79,
    "BMI": 25.6,
    "DiabetesPedigreeFunction": 0.351,
    "Age": 33
}

response = requests.post(f'{url_base}/predict', json=data_predict)
print('POST /predict response:', response.text)