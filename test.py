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

# "age",
#     "gender",  # Assuming "gender" corresponds to "sex"
#     "cp",
#     "trestbps",
#     "chol",
#     "fbs",
#     "restecg",
#     "thalach",
#     "exang",
#     "oldpeak",
#     "slope",
#     "ca",
#     "thal",
#     "target"

data = {
    "age": "59",
    "sex": "1",
    "cp": "1",
    "trestbps": "140",
    "chol": "221",
    "fbs": "0",
    "restecg": "1",
    "thalach": "164",
    "exang": "1",
    "oldpeak": "0.0",
    "slope": "2",
    "ca": "0",
    "thal": "2",
}
# 60	1	0	125	258	0	0	141	1	2.8	1	1	3	0

data = {
    "age": "60",
    "sex": "1",
    "cp": "0",
    "trestbps": "125",
    "chol": "258",
    "fbs": "0",
    "restecg": "0",
    "thalach": "141",
    "exang": "1",
    "oldpeak": "2.8",
    "slope": "1",
    "ca": "1",
    "thal": "3",
}

# 50	0	0	110	254	0	0	159	0	0.0	2	0	2	1

data = {
    "age": "50",
    "sex": "0",
    "cp": "0",
    "trestbps": "110",
    "chol": "254",
    "fbs": "0",
    "restecg": "0",
    "thalach": "159",
    "exang": "0",
    "oldpeak": "0",
    "slope": "2",
    "ca": "0",
    "thal": "2",
}

# 54	1	0	120	188	0	1	113	0	1.4	1	1	3	0

data = {
    "age": "54",
    "sex": "1",
    "cp": "0",
    "trestbps": "120",
    "chol": "188",
    "fbs": "0",
    "restecg": "1",
    "thalach": "113",
    "exang": "0",
    "oldpeak": "1.4",
    "slope": "1",
    "ca": "1",
    "thal": "3",
}


# data = {
#     "sbp": "140",
#     "alcohol": "0",
#     "glucose": "1",
#     "dbp": "90",
#     "gender": "1",
#     "activity": "1",
#     "smoking": "0",
#     "weight": "85",
#     "cholesterol": "3",
#     "age": "20228",
#     "height": "156",
# }

response = requests.post(url, data=data)
print(response.json())


# input ImmutableMultiDict([('age', '20228'), ('height', '156'), ('weight', '85.0'), ('gender', '1'), ('sbp', '140'), ('dbp', '90'), ('cholesterol', '3'), ('glucose', '1'), ('smoking', '0'), ('alcohol', '0'), ('activity', '1')])
# data_dict {'age': 20228.0, 'height': 156.0, 'weight': 85.0, 'gender': 1.0, 'sbp': 140.0, 'dbp': 90.0, 'cholesterol': 3.0, 'glucose': 1.0, 'smoking': 0.0, 'alcohol': 0.0, 'activity': 1.0}
# prediction_list [1]
# input ImmutableMultiDict([('sbp', '140'), ('alcohol', '0'), ('glucose', '1'), ('dbp', '90'), ('gender', '1'), ('activity', '1'), ('smoking', '0'), ('weight', '85'), ('cholesterol', '3'), ('age', '20228'), ('height', '156')])
# data_dict {'sbp': 140.0, 'alcohol': 0.0, 'glucose': 1.0, 'dbp': 90.0, 'gender': 1.0, 'activity': 1.0, 'smoking': 0.0, 'weight': 85.0, 'cholesterol': 3.0, 'age': 20228.0, 'height': 156.0}
# prediction_list [0]
# 127.0.0.1 - - [18/Feb/2024:14:45:58 +0000] "POST /predict HTTP/1.1" 200 19 "-" "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X671 Build/SP1A.210812.016)"
