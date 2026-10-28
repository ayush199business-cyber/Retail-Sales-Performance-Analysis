import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)
records = 1500

products = {
    'Pro Gaming Laptop': ('Electronics', 1299.99),
    'Noise Canceling Headphones': ('Electronics', 199.99),
    'Ergonomic Desk Chair': ('Home & Kitchen', 249.99),
    'Smart Coffee Maker': ('Home & Kitchen', 89.99),
    'Premium Running Shoes': ('Apparel', 120.00),
    'Leather Bomber Jacket': ('Apparel', 250.00),
    'Vitamin C Skincare Serum': ('Beauty & Health', 45.00),
    'Plant Protein Powder': ('Beauty & Health', 35.00)
}

prod_names = list(products.keys())

data = {
    'Transaction_ID': [f"TX-{10000 + i}" for i in range(records)],
    'Date': pd.date_range(start='2025-01-01', periods=records, freq='4h').strftime('%Y-%m-%d %H:%M:%S'),
    'Product_Name': np.random.choice(prod_names, size=records),
    'Quantity': np.random.randint(1, 5, size=records),
    'Unit_Price': [np.nan if np.random.rand() < 0.05 else 0.0 for _ in range(records)], # 5% missing prices
    'Store_Location': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'], size=records)
}

df_gen = pd.DataFrame(data)

# Map correct prices while keeping the missing rows empty
for idx, row in df_gen.iterrows():
    if not pd.isna(row['Unit_Price']):
        df_gen.at[idx, 'Unit_Price'] = products[row['Product_Name']][1]

# Map categories
df_gen['Category'] = df_gen['Product_Name'].map(lambda x: products[x][0])

# Inject duplicate records to simulate data noise
df_gen = pd.concat([df_gen, df_gen.sample(n=45)], ignore_index=True)

df_gen.to_csv('retail_sales_raw_data.csv', index=False)
print("SUCCESS: 'retail_sales_raw_data.csv' created with missing values and duplicates.")
