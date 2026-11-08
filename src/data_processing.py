
# 1. Import Pandas
import pandas as pd


# 2. Load and process customer data
def load_customer_data():

    # Load the original dataset
    data = pd.read_csv("data/Ecommerce.csv")

    # Aggregate session-level data into customer-level data
    customer_data = data.groupby("customer_id").agg({
        "session_id": "count",
        "purchased": "sum",
        "revenue": "sum",
        "pages_viewed": "mean",
        "time_on_site_sec": "mean",
        "added_to_cart": "sum",
        "cart_abandoned": "sum"
    })

    # Rename columns for better understanding
    customer_data.rename(columns={
        "session_id": "total_sessions",
        "purchased": "total_purchases",
        "revenue": "total_revenue",
        "pages_viewed": "average_pages_viewed",
        "time_on_site_sec": "average_time_on_site",
        "added_to_cart": "total_cart_additions",
        "cart_abandoned": "total_cart_abandonments"
    }, inplace=True)

    # Return the processed customer data
    return customer_data
