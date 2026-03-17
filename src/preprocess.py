import pandas as pd
from sklearn.model_selection import train_test_split
from utils import get_logger

logger = get_logger("Preprocess")

def load_data(path="data/house_prices.csv"):
    logger.info(f"Loading data from {path}")
    df = pd.read_csv(path)
    logger.info(f"Data shape: {df.shape}")
    return df

def preprocess(df):
    logger.info("Starting preprocessing")
    # Example: simple features
    X = df[['square_feet', 'num_rooms']]  # select relevant features
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logger.info(f"Split data: Train {X_train.shape}, Test {X_test.shape}")
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = load_data()
    preprocess(df)