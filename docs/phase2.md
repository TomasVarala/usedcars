# Phase 2: Data Understanding – Craigslist Cars & Trucks Dataset

## 1. All Available Data Collected

You’re using the dataset from Kaggle: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data 

This dataset includes listings scraped from Craigslist, with various attributes about used cars and trucks across different U.S. cities.

## 2. Content of the Data

Typical columns (based on dataset documentation and samples) include:

| Column Name    | Description                                     |
| -------------- | ----------------------------------------------- |
| `id`           | Unique listing ID                               |
| `url`          | Link to the listing                             |
| `region`       | Craigslist region (city)                        |
| `price`        | Listing price in USD                            |
| `year`         | Model year of the vehicle                       |
| `manufacturer` | Car brand (e.g., Toyota, Ford)                  |
| `model`        | Model name (e.g., Corolla, F-150)               |
| `condition`    | Vehicle condition (e.g., excellent, good, fair) |
| `cylinders`    | Number of cylinders (e.g., 4 cylinders)         |
| `fuel`         | Fuel type (e.g., gas, diesel, electric)         |
| `odometer`     | Mileage in miles                                |
| `title_status` | Title status (clean, salvage, rebuilt, etc.)    |
| `transmission` | Automatic, manual, or other                     |
| `drive`        | FWD, RWD, 4WD                                   |
| `size`         | Vehicle size (compact, full-size, etc.)         |
| `type`         | Body type (SUV, pickup, sedan, etc.)            |
| `paint_color`  | Exterior color                                  |
| `state`        | U.S. state                                      |
| `lat`, `long`  | Geographic coordinates                          |
| `posting_date` | When the listing was posted                     |

## 3. Initial Data Exploration

Some early EDA steps:

a. Basic Statistics

- Summary stats of numeric columns (e.g., price, odometer, year)
- Unique values in categorical columns (e.g., fuel, condition, manufacturer)
- Date range of postings

b. Sample Observations

Check a few rows manually to verify:
- Are there duplicates?
- Are prices realistic?
- Are years within a sensible range (e.g., no cars from 1900)?

## 4. Data Quality Check

| Check                     | Potential Issues                                                    |
| ------------------------- | ------------------------------------------------------------------- |
| **Missing Values**        | Some fields like `model`, `condition`, `drive` may be missing       |
| **Outliers**              | Unusually high/low prices or mileage (e.g., \$1 or 1,000,000 miles) |
| **Inconsistent Formats**  | Year or cylinders in text form, different spellings                 |
| **Duplicates**            | Listings reposted multiple times                                    |
| **Incorrect Geolocation** | Mismatched lat/long values or blank states                          |

You’ll want to create a data cleaning notebook to log all transformations and decisions.

## 5. Data Formats Used

- Dataset format: CSV
- All columns are structured and tabular
- price, odometer, year – numeric
- region, model, condition, etc. – categorical
- posting_date – date format, can be parsed to datetime

## 6. Visualization Tools & Techniques

Use the following libraries in Python:

| Tool                            | Use Case                                                     |
| ------------------------------- | ------------------------------------------------------------ |
| **Matplotlib / Seaborn**        | General plotting (histograms, boxplots, scatterplots)        |
| **Plotly**                      | Interactive visualizations (geographical maps, price trends) |
| **Pandas groupby + bar charts** | Group-level summaries                                        |
| **Heatmaps**                    | Correlation matrix (e.g., odometer vs. price)                |
| **Geo maps**                    | Price distribution by region/state                           |

Sample Visualization Ideas:

- Histogram of prices
- Price vs. mileage scatterplot
- Average price per region
- Boxplot of price by car condition
- Year vs. price trendline
- Heatmap of price correlation with year, odometer

