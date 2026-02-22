#  Superstore Sales Analysis, Forecasting & Automation Pipeline

##  Project Overview

This project automates end-to-end business analysis of a retail Superstore dataset.  
It transforms raw transactional data into actionable business insights and short-term sales forecasts using a fully runnable Python automation script.

The entire workflow runs using a single command:

```bash
python main.py
```

All cleaned data, analysis outputs, and forecast results are automatically saved into the `/output` folder.

This project simulates a real-world business analytics pipeline used in production environments.

---

#  Business Objectives

The primary objectives of this project are:

- Automate data cleaning and preprocessing
- Analyze sales performance trends over time
- Identify loss-making product categories
- Evaluate regional and customer segment profitability
- Analyze discount impact on profit margins
- Generate short-term sales forecasts using Machine Learning
- Convert notebook-based analysis into a production-style runnable script

---

#  Dataset Description

Dataset: **Sample - Superstore**

The dataset contains retail transactional data including:

- Order Date
- Ship Date
- Sales
- Profit
- Discount
- Category
- Sub-Category
- Region
- Customer Segment

It represents a multi-category retail business operating across different geographic regions.

---

#  Data Cleaning & Feature Engineering

The automation pipeline performs:

- Removal of duplicate records
- Conversion of date columns to datetime format
- Creation of Profit Margin (%)
- Monthly aggregation for time-series analysis
- Structured grouping for category, region, and segment evaluation

All preprocessing logic is modularized inside `analysis.py`.

---

#  Business Analysis & Key Insights

##  1. Sales Performance Over Time

- Overall upward growth trend observed
- High month-to-month volatility
- Seasonal spikes likely during year-end periods
- Business shows growth but lacks stability

---

##  2. Loss-Making Sub-Category

- **Tables** generates high revenue but negative profit
- Indicates structural pricing or cost inefficiencies
- Scaling this category without correction may increase losses

---

##  3. Regional Performance

- **West Region**: Highest sales and profitability
- **East Region**: Strong performance
- **Central Region**: Lower profitability efficiency
- **South Region**: Lowest sales contribution

---

##  4. Customer Segment Analysis

- Consumer segment contributes highest overall profit
- Corporate segment performs moderately
- Home Office segment shows lowest contribution

---

##  5. Discount Impact on Profit

- Discounts up to 20% → Generally profitable
- Around 30% → Profitability declines
- 40–80% → Strong negative impact

Conclusion: Aggressive discounting erodes profit margins significantly.

---

#  Machine Learning – Sales Forecasting

## Model Used: Linear Regression

### Approach:

1. Aggregate monthly sales
2. Create Time_Index variable
3. Train Linear Regression model
4. Forecast next 3 months sales

### Forecast Summary:

- Predicted steady upward growth
- Expected range: ~$69K – $72K monthly
- Captures trend but does not account for seasonality

### Potential Improvements:

- ARIMA for time-series modeling
- Prophet for seasonality-aware forecasting
- Model evaluation using MAE / RMSE

---

#  Automation Architecture

The project follows a production-ready structure:

```bash
superstore_project/
│
├── data/
│   └── Sample - Superstore.csv
│
├── output/
│
├── analysis.py
├── model.py
├── main.py
└── requirements.txt
```

---

##  main.py

Controls the entire workflow:

- Load raw data
- Clean data
- Perform business analysis
- Run forecasting
- Save outputs automatically

---

##  analysis.py

Contains:

- clean_data()
- sales_over_time()
- category_analysis()
- region_analysis()
- segment_analysis()

---

##  model.py

Contains:

- forecast_linear()

---

#  Output Files Generated

After running:

```bash
python main.py
```

The following files are automatically generated:

- cleaned_data.csv
- monthly_sales.csv
- category_summary.csv
- region_summary.csv
- segment_summary.csv
- forecast.csv

---

#  How To Run This Project

### 1️ Clone Repository

```bash
git clone <your-repo-link>
cd superstore_project
```

### 2️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️ Run the Automation Pipeline

```bash
python main.py
```

### 4️ Check Results

All outputs will be available inside the `/output` folder.

---

#  Business Recommendations

1. Reassess pricing strategy for Tables sub-category.
2. Restrict discount levels beyond 30%.
3. Increase investment in West region.
4. Improve operational efficiency in Central region.
5. Strengthen Consumer segment retention strategies.

---

#  Risks Identified

- Margin erosion due to excessive discounting
- Overdependence on seasonal demand
- Structural losses in specific product categories
- Forecast model excludes seasonality and external factors

---

#  Key Technical Learnings

- Converting Jupyter Notebook analysis into automation script
- Modular Python architecture
- Business-focused storytelling
- Regression-based forecasting
- Production-style folder structuring

---

#  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn


# 📎 License

This project is developed for academic and portfolio purposes.
