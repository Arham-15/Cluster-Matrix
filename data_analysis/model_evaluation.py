# 1. IMPORT REQUIRED LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.decomposition import PCA


# 2. LOAD DATASET

df = pd.read_csv("data/Ecommerce.csv")

print("DATASET LOADED SUCCESSFULLY")
print("Original Dataset Shape:", df.shape)

# 3. CUSTOMER-LEVEL AGGREGATION

customer_data = df.groupby("customer_id").agg({

    "session_id": "count",
    "purchased": "sum",
    "revenue": "sum",
    "pages_viewed": "mean",
    "time_on_site_sec": "mean",
    "added_to_cart": "sum",
    "cart_abandoned": "sum"

})

# Rename columns

customer_data.columns = [
    "total_sessions",
    "total_purchases",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions",
    "total_cart_abandonments"
]

print("\nCUSTOMER-LEVEL DATA CREATED")
print(customer_data.head())

print("\nCUSTOMER DATASET SIZE:")
print(customer_data.shape)

# 4. SELECT FEATURES FOR CLUSTERING

selected_features = [
    "total_sessions",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions"
]

customer_features = customer_data[selected_features]

print("\nSELECTED CUSTOMER FEATURES:")
print(customer_features.head())

print("\nSELECTED FEATURES DATASET SIZE:")
print(customer_features.shape)

# 5. FEATURE SCALING

scaler = StandardScaler()

scaled_features = scaler.fit_transform(customer_features)

print("\nFEATURE SCALING COMPLETED")
print("\nSCALED DATASET SIZE:")
print(scaled_features.shape)

# 6. ELBOW METHOD

inertia_values = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(scaled_features)

    inertia_values.append(kmeans.inertia_)

    print("Clusters:", k, "Inertia:", kmeans.inertia_)

    # 7. ELBOW METHOD VISUALIZATION

plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    inertia_values,
    marker="o"
)

plt.title("Elbow Method for Optimal Number of Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")

plt.xticks(range(2, 11))
plt.grid(True)

plt.tight_layout()
plt.savefig("outputs/graphs/elbow_method.png", dpi=300)
plt.show()


# 8. SILHOUETTE SCORE

silhouette_scores = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    cluster_labels = kmeans.fit_predict(scaled_features)

    score = silhouette_score(
        scaled_features,
        cluster_labels
    )

    silhouette_scores.append(score)

    print("Clusters:", k, "Silhouette Score:", score)


    # 9. SILHOUETTE SCORE VISUALIZATION

plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    silhouette_scores,
    marker="o"
)

plt.title("Silhouette Score for Different Cluster Counts")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")

plt.xticks(range(2, 11))
plt.grid(True)

plt.tight_layout()
plt.savefig("outputs/graphs/silhouette_score.png", dpi=300)
plt.show()


# 10. DAVIES-BOULDIN INDEX

db_scores = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    cluster_labels = kmeans.fit_predict(scaled_features)

    score = davies_bouldin_score(
        scaled_features,
        cluster_labels
    )

    db_scores.append(score)

    print("Clusters:", k, "Davies-Bouldin Index:", score)

    # 11. DAVIES-BOULDIN INDEX VISUALIZATION

plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    db_scores,
    marker="o"
)

plt.title("Davies-Bouldin Index for Different Cluster Counts")
plt.xlabel("Number of Clusters")
plt.ylabel("Davies-Bouldin Index")

plt.xticks(range(2, 11))
plt.grid(True)

plt.tight_layout()
plt.savefig("outputs/graphs/davies_bouldin_index.png", dpi=300)
plt.show()


# 12. PCA VISUALIZATION

# Create K-Means model with 3 clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Assign customers to clusters
cluster_labels = kmeans.fit_predict(scaled_features)

# Reduce 5 features into 2 dimensions
pca = PCA(n_components=2)

pca_features = pca.fit_transform(scaled_features)

# Create DataFrame for PCA results
pca_data = pd.DataFrame(
    pca_features,
    columns=["PC1", "PC2"]
)

pca_data["Cluster"] = cluster_labels

print("\nPCA VISUALIZATION DATA:")
print(pca_data.head())

print("\nPCA DATASET SIZE:")
print(pca_data.shape)


# 13. PCA CLUSTER SCATTER PLOT

plt.figure(figsize=(10, 6))

for cluster in range(3):

    cluster_data = pca_data[
        pca_data["Cluster"] == cluster
    ]

    plt.scatter(
        cluster_data["PC1"],
        cluster_data["PC2"],
        label=f"Cluster {cluster}",
        alpha=0.6
    )

plt.title("Customer Segmentation using PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "outputs/graphs/pca_customer_clusters.png",
    dpi=300
)

plt.show()


# 14. CUSTOMER SEGMENT COMPARISON

for k in [2, 3, 5]:

    print("\n===================================")
    print("CUSTOMER SEGMENT ANALYSIS FOR K =", k)
    print("===================================")

    # Create K-Means model
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    # Assign customers to clusters
    cluster_labels = kmeans.fit_predict(scaled_features)

    # Add cluster labels to customer data
    comparison_data = customer_features.copy()

    comparison_data["Cluster"] = cluster_labels

    # Calculate average behaviour of each cluster
    cluster_profile = comparison_data.groupby("Cluster").mean()

    print(cluster_profile.round(2))

    print("\nCUSTOMER COUNT:")
    print(comparison_data["Cluster"].value_counts().sort_index())


    # 15. MEDIAN-BASED CUSTOMER SEGMENT COMPARISON

for k in [2, 3, 5]:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    cluster_labels = kmeans.fit_predict(scaled_features)

    comparison_data = customer_features.copy()
    comparison_data["Cluster"] = cluster_labels

    median_profile = comparison_data.groupby("Cluster").median()

    print("\nMEDIAN CUSTOMER PROFILE FOR K =", k)
    print(median_profile.round(2))


    # 16. CUSTOMER PURCHASE BEHAVIOUR BY CLUSTER

# Create K-Means model with 3 clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Assign cluster labels
cluster_labels = kmeans.fit_predict(scaled_features)

# Create customer-level analysis dataset
validation_data = customer_data.copy()

validation_data["Cluster"] = cluster_labels

# Calculate purchase rate for each cluster
validation_data["purchase_rate"] = (
    validation_data["total_purchases"] /
    validation_data["total_sessions"]
) * 100

# Calculate cart abandonment rate
validation_data["cart_abandonment_rate"] = (
    validation_data["total_cart_abandonments"] /
    validation_data["total_cart_additions"].replace(0, float("nan"))
) * 100

# Calculate cluster-level behaviour
validation_summary = validation_data.groupby("Cluster").agg({
    "total_sessions": "count",
    "total_purchases": "sum",
    "purchase_rate": "mean",
    "cart_abandonment_rate": "mean"
})

validation_summary = validation_summary.rename(
    columns={"total_sessions": "customer_count"}
)

print("\nCUSTOMER PURCHASE BEHAVIOUR BY CLUSTER:")
print(validation_summary.round(2))