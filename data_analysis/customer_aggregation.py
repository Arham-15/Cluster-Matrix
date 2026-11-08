
# 1. IMPORT LIBRARIES

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 2. LOAD THE DATASET

df = pd.read_csv("data/Ecommerce.csv")


print("\nDATASET LOADED SUCCESSFULLY")

print("\nORIGINAL DATASET SIZE:")
print(df.shape)



# 3. AGGREGATE DATA CUSTOMER-WISE

customer_data = df.groupby("customer_id").agg(

    total_sessions=("session_id", "count"),

    total_purchases=("purchased", "sum"),

    total_revenue=("revenue", "sum"),

    average_pages_viewed=("pages_viewed", "mean"),

    average_time_on_site=("time_on_site_sec", "mean"),

    total_cart_additions=("added_to_cart", "sum"),

    total_cart_abandonments=("cart_abandoned", "sum")

)


# 4. DISPLAY CUSTOMER DATA

print("\nCUSTOMER-LEVEL DATA:")
print(customer_data.head())

print("\nCUSTOMER DATASET SIZE:")
print(customer_data.shape)



# 5. CALCULATE CUSTOMER BEHAVIOUR RATES

customer_data["purchase_rate"] = (
    customer_data["total_purchases"] /
    customer_data["total_sessions"]
) * 100


customer_data["cart_abandonment_rate"] = (
    customer_data["total_cart_abandonments"] /
    customer_data["total_cart_additions"].replace(0, float("nan"))
) * 100


# 6. DISPLAY CUSTOMER BEHAVIOUR RATES

print("\nCUSTOMER PURCHASE AND CART RATES:")

print(
    customer_data[
        ["purchase_rate", "cart_abandonment_rate"]
    ].head()
)



# 7. CHECK FINAL CUSTOMER DATA

print("\nFINAL CUSTOMER DATA:")
print(customer_data.head())

print("\nFINAL CUSTOMER DATASET SIZE:")
print(customer_data.shape)

print("\nCUSTOMER DATA SUMMARY:")
print(customer_data.describe())


# 8. SAVE CUSTOMER-LEVEL DATASET
# Save customer-level summary
customer_data.to_csv("outputs/results/customer_summary.csv")

# Save final customer segments
customer_data.to_csv("outputs/results/customer_segments.csv")

print("\nCUSTOMER-LEVEL DATASET SAVED SUCCESSFULLY")


# 9. CHECK CORRELATION BETWEEN CUSTOMER FEATURES
print("\nCUSTOMER FEATURE CORRELATION:")
print(customer_data.corr().round(2))


# 10. SELECT FEATURES FOR CUSTOMER SEGMENTATION
selected_features = [
    "total_sessions",
    "total_revenue",
    "average_pages_viewed",
    "average_time_on_site",
    "total_cart_additions"
]

customer_features = customer_data[selected_features]




# 11. DISPLAY SELECTED FEATURES
print("\nSELECTED CUSTOMER FEATURES:")
print(customer_features.head())

print("\nSELECTED FEATURES DATASET SIZE:")
print(customer_features.shape)


# 12. SCALE CUSTOMER FEATURES
scaler = StandardScaler()

scaled_features = scaler.fit_transform(customer_features)

print("\nFEATURE SCALING COMPLETED")
print("\nSCALED FEATURES:")
print(scaled_features[:5])

print("\nSCALED DATASET SIZE:")
print(scaled_features.shape)

# 13. FIND OPTIMAL NUMBER OF CLUSTERS
wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(scaled_features)

    wcss.append(kmeans.inertia_)

# 14. PLOT ELBOW GRAPH
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker="o")

plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.xticks(range(1, 11))
plt.grid(True)
plt.tight_layout()
plt.show()

# 15. APPLY K-MEANS CLUSTERING
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

customer_data["Cluster"] = kmeans.fit_predict(scaled_features)

# 16. DISPLAY CLUSTER ASSIGNMENTS
print("\nCUSTOMER CLUSTER ASSIGNMENTS:")
print(customer_data[["Cluster"]].head(10))

print("\nNUMBER OF CUSTOMERS IN EACH CLUSTER:")
print(customer_data["Cluster"].value_counts().sort_index())



# 17. ANALYZE CUSTOMER CLUSTERS

cluster_summary = customer_data.groupby("Cluster")[
    selected_features
].mean()

print("\nCUSTOMER CLUSTER SUMMARY:")
print(cluster_summary.round(2))


