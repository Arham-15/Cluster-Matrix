import pandas as pd
import joblib
import sys
import os

# Add the main project folder to Python's module search path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from src.data_processing import load_customer_data

# 1. Load the saved model and scaler
model = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# 2. Load customer-level data
customer_data = load_customer_data()

# 3. Select the same features used during training
selected_features = [
    "total_sessions",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions"
]

# 4. Scale the customer data
scaled_data = scaler.transform(
    customer_data[selected_features]
)

# 5. Predict customer clusters
predicted_clusters = model.predict(scaled_data)

# 6. Load the saved segmentation results
final_data = pd.read_csv(
    "outputs/results/customer_segments_final.csv"
)

# 7. Compare predicted and saved cluster assignments
matches = (
    predicted_clusters == final_data["Cluster"].values
)

print("Model type:", type(model).__name__)
print("Number of clusters:", model.n_clusters)
print("Number of customers tested:", len(predicted_clusters))
print("Matching cluster assignments:", matches.sum())
print("Mismatched assignments:", (~matches).sum())

print(
    "\nAll assignments match:",
    matches.all()
)