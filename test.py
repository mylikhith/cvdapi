import requests

url = "https://cvd-o2ov.onrender.com/predict"

data = {
    "age": "20228",
    "gender": "1",
    "height": "156",
    "weight": "85.0",
    "ap_hi": "140",
    "ap_lo": "90",
    "cholesterol": "3",
    "gluc": "1",
    "smoke": "0",
    "alco": "0",
    "active": "1",
}

response = requests.post(url, data=data)
print(response.json())
