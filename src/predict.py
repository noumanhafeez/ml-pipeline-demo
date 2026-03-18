# predict.py
import pandas as pd
import joblib
from utils import get_logger
from pathlib import Path

# Create a logger
logger = get_logger("predict", "logs/predict.log")

try:
    logger.info("Starting prediction script.")

    # Load the saved pipeline
    model_path = Path("../artifacts/house_price_pipeline.pkl")
    logger.info(f"Loading trained pipeline from {model_path}")
    pipeline = joblib.load(model_path)

    # Load new data
    data_path = Path("../data/new_house.csv")
    logger.info(f"Loading new data from {data_path}")
    new_data = pd.read_csv(data_path)
    logger.info(f"New data loaded. Shape: {new_data.shape}")

    # Predict
    predictions = pipeline.predict(new_data)
    logger.info(f"Predictions made successfully. Sample predictions: {predictions[:5]}")

    # Optionally save predictions to CSV
    output_path = Path("../data/new_house_predictions.csv")
    new_data["Predicted_Price"] = predictions
    new_data.to_csv(output_path, index=False)
    logger.info(f"Predictions saved to {output_path}")

except FileNotFoundError as e:
    logger.error(f"File not found: {e}")
    raise
except Exception as e:
    logger.error(f"Prediction failed: {e}")
    raise