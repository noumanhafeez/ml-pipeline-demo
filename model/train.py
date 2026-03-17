from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from src.preprocess import load_data, preprocess
from src.utils import get_logger

logger = get_logger("Train")

def train_model():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess(df)

    logger.info("Training Linear Regression model")
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    logger.info(f"Model evaluation: MSE={mse:.2f}, R2={r2:.2f}")

    # Save model
    joblib.dump(model, "house_price_model.pkl")
    logger.info("Model saved to house_price_model.pkl")

if __name__ == "__main__":
    train_model()