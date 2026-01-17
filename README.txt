# 💳 Credit Card Fraud Detection System

An AI-powered fraud detection system that identifies suspicious credit card transactions using machine learning.  
Supports both **manual transaction scanning** and **bulk CSV fraud analysis** with downloadable reports.

---

✨ Features

- 🔍 Real-time fraud prediction (manual mode)
- 📁 Bulk CSV fraud scanning
- 📊 Fraud probability & risk level scoring
- 📥 Downloadable fraud reports (CSV)
- 🧠 Trained Random Forest ML model
- ⚡ Fast & interactive Streamlit UI
- 🔐 Privacy-preserving PCA features

---

🧠 Tech Stack

| Component | Technology |
|---------|-------------|
| Language | Python |
| UI | Streamlit |
| ML Model | Random Forest |
| Data Processing | Pandas, NumPy |
| Scaling | StandardScaler |
| Model Storage | Joblib |
| Dataset | ULB Credit Card Fraud Dataset |

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 99.9% |
| ROC-AUC | 0.92 |
| Precision (Fraud) | 0.89 |
| Recall (Fraud) | 0.75 |
| F1 Score | 0.81 |

---

🏗 System Architecture
Fraud Detection System
│
├── Manual Fraud Scanner (Real-time Prediction)
│   ├ Input transaction details
│   ├ Predict fraud probability
│   ├ Risk classification
│   └ Result dashboard
│
└── CSV Fraud Scanner (Batch Processing)
    ├ Upload transaction CSV
    ├ Scan all transactions
    ├ Generate fraud probability
    └ Download fraud report

📂 Project Structure
fraud-detection-system/
│
├── app.py                    # Streamlit web application
├── fraud_model.pkl          # Trained Random Forest model
├── scaler.pkl               # Trained StandardScaler
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
│
├── notebook/
│   └── model_training.ipynb # Model training notebook
│
├── sample_data/
│   └── test_transactions.csv
│
└── screenshots/
    ├── manual_page.png
    └── csv_page.png



📦 Dataset

Dataset used: ULB Credit Card Fraud Dataset

284,807 transactions

492 fraud cases

PCA anonymized features (V1–V28)

Time & Amount columns

Highly imbalanced dataset

Source: Kaggle / ULB Machine Learning Group

💻 Usage Examples
Manual Scanner

Enter transaction values

Click Predict Fraud Risk

Get fraud probability and risk level

CSV Scanner

Upload CSV file

Click Scan Transactions

Download fraud report

📈 How It Works

User enters transaction or uploads CSV

Input is validated and scaled

Random Forest model predicts fraud probability

Risk level is calculated

Results are displayed & downloadable


🎯 Use Cases

Banking transaction monitoring

Payment gateway fraud detection

Financial compliance audits

Risk analytics platforms

Fraud research & training


🔮 Future Improvements

PDF report export

Cloud deployment

Batch API service

Model explainability (SHAP)

Transaction history dashboard

User authentication


🐛 Troubleshooting


| Issue             | Solution             |
| ----------------- | -------------------- |
| Model not loading | Check file path      |
| Wrong predictions | Ensure feature order |
| Scaling error     | Verify scaler.pkl    |
| CSV error         | Check column names   |



👨‍💻 Author

Muhammed Hijas


⭐ If you like this project

Give it a star on GitHub ⭐

