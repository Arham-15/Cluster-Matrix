 
# 1. IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt


# 2. LOAD THE DATASET

df = pd.read_csv("data/Ecommerce.csv")


# 3. INSPECT SESSION-LEVEL BEHAVIOUR

print("\nSESSION-LEVEL INSPECTION")
print("=" * 50)

# Total sessions
print("\nTOTAL SESSIONS:")
print(df["session_id"].nunique())

# Sessions per customer
sessions_per_customer = df.groupby("customer_id")["session_id"].count()

print("\nSESSIONS PER CUSTOMER:")
print(sessions_per_customer.describe())

# Purchase behaviour
print("\nPURCHASE BEHAVIOUR:")
print(df["purchased"].value_counts())

# Purchase rate
purchase_rate = df["purchased"].mean() * 100

print("\nPURCHASE RATE:")
print(round(purchase_rate, 2), "%")

# Cart behaviour
print("\nCART BEHAVIOUR:")
print(pd.crosstab(
    df["added_to_cart"],
    df["purchased"]
))

# Cart abandonment
print("\nCART ABANDONMENT:")
print(df["cart_abandoned"].value_counts())

# Average session behaviour by purchase status
print("\nSESSION BEHAVIOUR BY PURCHASE STATUS:")

print(
    df.groupby("purchased")[
        ["pages_viewed", "time_on_site_sec"]
    ].mean()
)


# 4. SESSION REVENUE INSPECTION

print("\nREVENUE BY PURCHASE STATUS:")

print(
    df.groupby("purchased")["revenue"].agg(
        ["count", "mean", "sum", "min", "max"]
    )
)


# 5. VISUALIZE SESSION BEHAVIOUR

# Purchase status distribution
plt.figure(figsize=(7, 5))

df["purchased"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Purchase Status Distribution")
plt.xlabel("Purchased (0 = No, 1 = Yes)")
plt.ylabel("Number of Sessions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Cart abandonment distribution
plt.figure(figsize=(7, 5))

df["cart_abandoned"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Cart Abandonment Distribution")
plt.xlabel("Cart Abandoned (0 = No, 1 = Yes)")
plt.ylabel("Number of Sessions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Average time spent by purchase status
plt.figure(figsize=(7, 5))

df.groupby("purchased")["time_on_site_sec"].mean().plot(
    kind="bar"
)

plt.title("Average Time on Site by Purchase Status")
plt.xlabel("Purchased (0 = No, 1 = Yes)")
plt.ylabel("Average Time (Seconds)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


print("\nSESSION INSPECTION COMPLETED.")
