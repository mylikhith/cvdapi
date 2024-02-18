import requests

url = "http://127.0.0.1:5000/predict"
# data = {
#     "age": 18393,
#     "gender": 2,
#     "height": 168,
#     "weight": 62.0,
#     "ap_hi": 110,
#     "ap_lo": 80,
#     "cholesterol": 1,
#     "gluc": 1,
#     "smoke": 0,
#     "alco": 0,
#     "active": 1,
# }

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
