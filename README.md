# DE_Project
## Gold Price Prediction Using Machine Learning
### Links:
-**Project Website**: https://goldpricepredictiondeproject.netlify.app/

-**DockerHub Repository**: https://hub.docker.com/repository/docker/arjunbhattad/gold-price-prediction/general
### Overview

The **Gold Price Prediction** project focuses on forecasting gold prices using machine learning techniques by leveraging two different datasets: one sourced from Kaggle and another from financial datasets, such as the SPDR Gold Trust (GLD) Exchange Traded Fund. This integrated approach combines strengths from both projects to build a robust model capable of predicting future gold prices based on various economic and market indicators.

Gold plays a significant role in the global financial system. Predicting its prices can assist investors and traders in making informed decisions. The project incorporates advanced machine learning techniques, feature engineering, and ensemble modeling to achieve high accuracy in price prediction.

---

### Key Features

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

### Workflow

1. Data Collection and Integration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training and Optimization
6. Ensemble Modeling
7. Model Evaluation
8. Prediction and Deployment

---

### Installation

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

### How to Run

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

3. **Docker Setup**:
   - You can also run the project in a Docker container for a consistent environment. Follow the steps below to set up Docker for the Gold Price Prediction project.
   - [Dockerhub Repository](https://hub.docker.com/repository/docker/arjunbhattad/gold-price-prediction/general)

---

### Docker Image Implementation

To run this project in a Docker container, follow these steps:

#### Step 1: Build the Docker Image
1. Make sure your project directory contains a `Dockerfile` (as described in the previous instructions).
2. Open a terminal and navigate to the project directory.
3. Build the Docker image using the following command:
   ```bash
   docker build -t gold-price-prediction .
   ```

#### Step 2: Run the Docker Container
Once the image is built, you can run the container with the following command:
```bash
docker run -p 8888:8888 gold-price-prediction
```
- `-p 8888:8888`: This maps port `8888` on your host machine to port `8888` inside the Docker container, which is the default port for Jupyter Lab.
- This will start the container and launch **Jupyter Lab**.

#### Step 3: Access the Jupyter Notebook
Once the container is running, you can access the Jupyter Lab interface from your browser by visiting:
```bash
http://localhost:8888
```
You may need to enter the **token** provided in the terminal output to log in.

---

### Importing the Docker Image from DockerHub

If you want to import the pre-built Docker image from DockerHub (instead of building it yourself), follow these steps:

#### Step 1: Pull the Docker Image from DockerHub
Open a terminal and run the following command to pull the Docker image from DockerHub (replace `username` with the actual DockerHub username where the image is hosted):
```bash
docker pull arjunbhattad/gold-price-prediction:latest
```
This will download the pre-built Docker image to your local machine.

#### Step 2: Run the Docker Container
After pulling the image, you can run the Docker container with the following command:
```bash
docker run -p 8888:8888 arjunbhattad/gold-price-prediction:latest
```
- `-p 8888:8888`: This maps port `8888` on your host machine to port `8888` inside the Docker container, where Jupyter Lab will be accessible.

#### Step 3: Access the Jupyter Notebook
Once the container is running, open your browser and go to:
```bash
http://localhost:8888
```
You can then use Jupyter Lab to interact with the project.

---

### Dataset and Inputs

- **Kaggle Dataset**: Provides historical gold price data and economic indicators.
- **Final_USO Dataset**:
  - Covers 1,718 rows and 80 columns, including features like oil prices, S&P 500 index, bond rates, exchange rates, and precious metal prices.
  - **Target Variable**: Adjusted Close Price of the GLD ETF, which accounts for dividends, stock splits, and offerings.

---

### Evaluation Metrics

- **Root Mean Square Error (RMSE)**: Measures the standard deviation of residuals (prediction errors).
- **R² Score**: Indicates the proportion of variance explained by the model.

---

### Conclusion

The integrated project offers a comprehensive framework for predicting gold prices using machine learning. By combining insights from Kaggle and Final_USO datasets, this project leverages a wide range of features, advanced algorithms, and ensemble modeling to enhance prediction accuracy.

---

### Acknowledgments

This project utilizes open-source tools and datasets. Special thanks to:
- Kaggle and Yahoo Finance for datasets.
- Developers of Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn.
