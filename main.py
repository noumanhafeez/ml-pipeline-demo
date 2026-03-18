# main.py
from model.train import train  # import train function
# No need to import src.utils here, train handles logging

if __name__ == "__main__":
    data_path = "data/housing.csv"
    target_column = "price"

    # Run training
    model_pipeline = train(data_path, target_column)