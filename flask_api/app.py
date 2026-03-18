# app.py
from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
import os

app = Flask(__name__, static_folder="frontend")

# Load trained model
model = joblib.load("artifacts/house_price_pipeline.pkl")


# Serve frontend UI
@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]

        return jsonify({"prediction": float(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)