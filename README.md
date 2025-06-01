# 🧠 Influence-Weighted Sentiment for Stock Return Forecasting

This repository contains the code for our Master's thesis, which explores whether investor sentiment extracted from X (formerly Twitter) becomes more predictive when weighted by user influence. The main focus is on constructing a novel **influence-weighted sentiment variable** and comparing its forecasting performance to raw sentiment across four models.

---

## 📥 1. Data Collection

Social media posts are scraped from X and financial data (S&P 500, VIX, and macroeconomic indicators) is retrieved using the Yahoo Finance API.

**Folder:** `Data scrapers`  
Contains scripts and notebooks for collecting X posts and downloading financial market data.

---

## 💬 2. Sentiment Variable Creation

We use large language models (RoBERTa and FinBERT) to classify tweet sentiment. These sentiment labels are then weighted based on user influence, measured by follower count, likes, and reposts.

**Folder:** `Sentiment analysis`  
Contains fine-tuning scripts and sentiment inference models for post classification.

**Notebook:** `Constructing sentiment.ipynb`  
Illustrates how influence-weighted sentiment scores are calculated.

---

## 💼 3. Financial Data Integration

The influence-weighted sentiment data is merged with return data and financial indicators to create the final modeling dataset.

**Folder:** `Combining financial data`  
Contains notebooks for aligning sentiment data with S&P 500 returns, volatility, and macroeconomic variables.

---

## 📈 4. Forecasting Models

We evaluate predictive performance using:

- Ridge Regression  
- Random Forest  
- XGBoost  
- LSTM (Deep Learning)

**Folder:** `Models`  
Contains all scripts and notebooks for model training, validation, and performance comparison.

---

This repository includes all necessary components to reproduce the creation of sentiment variables and run forecasting experiments for the thesis.
