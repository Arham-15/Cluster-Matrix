# 1. IMPORT LIBRARIES

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score


# 2. LOAD DATASET

data = pd.read_csv("data/Ecommerce.csv")

print("DATASET LOADED SUCCESSFULLY")


# 3. CREATE CUSTOMER-LEVEL DATA

customer_data = data.groupby("customer_id").agg({
    "session_id": "count",
    "purchased": "sum",
    "revenue": "sum",
    "pages_viewed": "mean",
    "time_on_site_sec": "mean",
    "added_to_cart": "sum",
    "cart_abandoned": "sum"
})

customer_data.columns = [
    "total_sessions",
    "total_purchases",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions",
    "total_cart_abandonments"
]


# 4. SELECT CUSTOMER FEATURES

selected_features = [
    "total_sessions",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions"
]

customer_features = customer_data[selected_features]


# 5. FEATURE SCALING

scaler = StandardScaler()

scaled_features = scaler.fit_transform(customer_features)

print("FEATURE SCALING COMPLETED")


# 6. AGGLOMERATIVE CLUSTERING

for k in [2, 3, 5]:

    model = AgglomerativeClustering(
        n_clusters=k,
        linkage="ward"
    )

    cluster_labels = model.fit_predict(scaled_features)

    silhouette = silhouette_score(
        scaled_features,
        cluster_labels
    )

    db_index = davies_bouldin_score(
        scaled_features,
        cluster_labels
    )

    print("\n------------------------------")
    print("AGGLOMERATIVE CLUSTERING: K =", k)
    print("------------------------------")

    print("Silhouette Score:", round(silhouette, 4))
    print("Davies-Bouldin Index:", round(db_index, 4))

    comparison_data = customer_features.copy()

    comparison_data["Cluster"] = cluster_labels

    cluster_profile = comparison_data.groupby("Cluster").mean()

    print("\nCUSTOMER SEGMENT PROFILE:")
    print(cluster_profile.round(2))

    print("\nCUSTOMER COUNT:")
    print(comparison_data["Cluster"].value_counts().sort_index())