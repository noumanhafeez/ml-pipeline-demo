# House Price Predictor

**A simple machine learning project for predicting house prices using Linear Regression. Includes data preprocessing, model training, logging, and automated testing with GitHub Actions.**

---

## Features

* Linear Regression model for house price prediction
* Data preprocessing and train-test split
* Logging to track data and model metrics
* Automated CI pipeline using GitHub Actions

---

## Project Structure

```
ml_project/
│
├── data/                   # Dataset (house_prices.csv)
├── src/                    # Python scripts
│   ├── preprocess.py       # Data loading and preprocessing
│   ├── train.py            # Model training and evaluation
│   └── utils.py            # Logger setup
├── logs/                   # Log files
├── requirements.txt        # Python dependencies
└── .github/workflows/ci.yml  # GitHub Actions workflow
```

---

## Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your dataset**

Place a CSV file named `house_prices.csv` in the `data/` folder with at least the following columns:

* `square_feet`
* `num_rooms`
* `price`

4. **Run preprocessing**

```bash
python src/preprocess.py
```

5. **Train the model**

```bash
python src/train.py
```

6. **Check logs**

Logs will be saved in `logs/app.log` and printed in the console.

---

## GitHub Actions

* Runs preprocessing and training automatically on push or pull request to `main` branch
* Ensures code runs without errors before merging

---

## License

This project is licensed under the MIT License.
