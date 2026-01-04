📊 Market Regime Detection & Forecasting

A complete end-to-end Machine Learning research system that detects hidden market regimes, predicts regime transitions, summarizes market behavior, and produces a one-year forward outlook using real financial data.

This project demonstrates practical ML engineering, quantitative finance concepts, and real-world system design.

🧠 What This Project Does

Markets move through different regimes — such as bull markets, bear markets, crises, and consolidation phases — but these states are never explicitly labeled.

This system:

Discovers these hidden regimes using unsupervised learning

Predicts upcoming regimes using supervised learning

Summarizes current market structure in plain English

Forecasts the next year's regime behavior

All of this is done using live market data and a reproducible ML pipeline.

🚀 Core Features

📥 Automatic financial data ingestion

🧮 Advanced feature engineering on price & volume

🧠 Unsupervised regime detection (K-Means)

🤖 Supervised regime transition prediction (Random Forest)

🧾 Human-readable market summary

🔮 One-year forward regime outlook

📊 Strategy performance comparison

🖥️ Works on any asset: stocks, crypto, indices, commodities

🧩 System Architecture
Market Data 
   → Feature Engineering 
   → Regime Detection (Unsupervised ML)
   → Regime Prediction (Supervised ML)
   → Market Summary
   → One-Year Regime Forecast

🛠️ Installation & Setup
git clone https://github.com/yourusername/market-regime-detection
cd market-regime-detection
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

▶️ How To Run
python main.py


When prompted, enter any ticker:

AAPL
SPY
BTC-USD
^NSEI


The system will:

Download market data

Detect market regimes

Train a regime predictor

Plot regime behavior

Print market summary

Forecast the next year

📊 Example Outputs

Market regime visualization

Regime prediction accuracy report

Plain-English market interpretation

One-year regime outlook

Strategy vs Buy-and-Hold comparison

🧪 Machine Learning Models Used
Component	Model
Regime Detection	K-Means Clustering
Regime Prediction	Random Forest Classifier
⚠️ Disclaimer

This project is for educational and research purposes only.
It is not financial advice.

🧑‍💻 Author

Manav Garg
Machine Learning & Quantitative Research