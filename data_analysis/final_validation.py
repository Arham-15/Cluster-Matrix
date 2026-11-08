import pandas as pd

# Load original and final customer datasets
original_data = pd.read_csv("data/Ecommerce.csv")
customer_data = pd.read_csv(
    "outputs/results/customer_segments_final.csv"
)

# Check dataset dimensions
print("Original dataset shape:", original_data.shape)
print("Final customer dataset shape:", customer_data.shape)

# Check unique customers
print(
    "Unique customers in original data:",
    original_data["customer_id"].nunique()
)

print(
    "Customers in final dataset:",
    customer_data["customer_id"].nunique()
)

# Check duplicate customer records
print(
    "Duplicate customer IDs:",
    customer_data["customer_id"].duplicated().sum()
)

# Check missing values
print(
    "Missing values in final dataset:",
    customer_data.isnull().sum().sum()
)

# Check cluster distribution
print("\nCluster distribution:")
print(customer_data["Cluster"].value_counts().sort_index())

# Check total revenue
print(
    "\nTotal revenue:",
    round(customer_data["total_revenue"].sum(), 2)
)