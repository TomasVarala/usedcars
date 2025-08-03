import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os

# Load dataset (make sure vehicles.csv is in the same directory or provide the full path)
df = pd.read_csv("C:/Code/Projektit/downloads/archive/vehicles.csv")

# 1. Drop columns with more than 50% missing values
threshold = len(df) * 0.5
df = df.dropna(thresh=threshold, axis=1)

# 2. Drop rows missing essential fields
df = df.dropna(subset=['price', 'year', 'odometer', 'manufacturer'])

# 3. Fill missing categorical values
fill_values = {
    'condition': 'unknown',
    'fuel': 'unknown',
    'title_status': 'unknown'
}
df.fillna(fill_values, inplace=True)

# 4. Handle outliers
df = df[(df['price'] > 500) & (df['price'] < 100000)]
df = df[(df['odometer'] > 0) & (df['odometer'] < 300000)]

# 5. Drop unnecessary features
columns_to_drop = ['id', 'url', 'image_url', 'description', 'lat', 'long']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# 6. Add new features
df['car_age'] = 2025 - df['year']

# 7. Format categorical features
categorical_cols = [
    'manufacturer', 'condition', 'fuel', 'title_status',
    'transmission', 'drive', 'size', 'type', 'paint_color', 'state'
]
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype('category')

# 8. Scale numerical features
scaler = MinMaxScaler()
df['odometer_scaled'] = scaler.fit_transform(df[['odometer']])
df['car_age_scaled'] = scaler.fit_transform(df[['car_age']])

# 9. Create classification variable
median_price = df['price'].median()
df['price_category'] = df['price'].apply(lambda x: 'cheap' if x < median_price else 'expensive')

# 10. Save cleaned data
output_path = "C:/Code/Projektit/downloads/vehicles_cleaned.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Cleaned dataset saved to: {output_path}")
