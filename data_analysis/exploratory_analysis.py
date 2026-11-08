
# 1. IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt


# 2. LOAD THE DATASET

df = pd.read_csv("data/Ecommerce.csv")


# 3. EXPLORE NUMERICAL FEATURES

columns = [
    "pages_viewed",
    "time_on_site_sec",
    "revenue"
]


# 4. DISPLAY DISTRIBUTION GRAPHS

for col in columns:

    plt.figure(figsize=(8, 5))

    plt.hist(df[col], bins=30, edgecolor="black")

    plt.title("Distribution of " + col)
    plt.xlabel(col)
    plt.ylabel("Number of Sessions")

    plt.tight_layout()
    plt.show()
 

 
# 5. COMPARE BEHAVIOUR BY PURCHASE STATUS

print("\nAVERAGE BEHAVIOUR BY PURCHASE STATUS:")

print(
    df.groupby("purchased")[
        ["pages_viewed", "time_on_site_sec"]
    ].mean()
)


# 6. VISUALIZE BEHAVIOUR BY PURCHASE STATUS

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

df.boxplot(
    column="pages_viewed",
    by="purchased",
    ax=axes[0]
)

axes[0].set_title("Pages Viewed by Purchase Status")
axes[0].set_xlabel("Purchased (0 = No, 1 = Yes)")
axes[0].set_ylabel("Pages Viewed")

df.boxplot(
    column="time_on_site_sec",
    by="purchased",
    ax=axes[1]
)

axes[1].set_title("Time on Site by Purchase Status")
axes[1].set_xlabel("Purchased (0 = No, 1 = Yes)")
axes[1].set_ylabel("Time on Site (seconds)")

plt.suptitle("")

plt.tight_layout()
plt.show()



# 7. EXPLORE CATEGORICAL FEATURES

categorical_columns = [
    "device_type",
    "marketing_channel",
    "product_category"
]


# 8. DISPLAY CATEGORY DISTRIBUTIONS

for col in categorical_columns:

    category_counts = df[col].value_counts().sort_index()

    plt.figure(figsize=(8, 5))

    plt.bar(
        category_counts.index.astype(str),
        category_counts.values,
        edgecolor="black"
    )

    plt.title("Distribution of " + col)
    plt.xlabel(col)
    plt.ylabel("Number of Sessions")

    plt.tight_layout()
    plt.show()



# 9. CHECK CORRELATION BETWEEN NUMERICAL FEATURES

numerical_columns = [
    "pages_viewed",
    "time_on_site_sec",
    "unit_price",
    "quantity",
    "discount_percent",
    "revenue"
]

correlation = df[numerical_columns].corr()

print("\nCORRELATION MATRIX:")
print(correlation)


# 10. DISPLAY CORRELATION HEATMAP

plt.figure(figsize=(10, 7))

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(numerical_columns)),
    numerical_columns,
    rotation=45
)

plt.yticks(
    range(len(numerical_columns)),
    numerical_columns
)

plt.title("Correlation Between Numerical Features")

plt.tight_layout()
plt.show()



# 11. OUTLIER DETECTION USING BOXPLOTS

outlier_columns = [
    "unit_price",
    "quantity",
    "discount_percent",
    "revenue"
]


# 12. DISPLAY BOXPLOTS

for col in outlier_columns:

    plt.figure(figsize=(8, 4))

    plt.boxplot(df[col])

    plt.title("Boxplot of " + col)
    plt.ylabel(col)

    plt.tight_layout()
    plt.show()
