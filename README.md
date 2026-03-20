# 🚛 Tariff Rate Prediction

> **Machine Learning–Powered Transportation Cost Forecasting**
> Predict road-freight tariff rates from shipment parameters using ensemble ML — deployed via a Flask REST API with an interactive web interface.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-2.0.3-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-1.2.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/pandas-2.2.2-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Business Context](#-business-context)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [ML Pipeline](#-ml-pipeline)
- [Deployment Architecture](#-deployment-architecture)
- [Installation and Setup](#-installation-and-setup)
- [Usage](#-usage)
- [Dependencies](#-dependencies)
- [Results](#-results)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

Transportation tariff rates are influenced by a complex web of variables: fuel prices, tolls, cargo weight, route distance, labour rates, seasonal demand, and road classification. Manual pricing is slow, inconsistent, and prone to margin erosion.

This project builds a **supervised regression pipeline** that ingests historical shipment records and learns to predict the final tariff with high accuracy. The trained model is surfaced through a **Flask REST API** and an **HTML web form**, enabling non-technical users to obtain instant price estimates without touching a single line of code.

**Key Highlights**

- Automated EDA using ydata-profiling for rapid dataset insight
- 4 ML algorithms benchmarked with cross-validated evaluation
- Hyperparameter tuning via GridSearchCV
- Live web interface — browser-based form for instant predictions
- Reproducible — pinned dependency versions and fixed random seeds

---

## 💼 Business Context

Logistics companies face a persistent pricing challenge: tariff quotes must be generated quickly yet remain accurate enough to preserve margins. Under-quoting erodes profitability; over-quoting loses business to competitors.

The Tariff Rate Prediction system addresses this by modelling the relationship between shipment attributes and final cost — producing data-driven estimates that can be embedded in quoting tools, ERP systems, or customer-facing portals.

**Target Users**

- Pricing analysts at logistics and freight-forwarding firms
- Operations managers needing rapid cost estimates for route planning
- Data science teams extending the model with new data sources
- Developers integrating tariff estimation into larger supply-chain platforms

---

## 📁 Project Structure

    Tariff_Rate_Prediction/
    │
    ├── notebook/
    │   └── tariff_model.ipynb          # ML pipeline & training
    │
    ├── data/
    │   └── tariff_data.csv             # Dataset
    │
    ├── flaskEndpoint/
    │   ├── app.py                      # Flask API
    │   └── templates/
    │       └── index.html              # Web UI
    │
    ├── models/
    │   ├── model.pkl                   # Trained model
    │   └── scaler.pkl                  # Scaler
    │
    ├── requirements.txt
    └── README.md

---

## 📊 Dataset

The dataset contains historical road-freight shipment records. Each row represents a single shipment transaction with its associated cost components and the final billed tariff as the regression target.

### Feature Catalogue

| Feature | Type | Description |
|---|---|---|
| Year | Numerical | Calendar year of shipment |
| Road Type | Categorical | Highway / National / State / Rural |
| Seasonal Impact | Numerical | Demand index for seasonal pricing effects |
| Demand | Numerical | Relative demand level at time of shipment |
| Weight (kg) | Numerical | Gross cargo weight in kilograms |
| Labor Cost | Numerical | Labour cost component for the shipment |
| Toll | Numerical | Applicable toll charges for the route |
| Distance (km) | Numerical | Total route distance in kilometres |
| Fuel Cost | Numerical | Fuel expenditure for the shipment leg |
| Miscellaneous | Numerical | Additional surcharges not in other fields |
| Tariff Rate | Target | Final billed tariff — the regression target |

---

## 🤖 ML Pipeline

### 1. Exploratory Data Analysis

Automated HTML profiling report generated using ydata-profiling, covering variable distributions, missing-value patterns, correlation heatmaps, and outlier summaries.

### 2. Data Preprocessing

| Step | Method |
|---|---|
| Missing Values | Numeric: median fill / Categorical: mode fill |
| Categorical Encoding | Label encoding for Road Type |
| Feature Scaling | StandardScaler on all continuous features |
| Train / Test Split | 80/20 with fixed random_state |

### 3. Models Benchmarked

| Algorithm | Key Strength | Parameters Tuned |
|---|---|---|
| Linear Regression | Interpretable baseline | None |
| Decision Tree Regressor | Non-linear interactions | max_depth, min_samples_split |
| Random Forest Regressor | Ensemble, robust to outliers | n_estimators, max_features, max_depth |
| Support Vector Machine | High-dimensional space | C, epsilon, kernel |

### 4. Hyperparameter Optimisation

GridSearchCV with 5-fold cross-validation, scoring on negative MAE.

### 5. Evaluation Metrics

| Metric | Purpose |
|---|---|
| MAE | Average prediction error in currency units |
| RMSE | Penalises large errors, detects systematic mispredictions |
| R² Score | Proportion of variance explained |
| CV Score | 5-fold cross-validated MAE to confirm generalisation |

---

## 🌐 Deployment Architecture

    [ Browser Form (index.html) ]
             |
             |  POST /predict
             v
    [ Flask API (app.py) ]
       |-- Parse and validate inputs
       |-- Apply StandardScaler transform
       |-- Load serialised model
       |-- Return predicted tariff
             |
             v
    [ Prediction displayed in browser ]

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip
- Git
- Jupyter Notebook (for retraining)

### Step 1 — Clone the Repository

    git clone https://github.com/Nikhil06032004/Tariff_Rate_Prediction.git
    cd Tariff_Rate_Prediction

### Step 2 — Create a Virtual Environment

    python -m venv venv
    source venv/bin/activate

On Windows:

    venv\Scripts\activate

### Step 3 — Install Dependencies

    pip install -r requirements.txt

### Step 4 — Train the Model

    jupyter notebook

Open the notebook and run all cells. This trains the model and saves it to disk.

### Step 5 — Start the Flask API

    cd flaskEndpoint
    python app.py

### Step 6 — Open the Web Interface

    http://127.0.0.1:5000

---

## 🚀 Usage

### Via Web Browser

Navigate to http://127.0.0.1:5000, fill in the shipment parameters, and click Predict Tariff.

### Via cURL

    curl -X POST http://127.0.0.1:5000/predict \
      -d "year=2024&road_type=1&seasonal_impact=1.2&demand=0.8" \
      -d "weight=12000&labor=1500&toll=400&distance=450" \
      -d "fuel_cost=3200&miscellaneous=200"

### Via Python

    import pickle
    import numpy as np

    model = pickle.load(open("models/model.pkl", "rb"))
    scaler = pickle.load(open("models/scaler.pkl", "rb"))

    features = np.array([[2024, 1, 1.2, 0.8, 12000, 1500, 400, 450, 3200, 200]])
    prediction = model.predict(scaler.transform(features))
    print(f"Predicted Tariff: {prediction[0]:,.2f}")

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| pandas | 2.2.2 | Data loading and feature engineering |
| numpy | 1.24.3 | Numerical array operations |
| scikit-learn | 1.2.2 | ML algorithms, preprocessing, metrics |
| flask | 2.0.3 | Web framework for the prediction API |
| ydata-profiling | 4.11.0 | Automated EDA report generation |

    pip install -r requirements.txt

---

## 📈 Results

| Model | Performance |
|---|---|
| Linear Regression | Baseline — limited on non-linear data |
| Decision Tree | Good fit but prone to overfitting |
| Random Forest | Best performer — lowest MAE and RMSE |
| SVR | Competitive but slower to train |

Exact metric values (MAE, RMSE, R²) are available in the notebook output cells after running the full pipeline.

---

## 🗺️ Roadmap

- [ ] Dockerise the application for one-command deployment
- [ ] Add MLflow experiment tracking and model registry
- [ ] Benchmark XGBoost and LightGBM
- [ ] Integrate SHAP feature importance in the web UI
- [ ] Build a JSON REST API alongside the HTML form
- [ ] Add pytest unit tests and GitHub Actions CI/CD

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request with a clear description

Please ensure all notebook cells run without errors before submitting.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

**Nikhil** — [@Nikhil06032004](https://github.com/Nikhil06032004)

For bug reports or feature requests, please [open an issue](https://github.com/Nikhil06032004/Tariff_Rate_Prediction/issues).

---

<p align="center">Built with love for the logistics and data science community</p>
