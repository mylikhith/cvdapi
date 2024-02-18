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

# data = {
#     "age": "20228",
#     "gender": "1",
#     "height": "156",
#     "weight": "85.0",
#     "ap_hi": "140",
#     "ap_lo": "90",
#     "cholesterol": "3",
#     "gluc": "1",
#     "smoke": "0",
#     "alco": "0",
#     "active": "1",
# }

data = {
    "sbp": "140",
    "alcohol": "0",
    "glucose": "1",
    "dbp": "90",
    "gender": "1",
    "activity": "1",
    "smoking": "0",
    "weight": "85",
    "cholesterol": "3",
    "age": "20228",
    "height": "156",
}

response = requests.post(url, data=data)
print(response.json())


# input ImmutableMultiDict([('age', '20228'), ('height', '156'), ('weight', '85.0'), ('gender', '1'), ('sbp', '140'), ('dbp', '90'), ('cholesterol', '3'), ('glucose', '1'), ('smoking', '0'), ('alcohol', '0'), ('activity', '1')])
# data_dict {'age': 20228.0, 'height': 156.0, 'weight': 85.0, 'gender': 1.0, 'sbp': 140.0, 'dbp': 90.0, 'cholesterol': 3.0, 'glucose': 1.0, 'smoking': 0.0, 'alcohol': 0.0, 'activity': 1.0}
# prediction_list [1]
# input ImmutableMultiDict([('sbp', '140'), ('alcohol', '0'), ('glucose', '1'), ('dbp', '90'), ('gender', '1'), ('activity', '1'), ('smoking', '0'), ('weight', '85'), ('cholesterol', '3'), ('age', '20228'), ('height', '156')])
# data_dict {'sbp': 140.0, 'alcohol': 0.0, 'glucose': 1.0, 'dbp': 90.0, 'gender': 1.0, 'activity': 1.0, 'smoking': 0.0, 'weight': 85.0, 'cholesterol': 3.0, 'age': 20228.0, 'height': 156.0}
# prediction_list [0]
# 127.0.0.1 - - [18/Feb/2024:14:45:58 +0000] "POST /predict HTTP/1.1" 200 19 "-" "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X671 Build/SP1A.210812.016)"
