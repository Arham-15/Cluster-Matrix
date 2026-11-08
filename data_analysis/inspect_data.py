# 1. IMPORT LIBRARIES

import pandas as pd


# 2. LOAD THE DATASET

df = pd.read_csv("data/Ecommerce.csv")


# 3. UNDERSTAND THE DATASET

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET SIZE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nDATA INFORMATION:")
df.info()

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nSTATISTICAL SUMMARY:")
print(df.describe())


# 4. CHECK CUSTOMER DETAILS

print("\nTOTAL UNIQUE CUSTOMERS:")
print(df["customer_id"].nunique())

print("\nTOTAL UNIQUE SESSIONS:")
print(df["session_id"].nunique())


# 5. CHECK CUSTOMER BEHAVIOUR

columns = [
    "purchased",
    "added_to_cart",
    "cart_abandoned",
    "device_type",
    "user_type",
    "marketing_channel",
    "product_category"
]

for col in columns:
    print("\n", col, "COUNT:")
    print(df[col].value_counts())


# 6. CHECK REVENUE DETAILS

print("\nREVENUE SUMMARY:")
print(df["revenue"].describe())


# 7. CHECK PURCHASE AND CART RELATIONSHIP

print("\nPURCHASE AND CART DETAILS:")

print(pd.crosstab(df["purchased"], df["added_to_cart"]))

print("\nCART ABANDONMENT DETAILS:")
print(pd.crosstab(df["added_to_cart"], df["cart_abandoned"]))

print("\nPURCHASE AND REVENUE DETAILS:")
print(df.groupby("purchased")["revenue"].describe())


# 8. CHECK CUSTOMER SESSION FREQUENCY

print("\nSESSIONS PER CUSTOMER:")

sessions = df["customer_id"].value_counts()

print(sessions.describe())

print("\nCUSTOMERS WITH MOST SESSIONS:")
print(sessions.head(10))


# 9. CHECK DATE RANGE

df["visit_date"] = pd.to_datetime(
    df["visit_date"],
    format="%d-%m-%Y"
)

print("\nDATE RANGE:")
print("First Date:", df["visit_date"].min())
print("Last Date:", df["visit_date"].max())


# 10. CHECK UNIQUE CATEGORY VALUES

columns = [
    "device_type",
    "user_type",
    "marketing_channel",
    "product_category",
    "payment_method",
    "location"
]

for col in columns:
    print("\nUNIQUE VALUES IN", col)
    print(sorted(df[col].unique()))