

---
# Tariff Rate Prediction

## Overview

This project aims to predict transportation tariff rates based on various factors such as road type, distance, fuel cost, labor cost, and other related inputs. By leveraging machine learning techniques, the model forecasts the expected tariff, which can help logistics companies optimize their pricing strategies.

![App Screenshot](https://corlettexpress.com/storage/2023/07/Traffic-Managers-The-Key-Players-Behind-Efficient-Operations-and-Smooth-Workflows-scaled-2048x1024.jpeg)

### What is a Tariff?

A tariff, in this context, refers to the cost associated with the transportation of goods via roads. It typically includes multiple cost components like fuel, tolls, labor, and miscellaneous expenses. This project builds a predictive model to estimate the final tariff based on historical data and various influencing factors.

![App Screenshot](https://media.tenor.com/fE8klspLVBQAAAAM/gas-prices-petrol-station.gif)

## Project Structure

The project is structured into the following key steps:

1. **Data Preprocessing**:
   - **Data Cleaning**: Handling missing values in the dataset by either filling them with appropriate strategies or removing them.
   - **Feature Engineering**: Creating new features based on existing data to improve the model’s prediction power.
   - **Scaling**: Standardizing the features to ensure they are on a similar scale, which improves model performance.
   - **Handling Categorical Data**: Converting categorical variables (such as road type) into numerical values using encoding techniques.

2. **Model Development**:
   - **Training Data Split**: Splitting the data into training and testing sets to evaluate the model's performance.
   - **Model Selection**: Several machine learning models are tested, including:
     - **Linear Regression**
     - **Decision Trees**
     - **Random Forest**
     - **XGBoost**
   - **Hyperparameter Tuning**: Optimizing the model by fine-tuning hyperparameters to improve accuracy.

3. **Model Evaluation**:
   - **Metrics**: Models are evaluated using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess their prediction accuracy.
   - **Cross-validation**: To avoid overfitting, cross-validation techniques are employed, ensuring the model performs well on unseen data.

4. **Deployment**:
   - **HTML Form Interface**: The project includes a front-end form (`index.html`) where users can input their data to predict tariff rates.
   - **API (Flask)**: The `app.py` file is responsible for handling the form inputs and making predictions using the trained machine learning model.

   ![](https://miro.medium.com/v2/resize:fit:1400/1*SQ0gmwO8XV0b3KoTMWavEA.gif)

## Requirements

Below are the required dependencies along with their versions to replicate the project:

- Python 3.8+
- `pandas` (v2.2.2)
- `numpy` (v1.24.3)
- `scikit-learn` (v1.2.2)
- `flask` (v2.0.3)
- `ydata-profiling` (v4.11.0)

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Steps to Run the Project

1. Clone the repository:
   ```bash
   git clone <repository_link>
   ```

2. Navigate to the project directory:
   ```bash
   cd Tariff_Rate_Prediction
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Train the machine learning models:
   ```bash
   jupyter notebook Tariff_Rate_Prediction.ipynb
   ```

5. Run the Flask app to serve the prediction interface:
   ```bash
   python app.py
   ```

6. Access the web interface:
   Open your browser and navigate to `http://127.0.0.1:5000` to enter prediction data.

## Models Tested

- **Linear Regression** 
- **Decision Trees** 
- **Support Vector Machine**
- **Random Forest Regressor** 

## HTML Form (`index.html`)

The `index.html` file provides a user-friendly interface for entering the prediction data. It includes input fields for year, road type, seasonal impact, demand, weight, labor, toll, distance, fuel cost, and miscellaneous expenses. Once the user submits the form, the data is sent to the Flask app to generate a tariff prediction.

Key features of the form:
- **Field validation** ensures that no required field is left empty.
- **Responsive Design** using basic CSS ensures the form looks good on all devices.

You can find the key implementation details of the form in the [index.html file](21).

## Flask Application (`app.py`)

The `app.py` file serves as the back-end API. It processes the form inputs from the HTML file and uses the trained machine learning model to predict tariff rates. The key functionalities include:
- Handling POST requests from the form.
- Loading the machine learning model.
- Sending the predicted result back to the user interface.

---

