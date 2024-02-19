from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained LightGBM model
model_filename = "heart_predict.pkl"
with open(model_filename, "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Cardiovascular Disease Prediction API!"


# data = {
#     "age": "59",
#     "sex": "1",
#     "cp": "1",
#     "trestbps": "140",
#     "chol": "221",
#     "fbs": "0",
#     "restecg": "1",
#     "thalach": "164",
#     "exang": "1",
#     "oldpeak": "0.0",
#     "slope": "2",
#     "ca": "0",
#     "thal": "2",
# }

EXPECTED_COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]

# EXPECTED_COLUMNS = [
#     "age",
#     "gender",
#     "height",
#     "weight",
#     "ap_hi",
#     "ap_lo",
#     "cholesterol",
#     "gluc",
#     "smoke",
#     "alco",
#     "active",
# ]


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extracting form data
        data_dict = {key: float(value) for key, value in request.form.items()}

        # Create DataFrame ensuring the column order
        query_df = pd.DataFrame([data_dict], columns=EXPECTED_COLUMNS)

        # Optional: Print to verify the DataFrame's column order for debugging
        print(query_df)

        # Make prediction
        prediction = model.predict(query_df)

        # Ensure output is in a serializable format
        prediction_list = prediction.tolist()

        return jsonify({"prediction": prediction_list})
    except Exception as e:
        return jsonify({"error": str(e)})
