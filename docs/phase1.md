# Phase 1: Business Understanding – Craigslist Cars & Trucks Price Analysis App

## 1. Business Objectives

The imaginary customer is a used car dealership chain that wants to expand its operations across the U.S. They need better market insights to:

- Understand price trends and value depreciation across different makes, models, and locations.
- Optimize pricing strategies to stay competitive on platforms like Craigslist.
- Identify underpriced vehicles to source for resale.
- Understand regional differences in car values and inventory.

Main Business Goal: Leverage data from Craigslist to build a tool that provides price analytics and predictions to support vehicle purchasing, pricing, and inventory planning decisions.

## 2. Analyze the Current Situation

- The dealership currently prices vehicles based on gut feeling, limited local trends, and manual browsing of online listings.
- They lack a data-driven decision tool.
- The dealership has access to vehicle stock and historical sale prices, but they want a tool that uses external market data (like Craigslist) to improve decision-making.

Pain Points:

- Inefficient pricing
- Missed opportunities to buy undervalued cars
- Inability to track market trends in real time

## 3. Define Initial Goals of Data Analysis and Modelling

The initial phase of data analysis should answer:

- What are typical price ranges for vehicles by make, model, year, and condition?
- How does location affect pricing?
- What features (mileage, year, condition, location) are most important in predicting a vehicle’s price?
- Can we build a predictive model that estimates fair market value for a given vehicle?

Technical Goals:

- Clean and preprocess the data
- Conduct exploratory data analysis (EDA)
- Train and validate regression models for price prediction
- Build an app (dashboard/API) to serve pricing insights

## 4. Define the Project’s Goals

Create an app that allows users (the dealership) to:

- Input a vehicle’s details and get a predicted fair market price
- Explore trends across vehicle categories and regions
- Identify undervalued listings for potential purchase

Deliver documentation and visualizations to support business use

Key Deliverables:

- Predictive pricing model (e.g., linear regression, random forest)
- Data dashboard or web app for insights
- Technical documentation and user guide

## 5. Key Business Questions

- What is a fair market price for a specific used car?
- Are there pricing patterns that vary by region or time?
- Which listings offer the best value (i.e., price significantly below estimated value)?
- How do mileage, condition, and make/model influence pricing?

## 6. Measurable Results

Success will be measured by:

- Model accuracy (e.g., MAE or RMSE on validation data) 
- User feedback from dealership (imaginary) stakeholders
- Efficiency gains in sourcing/purchasing (estimated)
- Comparison between predicted prices and actual Craigslist listings

## 7. Target Audience / Beneficiaries

Primary customer: Used car dealership chain decision-makers

Other beneficiaries:

- Car buyers looking for fair prices
- Internal data analysts
- Marketing & procurement teams

## 8. Technologies

- Data analysis: Python (Pandas, NumPy)
- Modeling: Scikit-learn, XGBoost, or LightGBM
- Dashboard/app: Streamlit or Flask
- Visualization: Plotly, Matplotlib, or Seaborn
- Data storage: CSV, possibly SQLite or a simple backend DB

