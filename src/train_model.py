# 1. IMPORT REQUIRED LIBRARIES

import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# 2. LOAD ORIGINAL DATASET

data = pd.read_csv("data/Ecommerce.csv")

print("DATASET LOADED SUCCESSFULLY")
print("Original Dataset Shape:", data.shape)


# 3. CREATE CUSTOMER-LEVEL DATASET

customer_data = data.groupby("customer_id").agg({
    "session_id": "count",
    "purchased": "sum",
    "revenue": "sum",
    "pages_viewed": "mean",
    "time_on_site_sec": "mean",
    "added_to_cart": "sum",
    "cart_abandoned": "sum"
})


# 4. RENAME AGGREGATED COLUMNS

customer_data.columns = [
    "total_sessions",
    "total_purchases",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions",
    "total_cart_abandonments"
]


# 5. DISPLAY CUSTOMER DATASET

print("\nCUSTOMER-LEVEL DATA CREATED")

print(customer_data.head())

print("\nCUSTOMER DATASET SIZE:")
print(customer_data.shape)


# 6. SELECT FEATURES FOR CLUSTERING

selected_features = [
    "total_sessions",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions"
]

customer_features = customer_data[selected_features]


# 7. DISPLAY SELECTED FEATURES

print("\nSELECTED CUSTOMER FEATURES:")
print(customer_features.head())

print("\nSELECTED FEATURES DATASET SIZE:")
print(customer_features.shape)


# 8. FEATURE SCALING

scaler = StandardScaler()

scaled_features = scaler.fit_transform(customer_features)


# 9. DISPLAY SCALED DATASET

print("\nFEATURE SCALING COMPLETED")

print("\nSCALED DATASET SIZE:")
print(scaled_features.shape)


# 10. TRAIN K-MEANS CLUSTERING MODEL

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

cluster_labels = kmeans.fit_predict(scaled_features)


# 11. ASSIGN CLUSTER LABELS TO CUSTOMERS

customer_data["Cluster"] = cluster_labels


# 12. DISPLAY CLUSTER DISTRIBUTION

print("\nK-MEANS MODEL TRAINED SUCCESSFULLY")

print("\nCUSTOMER CLUSTER DISTRIBUTION:")
print(customer_data["Cluster"].value_counts().sort_index())


# 13. SAVE TRAINED MODEL AND SCALER

joblib.dump(kmeans, "models/kmeans_model.pkl")

joblib.dump(scaler, "models/scaler.pkl")


print("\nMODEL AND SCALER SAVED SUCCESSFULLY")


# 14. SAVE CUSTOMER SEGMENTATION RESULTS

customer_data.to_csv(
    "outputs/results/customer_segments_final.csv"
)

print("\nCUSTOMER SEGMENTATION RESULTS SAVED SUCCESSFULLY")


# 15. VALIDATE FINAL CUSTOMER SEGMENTATION FILE

saved_data = pd.read_csv(
    "outputs/results/customer_segments_final.csv"
)

print("\nFINAL SEGMENTATION FILE VALIDATION")

print("Dataset Shape:", saved_data.shape)

print("\nAvailable Columns:")
print(saved_data.columns.tolist())

print("\nCluster Distribution:")
print(saved_data["Cluster"].value_counts().sort_index())

print("\nMissing Values:")
print(saved_data.isnull().sum().sum())