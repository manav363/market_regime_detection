# 📊 Market Regime Detection & Forecasting

A complete end-to-end Machine Learning research system that detects hidden market regimes, predicts regime transitions, summarizes market behavior, and produces a one-year forward outlook using real financial data.

This project demonstrates practical ML engineering, quantitative finance concepts, and real-world system design.

## Table of Contents

- [What This Project Does](#what-this-project-does)
- [Core Features](#core-features)
- [System Architecture](#system-architecture)
- [Installation & Setup](#installation--setup)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [How To Run](#how-to-run)
- [Example Outputs](#example-outputs)
- [Machine Learning Models](#machine-learning-models)
- [Disclaimer](#disclaimer)
- [Author](#author)

---

## 🧠 What This Project Does

Markets move through different regimes — such as bull markets, bear markets, crises, and consolidation phases — but these states are never explicitly labeled.

This system:

- Discovers these hidden regimes using unsupervised learning
- Predicts upcoming regimes using supervised learning
- Summarizes current market structure in plain English
- Forecasts the next year's regime behavior

All of this is done using live market data and a reproducible ML pipeline.

## 🚀 Core Features

- 📥 **Automatic financial data ingestion** - Fetches real-time data from Yahoo Finance
- 🧮 **Advanced feature engineering** - Extracts technical indicators from price & volume data
- 🧠 **Unsupervised regime detection** - Discovers hidden market states using K-Means clustering
- 🤖 **Supervised regime prediction** - Forecasts regime transitions using Random Forest
- 🧾 **Human-readable market summary** - Generates plain English interpretation of market structure
- 🔮 **One-year forward regime outlook** - Produces probabilistic regime forecast
- 📊 **Strategy performance comparison** - Compares regime-aware strategies to buy-and-hold
- 🖥️ **Works on any asset** - Stocks, crypto, indices, commodities

## 🧩 System Architecture

```
Market Data
    ↓
Feature Engineering
    ↓
Regime Detection (Unsupervised ML) - K-Means Clustering
    ↓
Regime Prediction (Supervised ML) - Random Forest
    ↓
Market Summary & One-Year Regime Forecast
    ↓
Strategy Performance Evaluation
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Steps

```bash
# Clone the repository
git clone https://github.com/manav363/market_regime_detection.git
cd market_regime_detection

# Create and activate virtual environment
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

## 📋 Requirements

The project depends on the following packages:

- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn
- **Financial Data**: yfinance
- **Visualization**: matplotlib, seaborn
- **Utilities**: joblib, scipy

See `requirements.txt` for specific versions.

## 📁 Project Structure

```
market_regime_detection/
├── main.py                 # Entry point - orchestrates the entire pipeline
├── data.py                 # Financial data fetching and preprocessing
├── features.py             # Feature engineering (technical indicators)
├── model.py                # ML model definitions and training
├── predictor.py            # Regime prediction logic
├── forecast.py             # One-year regime forecasting
├── visualize.py            # Plotting and visualization utilities
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── LICENSE                 # MIT License
```

### Key Modules

- **data.py**: Downloads historical market data using yfinance
- **features.py**: Computes technical indicators (RSI, MACD, Bollinger Bands, etc.)
- **model.py**: Trains K-Means for regime detection and Random Forest for predictions
- **predictor.py**: Makes regime predictions for future periods
- **forecast.py**: Generates one-year ahead probabilistic regime forecasts
- **visualize.py**: Creates regime plots and performance comparisons

## ▶️ How To Run

```bash
python main.py
```

When prompted, enter any ticker symbol:

```
Enter ticker (e.g., AAPL, SPY, BTC-USD, ^NSEI):
```

### Examples

- **US Stocks**: AAPL, GOOGL, MSFT, TSLA
- **Indices**: SPY (S&P 500), QQQ (Nasdaq), ^NSEI (Nifty 50)
- **Crypto**: BTC-USD, ETH-USD
- **Commodities**: GC=F (Gold), CL=F (Crude Oil)

### Execution Flow

The system will automatically:

1. Download market data (past 5 years)
2. Extract technical features
3. Detect hidden market regimes using K-Means
4. Train a Random Forest to predict regime transitions
5. Generate market interpretation in English
6. Plot regime behavior over time
7. Forecast the next year's regime evolution
8. Compare regime-aware strategy performance to buy-and-hold

## 📊 Example Outputs

The system generates:

- **Market regime visualization**: Charts showing different market regimes over time
- **Regime prediction accuracy**: Classification metrics for regime predictions
- **Plain-English market interpretation**: Summary of current market structure
- **One-year regime outlook**: Probabilistic forecast of future regimes
- **Strategy vs Buy-and-Hold comparison**: Performance metrics and charts

## 🧪 Machine Learning Models

| Component | Model | Purpose |
|-----------|-------|----------|
| Regime Detection | K-Means Clustering | Discovers hidden market states (unsupervised) |
| Regime Prediction | Random Forest Classifier | Predicts regime transitions (supervised) |

### Model Parameters

- **K-Means**: K=3 regimes (typically bull, bear, consolidation)
- **Random Forest**: 100 estimators, max_depth=10

## ⚠️ Disclaimer

This project is for educational and research purposes only. It is **not financial advice**. 

Do not use this system to make real investment decisions without proper due diligence and consultation with a financial advisor.

## 🧑‍💻 Author

**Manav Garg**  
Machine Learning & Quantitative Research

---

## 📚 Additional Resources

- [Technical Analysis Indicators](https://www.investopedia.com/)
- [K-Means Clustering](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)
- [Yahoo Finance API](https://pypi.org/project/yfinance/)

---

*Last Updated: January 2026*
