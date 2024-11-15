# DE_Project
# Gold Price Prediction Using Machine Learning

## Overview

The **Gold Price Prediction** project focuses on forecasting gold prices using machine learning techniques by leveraging two different datasets: one sourced from Kaggle and another from financial datasets, such as the SPDR Gold Trust (GLD) Exchange Traded Fund. This integrated approach combines strengths from both projects to build a robust model capable of predicting future gold prices based on various economic and market indicators.

Gold plays a significant role in the global financial system. Predicting its prices can assist investors and traders in making informed decisions. The project incorporates advanced machine learning techniques, feature engineering, and ensemble modeling to achieve high accuracy in price prediction.

---

## Key Features

1. **Comprehensive Data Integration**:
   - **Kaggle Dataset**: Includes historical gold prices, economic indicators, and market sentiment.
   - **Final_USO Dataset**: Contains diverse features such as oil prices, stock indices, bond rates, and currency exchange rates from November 18, 2004, to January 1, 2019.

2. **Data Preprocessing**:
   - Cleaning and transforming raw datasets.
   - Handling missing values and outliers.
   - Merging and aligning datasets for compatibility.

3. **Feature Engineering**:
   - Identifying key attributes influencing gold prices, such as adjusted close prices, economic indices, and precious metal trends.
   - Exploring correlations using visualization tools like Matplotlib and Seaborn.

4. **Data Visualization**:
   - Time series plots to observe trends and seasonality.
   - Heatmaps to identify relationships between features.
   - Distribution plots to understand data variability.

5. **Machine Learning Modeling**:
   - Implementing Random Forest Regressor and other regression algorithms for predictive modeling.
   - Combining the top three performing models using ensemble techniques.

6. **Evaluation and Metrics**:
   - Models evaluated using RMSE (Root Mean Square Error) and R² scores.
   - Visual comparisons between predicted and actual prices using line plots.

7. **Ensemble Modeling**:
   - Integrating multiple models to improve accuracy and reduce prediction errors.

---

## Workflow

1. Data Collection and Integration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training and Optimization
6. Ensemble Modeling
7. Model Evaluation
8. Prediction and Deployment

---

## Installation

To run this project, you will need:

- **Python 3.x**
- Python Libraries:
  - [NumPy](http://www.numpy.org/)
  - [Pandas](http://pandas.pydata.org/)
  - [Matplotlib](https://matplotlib.org/)
  - [Seaborn](https://seaborn.pydata.org/)
  - [Scikit-learn](https://scikit-learn.org/stable/)

**Recommended**: Install [Anaconda](https://www.anaconda.com/), a pre-packaged Python distribution that includes all the required libraries and tools.

---

## How to Run

1. **Google Colab**:
   - Open the notebook file `Gold_Price_Prediction.ipynb` in [Google Colab](https://colab.research.google.com/).
   - Run the cells sequentially.

2. **Local Setup**:
   - Clone the project repository:
     ```
     git clone https://github.com/ArjunBhattad2004/Gold_Price_Prediction
     ```
   - Navigate to the project directory and run:
     ```
     jupyter notebook Gold_Price_Prediction.ipynb
     ```

---

## Dataset and Inputs

- **Kaggle Dataset**: Provides historical gold price data and economic indicators.
- **Final_USO Dataset**:
  - Covers 1,718 rows and 80 columns, including features like oil prices, S&P 500 index, bond rates, exchange rates, and precious metal prices.
  - Target Variable: **Adjusted Close Price** of the GLD ETF, which accounts for dividends, stock splits, and offerings.

---

## Evaluation Metrics

- **Root Mean Square Error (RMSE)**: Measures the standard deviation of residuals (prediction errors).
- **R² Score**: Indicates the proportion of variance explained by the model.

---

## Conclusion

The integrated project offers a comprehensive framework for predicting gold prices using machine learning. By combining insights from Kaggle and Final_USO datasets, this project leverages a wide range of features, advanced algorithms, and ensemble modeling to enhance prediction accuracy.

---

## Acknowledgments

This project utilizes open-source tools and datasets. Special thanks to:
- Kaggle and Yahoo Finance for datasets.
- Developers of Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn.
