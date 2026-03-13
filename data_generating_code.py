import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

start = datetime(2022,1,1)
end = datetime(2024,12,31)
dates = pd.date_range(start, end)
## the above steps are to show the date range

first_names = ["Arjun", "Priya", "Rohit", "Neha", "Sumit", "Rina", "Anindyo", "Aparna", "Ashalata", "Kaushik"]
surnames = ["Banerjee","Bhattacharya","Das","Dutta","Ghosh","Chatterjee","Mitra","Roy","Sen","Bose"]
salespersons = [" ".join([random.choice(first_names), random.choice(surnames)]) for _ in range(20)]

categories = {
"Grocery": ["Rice","Dal","Oil","Sugar","Tea"],
"Electronics": ["TV","Mobile","Laptop","Camera","Headphones"],
"Clothing": ["Shirt","Trousers","Dress","Jacket","Shoes"],
"Home": ["Cookware Set","Cushion Cover","Mop","Lamp","Cutlery"],
"Personal Care": ["Shampoo","Soap","Toothpaste","Lotion","Perfume"]}
payment_methods = ["Cash","Card","Online"]
locations = ["Central Kolkata","South Kolkata","North Kolkata","East Kolkata"]

rows = []
txn_counter = 1
for date in dates:
    num_txn = 3
    for _ in range(num_txn):
        cat = random.choice(list(categories.keys()))
        prod = random.choice(categories[cat])
        qty = random.randint(1,10)
        price = int(np.round(random.uniform(30,50000) if cat=="Electronics" else random.uniform(30,2000)))
        sp = random.choice(salespersons)
        rows.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Transaction ID": f"TRN{date.strftime('%Y%m%d')}-{txn_counter:04d}",
            "Customer ID": f"CUST{random.randint(100000,999999)}",
            "Product Category": cat,
            "Product Name": prod,
            "Quantity": qty,
            "Unit Price": price,
            "Payment Method": random.choice(payment_methods),
            "Store Location": random.choice(locations),
            "Salesperson ID": f"SP{salespersons.index(sp)+1:03d}",
            "Salesperson Name": sp})
        txn_counter += 1
d = pd.DataFrame(rows)
d.to_csv("store_sales_2022_2024.csv", index=False)
d.to_excel("store_sales_2022_2024.xlsx", index=False)
print("Generated CSV and Excel files with", len(d), "rows.")