# ANALYZE CART ABANDONMENT SEPARATELY

valid_cart_customers = customer_data[
    customer_data["total_cart_additions"] > 0
]

cart_abandonment_summary = valid_cart_customers.groupby("Cluster")[
    "cart_abandonment_rate"
].mean()

print("\nCART ABANDONMENT RATE BY CLUSTER:")
print(cart_abandonment_summary.round(2))


# 18. VISUALIZE AVERAGE REVENUE BY CLUSTER
plt.figure(figsize=(8, 5))

cluster_summary["total_revenue"].plot(kind="bar")

plt.title("Average Revenue by Customer Cluster")
plt.xlabel("Customer Cluster")
plt.ylabel("Average Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 19. VISUALIZE CART ABANDONMENT BY CLUSTER
plt.figure(figsize=(8, 5))

cart_abandonment_summary.plot(kind="bar")

plt.title("Cart Abandonment Rate by Customer Cluster")
plt.xlabel("Customer Cluster")
plt.ylabel("Cart Abandonment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 20. ADD CLUSTER LABELS TO CUSTOMER DATA
customer_data["Cluster"] = kmeans.labels_

# 21. SAVE FINAL CUSTOMER SEGMENTS
customer_data.to_csv("customer_segments.csv")

print("\nFINAL CUSTOMER SEGMENTS SAVED SUCCESSFULLY")

# ==========================================
# CUSTOMER SEGMENT VISUALIZATION
# ==========================================

# 1. CUSTOMER SEGMENT DISTRIBUTION


cluster_counts = customer_data["Cluster"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(cluster_counts.index, cluster_counts.values)

plt.title("Customer Distribution Across Clusters")
plt.xlabel("Customer Cluster")
plt.ylabel("Number of Customers")
plt.xticks([0, 1, 2])

plt.tight_layout()
plt.savefig("outputs/graphs/cluster_distribution.png", dpi=300)
plt.show()


# 2. AVERAGE REVENUE ACROSS CUSTOMER CLUSTERS

plt.figure(figsize=(8, 5))
plt.bar(cluster_summary.index, cluster_summary["total_revenue"])

plt.title("Average Revenue Across Customer Clusters")
plt.xlabel("Customer Cluster")
plt.ylabel("Average Revenue")
plt.xticks([0, 1, 2])

plt.tight_layout()
plt.savefig("outputs/graphs/average_revenue.png", dpi=300)
plt.show()

# 3. CUSTOMER ENGAGEMENT COMPARISON

engagement_data = cluster_summary[
    ["total_sessions", "total_cart_additions", "average_pages_viewed"]
]

engagement_data.plot(kind="bar", figsize=(10, 6))

plt.title("Customer Engagement Across Clusters")
plt.xlabel("Customer Cluster")
plt.ylabel("Average Value")
plt.xticks(rotation=0)
plt.legend(["Sessions", "Cart Additions", "Pages Viewed"])

plt.tight_layout()
plt.savefig("outputs/graphs/customer_engagement.png", dpi=300)
plt.show()




# 4. CART ABANDONMENT RATE ACROSS CLUSTERS

plt.figure(figsize=(8, 5))

plt.bar(
    cart_abandonment_summary.index,
    cart_abandonment_summary.values
)

plt.title("Cart Abandonment Rate Across Clusters")
plt.xlabel("Customer Cluster")
plt.ylabel("Cart Abandonment Rate (%)")
plt.xticks([0, 1, 2])

plt.tight_layout()
plt.savefig("outputs/graphs/cart_abandonment.png", dpi=300)
plt.show()


# 5. CUSTOMER SEGMENT PROFILE

import numpy as np

# Selecting features for comparison
profile_data = cluster_summary[
    ["total_sessions", "total_revenue", "total_cart_additions"]
]

# Normalizing values for radar chart
profile_data = (profile_data - profile_data.min()) / (
    profile_data.max() - profile_data.min()
)

# Creating radar chart angles
categories = list(profile_data.columns)
values = profile_data.values

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plotting each customer cluster
for i in range(len(profile_data)):
    cluster_values = values[i].tolist()
    cluster_values += cluster_values[:1]

    ax.plot(angles, cluster_values, label="Cluster " + str(i))
    ax.fill(angles, cluster_values, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

plt.title("Customer Segment Profile")
plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig("outputs/graphs/customer_segment_profile.png", dpi=300)
plt.show()