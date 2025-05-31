# 🧠 Influence-Weighted Sentiment for Stock Return Forecasting

This repository contains the code for our Master's thesis, where we study whether investor sentiment extracted from X (formerly Twitter) improves return forecasting when weighted by user influence. We compare models using raw sentiment versus an **influence-weighted sentiment variable** across four forecasting methods.

---

## 📥 1. Data Collection

We collect:
- Social media posts from X related to the S&P 500
- Market data (S&P 500, VIX) using the Yahoo Finance API
- Macroeconomic indicators

Relevant scripts:
- [`src/data/collect_posts.py`](src/data/collect_posts.py)
- [`src/data/download_market_data.py`](src/data/download_market_data.py)

---

## 💬 2. Sentiment Variable Creation

### Sentiment Extraction  
We use fine-tuned transformer models to classify post sentiment:
- RoBERTa → [`src/sentiment/roberta_sentiment.py`](src/sentiment/roberta_sentiment.py)
- FinBERT → [`src/sentiment/finbert_sentiment.py`](src/sentiment/finbert_sentiment.py)

### Influence Weighting  
Sentiment scores are weighted by user influence using:

`influence = followers * (likes + reposts + 1)`

Implemented in:  
- [`src/features/create_influence_weighted_sentiment.py`](src/features/create_influence_weighted_sentiment.py)

---

## 📈 3. Forecasting Models

We evaluate four forecasting models using both raw and influence-weighted sentiment variables:

- **Ridge Regression**  
  [`src/models/ridge_model.py`](src/models/ridge_model.py)

- **Random Forest**  
  [`src/models/random_forest.py`](src/models/random_forest.py)

- **XGBoost**  
  [`src/models/xgboost_model.py`](src/models/xgboost_model.py)

- **LSTM (Deep Learning)**  
  [`src/models/lstm_model.py`](src/models/lstm_model.py)

---

Let me know if you'd like help generating a `requirements.txt` or running instructions.
