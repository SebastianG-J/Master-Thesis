# 🧠 Influence-Weighted Sentiment for Stock Return Forecasting

This repository contains the code for our Master's thesis exploring whether investor sentiment extracted from X (formerly Twitter) becomes more predictive when weighted by user influence. We construct an **influence-weighted sentiment variable** and evaluate its forecasting performance using four different models.

---

## 📥 1. Data Collection

Social media data is collected and scraped using:
- [`Data scrapers/selenium.ipynb`](Data%20scrapers/selenium.ipynb)

Market and financial data (S&P 500, VIX, macro variables) is handled in:
- [`Combining financial data/Data Preprocessing (yfinance + sentiment) .ipynb`](Combining%20financial%20data/Data%20Preprocessing%20%28yfinance%20+%20sentiment%29%20.ipynb)

---

## 💬 2. Sentiment Variable Creation

### Sentiment Classification  
Posts are classified using RoBERTa and FinBERT in:
- [`Sentiment analysis/`](Sentiment%20analysis/)

### Influence Weighting  
Sentiment is adjusted by engagement metrics (likes, reposts, follower count) in:
- [`Constructing sentiment.ipynb`](Constructing%20sentiment.ipynb)

---

## 📈 3. Forecasting Models

The following models are used to evaluate prediction performance:

- **Ridge Regression**  
  [`Models/ridge_model.py`](Models/ridge_model.py)

- **Random Forest**  
  [`Models/random_forest.py`](Models/random_forest.py)

- **XGBoost**  
  [`Models/xgboost_model.py`](Models/xgboost_model.py)

- **LSTM**  
  [`Models/lstm_model.py`](Models/lstm_model.py)
