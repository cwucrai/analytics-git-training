import pandas as pd
import numpy as np
import os

# ---------------------------------------
# Example: Process sales data with pandas
# ---------------------------------------

# Generate a sample dataset
np.random.seed(42)  # for reproducible random numbers
data={
    "Product": np.random.choice(["A","B","C"], size=10),
    "Price": np.random.randint(10, 50, size=10),
    "Quantity":np.random.randint(1,10, size=10),
}
df = pd.DataFrame(data)

print("=== Original Data ===")
print(df)

# Add a calculated column: total sales per row
df["Total"] = df["Price"] * df["Quantity"]

print("\n=== Data with Total column ===")
print(df)

# Group by product and sum totals
grouped = df.groupby("Product", as_index=False).agg(
    Total_Sales=("Total", "sum"),
    Avg_Price=("Price", "mean"),
    Count=("Quantity", "sum"),
)

print("\n=== Grouped Summary ===")
print(grouped)

# Save to CSV
output_file = "sales_summary.csv"
grouped.to_csv(output_file, index=False)
print(f"\n✅ Summary data saved to {output_file}")
