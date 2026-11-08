
# 1. Import Streamlit
import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_processing import load_customer_data



# 2. Configure the dashboard page
st.set_page_config(
    page_title="Cluster Matrix",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load customer-level data
customer_data = load_customer_data()
# Load customer segmentation results
segmented_data = pd.read_csv(
    "outputs/results/customer_segments_final.csv"
)




# 3. Custom CSS styling
st.markdown("""
<style>

    /* 
       GLOBAL THEME
     */

    .stApp {
        background-color: #111111;
        color: #F5F5F5;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    /* 
       SIDEBAR */

    [data-testid="stSidebar"] {
        background-color: #080808;
        border-right: 1px solid #292929;
    }

    [data-testid="stSidebar"] * {
        color: #F5F5F5;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        border-radius: 7px;
        padding: 8px;
        transition: background-color 0.2s ease;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background-color: #24190F;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background-color: #332014;
        border-left: 3px solid #FF7518;
    }

    /*
       BRANDING AND HEADINGS
     */

    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #FF7518;
        letter-spacing: -1px;
    }

    .sub-title {
        font-size: 15px;
        color: #A6A6A6;
    }

    .accent-line {
        background-color: #FF7518;
        height: 4px;
        width: 65px;
        margin-top: 12px;
        margin-bottom: 25px;
        border-radius: 4px;
    }

    h1 {
        color: #FF7518 !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #F5F5F5 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #F5A05A !important;
        font-weight: 700 !important;
    }

    h4, h5, h6 {
        color: #BDBDBD !important;
        font-weight: 650 !important;
    }

    /* 
       METRICS
     */

    [data-testid="stMetric"] {
        background-color: #191919;
        border: 1px solid #303030;
        border-radius: 10px;
        padding: 16px;
    }

    [data-testid="stMetricLabel"] {
        color: #A6A6A6 !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricValue"] {
        color: #FF9A4D !important;
        font-weight: 750 !important;
    }

    /* 
       BUTTONS
     */

    .stButton > button {
        background-color: #FF7518;
        color: #111111;
        border: 1px solid #FF7518;
        border-radius: 7px;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #FF923F;
        border-color: #FF923F;
        color: #111111;
    }

    /* 
       INPUT FIELDS
     */

    .stTextInput input,
    .stNumberInput input {
        background-color: #191919;
        color: #F5F5F5;
        border: 1px solid #444444;
        border-radius: 7px;
    }

    .stTextInput input:focus,
    .stNumberInput input:focus {
        border-color: #FF7518;
    }

    /* 
       TABLES AND DATAFRAMES
     */

    [data-testid="stDataFrame"] {
        border: 1px solid #303030;
        border-radius: 8px;
        overflow: hidden;
    }

    /* 
       CAPTIONS AND DIVIDERS
     */

    [data-testid="stCaptionContainer"] {
        color: #A6A6A6 !important;
    }

    hr {
        border-color: #333333 !important;
    }

</style>
""", unsafe_allow_html=True)




# 4. Sidebar branding
st.sidebar.markdown("""
<div style="padding: 20px 0px 30px 0px;">
    <div style="font-size: 27px; font-weight: 800;">
        ◈ CLUSTER
    </div>
    <div style="font-size: 27px; font-weight: 800;">
        MATRIX
    </div>
    <div style="font-size: 11px; letter-spacing: 2px; margin-top: 8px;">
        CUSTOMER INTELLIGENCE
    </div>
</div>
""", unsafe_allow_html=True)



# 5. Sidebar navigation
st.sidebar.markdown("---")

st.sidebar.markdown("### NAVIGATION")

page = st.sidebar.radio(
    "Go to",
    [
        "Command Center",
        "Segment Intelligence",
        "Model Studio",
        "Customer Directory",
        "Strategic Insights",
        "Project Team"
    ],
    label_visibility="collapsed"
)


# 6. Main page heading
st.markdown(
    '<div class="main-title">CLUSTER MATRIX</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">E-Commerce Customer Intelligence & Behavioural Segmentation</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="accent-line"></div>',
    unsafe_allow_html=True
)



# 7. Display selected page


if page == "Command Center":

       
    # 1. COMMAND CENTER WELCOME BANNER
    

        

    st.markdown(
        """
<div style="background: linear-gradient(120deg, #24150C, #111111); border: 1px solid #49301F; border-left: 5px solid #FF7518; border-radius: 12px; padding: 30px 32px; margin-bottom: 25px;">

<div style="color: #FF7518; font-size: 12px; font-weight: 700; letter-spacing: 3px; margin-bottom: 12px;">
CUSTOMER INTELLIGENCE PLATFORM
</div>

<div style="color: #FFFFFF; font-size: 34px; font-weight: 800; letter-spacing: -1px; margin-bottom: 10px;">
CLUSTER MATRIX
</div>

<div style="color: #C0B5AC; font-size: 15px; line-height: 1.6; max-width: 700px;">
Understand customer behaviour, uncover meaningful patterns, and transform e-commerce data into actionable business insights.
</div>

<div style="color: #FF923F; font-size: 11px; font-weight: 700; letter-spacing: 2px; margin-top: 22px;">
UNDERSTAND CUSTOMERS. DISCOVER PATTERNS. FIND SEGMENTS.
</div>

</div>
        """,
        unsafe_allow_html=True
    )

    
    # 2. CALCULATE KEY METRICS
    

    total_customers = customer_data.shape[0]
    total_sessions = customer_data["total_sessions"].sum()
    total_purchases = customer_data["total_purchases"].sum()
    total_revenue = customer_data["total_revenue"].sum()

    purchase_rate = (
        total_purchases / total_sessions
    ) * 100

    average_revenue = (
        total_revenue / total_customers
    )

    
    # 3. CUSTOMER PERFORMANCE SNAPSHOT
    

    st.subheader("Customer Snapshot")
    st.caption(
        "A consolidated view of customer activity and purchasing performance."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "TOTAL CUSTOMERS",
        f"{total_customers:,}"
    )

    col2.metric(
        "TOTAL SESSIONS",
        f"{total_sessions:,}"
    )

    col3.metric(
        "TOTAL PURCHASES",
        f"{total_purchases:,}"
    )

    col4.metric(
        "PURCHASE RATE",
        f"{purchase_rate:.2f}%"
    )
        
    # 4. BUSINESS PERFORMANCE HIGHLIGHT
    

    st.markdown("---")
    st.subheader("Business Performance Highlight")

    st.caption(
        "Understanding the revenue contribution of high-value customers."
    )

    # Identify high-value customers
    high_value_customers = segmented_data[
        segmented_data["Cluster"] == 1
    ]

    # Calculate their revenue contribution
    high_value_revenue = (
        high_value_customers["total_revenue"].sum()
    )

    revenue_contribution = (
        high_value_revenue / total_revenue
    ) * 100 if total_revenue > 0 else 0

    customer_contribution = (
        len(high_value_customers) / total_customers
    ) * 100 if total_customers > 0 else 0

    highlight_col1, highlight_col2 = st.columns(2)

    highlight_col1.metric(
        "HIGH-VALUE CUSTOMER REVENUE SHARE",
        f"{revenue_contribution:.2f}%"
    )

    highlight_col2.metric(
        "SHARE OF CUSTOMER BASE",
        f"{customer_contribution:.2f}%"
    )

    st.info(
        f"High-Value Customers represent "
        f"{customer_contribution:.2f}% of customers "
        f"and contribute {revenue_contribution:.2f}% "
        f"of total customer revenue."
    )

    
    # 4. REVENUE INTELLIGENCE
    

    st.markdown("---")
    st.subheader("Revenue Intelligence")
    st.caption(
        "An overview of revenue generated across the customer base."
    )

    revenue_col1, revenue_col2 = st.columns([1, 2])

    with revenue_col1:

        st.markdown("#### Total Revenue")

        st.metric(
            "REVENUE GENERATED",
            f"{total_revenue:,.2f}"
        )

        st.markdown("#### Average Revenue")

        st.metric(
            "REVENUE PER CUSTOMER",
            f"{average_revenue:,.2f}"
        )

    with revenue_col2:

        st.markdown("#### Customer Revenue Distribution")

        revenue_chart = px.histogram(
            customer_data,
            x="total_revenue",
            nbins=30,
            labels={
                "total_revenue": "Revenue per Customer",
                "count": "Number of Customers"
            }
        )

        revenue_chart.update_traces(
            marker_color="#FF7518",
            marker_line_color="#111111",
            marker_line_width=1
        )

        revenue_chart.update_layout(
            template="plotly_dark",
            paper_bgcolor="#191919",
            plot_bgcolor="#191919",
            font_color="#F5F5F5",
            showlegend=False,
            margin=dict(l=20, r=20, t=30, b=20),
            xaxis_title="Revenue per Customer",
            yaxis_title="Number of Customers",
            bargap=0.08
        )

        st.plotly_chart(
            revenue_chart,
            use_container_width=True
        )
            # =====================================
    # 5. SEGMENT REVENUE CONTRIBUTION
    # =====================================

    st.markdown("---")
    st.subheader("Segment Revenue Contribution")

    st.caption(
        "Percentage of total revenue generated by each customer segment."
    )

    # Calculate total revenue for each segment
    segment_revenue = segmented_data.groupby("Cluster")[
        "total_revenue"
    ].sum().reset_index()

    # Assign readable segment names
    segment_labels = {
        0: "Engaged Browsers",
        1: "High-Value Customers",
        2: "Quick Browsers"
    }

    segment_revenue["Customer Segment"] = (
        segment_revenue["Cluster"].map(segment_labels)
    )

    # Calculate revenue contribution percentage
    segment_revenue["Revenue Contribution"] = (
        segment_revenue["total_revenue"]
        / segment_revenue["total_revenue"].sum()
    ) * 100

    # Create comparison chart
    contribution_chart = px.bar(
        segment_revenue,
        x="Customer Segment",
        y="Revenue Contribution",
        color="Customer Segment",
        text="Revenue Contribution",
        color_discrete_map={
            "Engaged Browsers": "#FF7518",
            "High-Value Customers": "#F5A05A",
            "Quick Browsers": "#A6A6A6"
        },
        labels={
            "Customer Segment": "Customer Segment",
            "Revenue Contribution": "Revenue Contribution (%)"
        }
    )

    contribution_chart.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    contribution_chart.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font_color="#F5F5F5",
        showlegend=False,
        yaxis_title="Revenue Contribution (%)",
        xaxis_title="Customer Segment",
        margin=dict(l=20, r=20, t=30, b=20),
        height=400
    )

    contribution_chart.update_yaxes(
        range=[0, 80],
        dtick=10
    )

    st.plotly_chart(
        contribution_chart,
        use_container_width=True
    )

    
    # 5. DASHBOARD FOOTNOTE
    

    st.markdown("---")

    st.caption(
        "CLUSTER MATRIX  |  CUSTOMER INTELLIGENCE & BEHAVIOURAL SEGMENTATION"
    )


elif page == "Segment Intelligence":

    # 1. Page heading
    st.subheader("Customer Segment Distribution")
    st.caption(
        "An overview of customers grouped by the K-Means clustering model."
    )

    # 2. Define segment names FIRST
    cluster_names = {
        0: "Engaged Browsers",
        1: "High-Value Customers",
        2: "Quick Browsers"
    }
    
    
    # Segment summary cards
    segment_summary = segmented_data.groupby("Cluster").agg(
        customer_count=("customer_id", "count"),
        average_revenue=("total_revenue", "mean")
    )

    col1, col2, col3 = st.columns(3)

    for column, cluster_id in zip(
        [col1, col2, col3],
        [0, 1, 2]
    ):
        details = segment_summary.loc[cluster_id]

        column.metric(
            cluster_names[cluster_id],
            f"{int(details['customer_count']):,} customers",
            f"Avg. revenue: {details['average_revenue']:,.2f}"
        )

    # 2. Count customers in each cluster
    cluster_counts = (
        segmented_data["Cluster"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    cluster_counts.columns = ["Cluster", "Customer Count"]
        

    cluster_counts["Segment"] = (
        cluster_counts["Cluster"].map(cluster_names)
    )

    # 3. Create the segment distribution chart
    segment_chart = px.bar(
        cluster_counts,
        x="Segment",
        y="Customer Count",
        text="Customer Count",
        title="Customer Distribution Across Clusters",
        labels={
            "Segment": "Customer Segment",
            "Customer Count": "Number of Customers"
        }
    )

    # 4. Apply dashboard styling
    segment_chart.update_traces(
        marker_color="#FF7518",
        textposition="outside"
    )

    segment_chart.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font_color="#F5F5F5",
        title_font_color="#FF7518",
        
    )

    # 5. Display chart
    st.plotly_chart(segment_chart, use_container_width=True)

        # 6. Calculate customer segment profiles
    segment_profile = segmented_data.groupby("Cluster").agg({
        "total_sessions": "mean",
        "total_revenue": "mean",
        "average_pages_viewed": "mean",
        "average_time_on_site": "mean",
        "total_cart_additions": "mean"
    }).round(2)
        # Replace cluster numbers with segment names
    segment_profile.index = segment_profile.index.map(cluster_names)
    segment_profile.index.name = "Customer Segment"

    # 7. Display segment profile table
    st.markdown("---")
    st.subheader("Customer Behaviour Profiles")
    st.caption(
        "Average customer behaviour across the three identified segments."
    )

    st.dataframe(
        segment_profile,
        use_container_width=True
    )
        # 8. Compare average revenue across customer segments
    st.markdown("---")
    st.subheader("Revenue Comparison")
    st.caption(
        "Average revenue generated per customer in each segment."
    )

    revenue_comparison = segment_profile.reset_index()

    revenue_chart = px.bar(
        revenue_comparison,
        x="Customer Segment",
        y="total_revenue",
        text="total_revenue",
        title="Average Revenue by Customer Segment",
        labels={
            "Customer Segment": "Customer Segment",
            "total_revenue": "Average Revenue"
        }
    )

    revenue_chart.update_traces(
        marker_color="#FF7518",
        texttemplate="%{text:,.2f}",
        textposition="outside"
    )

    revenue_chart.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font_color="#F5F5F5",
        title_font_color="#FF7518"
    )

    st.plotly_chart(
        revenue_chart,
        use_container_width=True
    )


elif page == "Model Studio":

    # 1. Page heading
    st.subheader("Clustering Model Laboratory")
    st.caption(
        "Explore the machine learning architecture behind customer segmentation."
    )

    # 2. Model configuration
    st.markdown("### Model Configuration")

    col1, col2, col3 = st.columns(3)

    col1.metric("ALGORITHM", "K-Means")
    col2.metric("NUMBER OF CLUSTERS", "3")
    col3.metric("CUSTOMERS ANALYSED", "8,442")

    # 3. Model details
    st.markdown("---")
    st.markdown("### Training Configuration")

    model_details = pd.DataFrame({
        "Parameter": [
            "Algorithm",
            "Number of clusters",
            "Random state",
            "Initialisations",
            "Feature scaling",
            "Scaling method"
        ],
        "Value": [
            "K-Means",
            "3",
            "42",
            "10",
            "Enabled",
            "StandardScaler"
        ]
    })

    st.dataframe(
        model_details,
        hide_index=True,
        use_container_width=True
    )
        # 4. Model evaluation
    st.markdown("---")
    st.markdown("### Model Evaluation")

    col1, col2 = st.columns(2)

    col1.metric(
        "SILHOUETTE SCORE",
        "0.2070"
    )

    col2.metric(
        "DAVIES-BOULDIN INDEX",
        "1.5456"
    )

    st.caption(
        "Evaluation results for the K-Means model with 3 clusters."
    )

           # 5. Elbow Method Analysis
    st.markdown("---")
    st.markdown("### Optimal Cluster Analysis")

    st.caption(
        "EVALUATION METHOD  /  CLUSTER SELECTION"
    )

    col1, col2 = st.columns([1.7, 1])

    with col1:
        st.markdown("#### Elbow Method")
        st.image(
            "outputs/graphs/elbow_method.png",
            use_container_width=True
        )

    with col2:
        st.markdown("#### What the curve tells us")

        st.markdown(
            """
            The Elbow Method measures how clustering
            inertia changes as the number of clusters increases.

            **Key observation**

            The curve does not show a sharp elbow.
            This suggests there is no single obvious
            cluster count based on inertia alone.

            **Model decision**

            We use 3 clusters as a provisional choice
            to balance interpretability and segment size.
            """
        )

        st.info(
            "K = 3 is an interpretability-based choice, "
            "not the metric-optimal solution."
        )
            # 6. Silhouette and Davies-Bouldin Analysis
    st.markdown("---")
    st.markdown("### Cluster Quality Assessment")

    st.caption(
        "TWO METRICS  /  MEASURING CLUSTER QUALITY"
    )

    col1, col2 = st.columns(2)

    # Silhouette Score
    with col1:
        st.markdown("#### Silhouette Score")

        st.metric(
            "K = 3",
            "0.2070",
            help="Higher values generally indicate better-separated clusters."
        )

        st.image(
            "outputs/graphs/silhouette_score.png",
            use_container_width=True
        )

        st.caption(
            "Measures how well customers fit within their assigned "
            "cluster compared with other clusters."
        )

    # Davies-Bouldin Index
    with col2:
        st.markdown("#### Davies-Bouldin Index")

        st.metric(
            "K = 3",
            "1.5456",
            help="Lower values generally indicate more compact and distinct clusters."
        )

        st.image(
            "outputs/graphs/davies_bouldin_index.png",
            use_container_width=True
        )

        st.caption(
            "Measures cluster compactness and separation. "
            "Lower values generally indicate better clustering."
        )

            # 7. Customer Cluster Visualisation
    st.markdown("---")
    st.markdown("### Customer Cluster Mapping")

    st.caption(
        "DIMENSIONALITY REDUCTION  /  PCA VISUALISATION"
    )

    col1, col2 = st.columns([1.6, 1])

    with col1:
        st.image(
            "outputs/graphs/pca_customer_clusters.png",
            use_container_width=True
        )

    with col2:
        st.markdown("#### Understanding the Map")

        st.write(
            "PCA reduces the five clustering features "
            "into two principal components."
        )

        st.write(
            "Each point represents a customer. Colours "
            "represent the assigned customer clusters."
        )

        st.info(
            "Some overlap is visible in this 2D projection. "
            "This does not necessarily mean the clusters "
            "overlap in the original five-dimensional feature space."
        )

elif page == "Customer Directory":

    # 1. Page heading
    st.subheader("Customer Directory")
    st.caption(
        "Search individual customers and explore their behavioural profiles."
    )
    
    # 2. Customer filters
    st.markdown("### Explore Customer Segments")

    customer_names = {
        0: "Engaged Browsers",
        1: "High-Value Customers",
        2: "Quick Browsers"
    }

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_segment = st.selectbox(
            "Filter by Customer Segment",
            ["All Segments"] + list(customer_names.values())
        )

    with filter_col2:
        max_revenue = float(segmented_data["total_revenue"].max())

        revenue_limit = st.slider(
            "Maximum Customer Revenue",
            min_value=0.0,
            max_value=max_revenue,
            value=max_revenue
        )

    # Apply selected filters
    filtered_customers = segmented_data.copy()

    if selected_segment != "All Segments":
        selected_cluster = {
            name: cluster
            for cluster, name in customer_names.items()
        }[selected_segment]

        filtered_customers = filtered_customers[
            filtered_customers["Cluster"] == selected_cluster
        ]

    filtered_customers = filtered_customers[
        filtered_customers["total_revenue"] <= revenue_limit
    ]

    # Display matching customer count
    st.metric(
        "MATCHING CUSTOMERS",
        f"{len(filtered_customers):,}"
    )

       # Display filtered customer table with segment labels

    customer_display = filtered_customers[
        [
            "customer_id",
            "total_sessions",
            "total_purchases",
            "total_revenue",
            "Cluster"
        ]
    ].copy()

    # Convert cluster numbers into readable segment names
    customer_display["Customer Segment"] = (
        customer_display["Cluster"].map(customer_names)
    )

    # Remove the numeric cluster column
    customer_display.drop(columns=["Cluster"], inplace=True)

    # Apply colours to customer segment labels
    def highlight_segment(column):

        colors = {
            "Engaged Browsers": "#FF7518",
            "High-Value Customers": "#F5A05A",
            "Quick Browsers": "#A6A6A6"
        }

        return [
            f"background-color: #292929; color: {colors[value]}; font-weight: bold;"
            for value in column
        ]

    styled_customer_table = customer_display.style.apply(
        highlight_segment,
        subset=["Customer Segment"]
    )

    st.dataframe(
        styled_customer_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")
    
    # 3. Customer segment revenue comparison
    st.markdown("### Segment Revenue Comparison")

    segment_revenue = segmented_data.groupby("Cluster")[
        "total_revenue"
    ].mean().reset_index()

    segment_revenue["Customer Segment"] = (
        segment_revenue["Cluster"].map(customer_names)
    )

    revenue_chart = px.bar(
        segment_revenue,
        x="Customer Segment",
        y="total_revenue",
        color="Customer Segment",
        color_discrete_sequence=[
            "#FF7518",
            "#F5A05A",
            "#A6A6A6"
        ],
        title="Average Revenue by Customer Segment",
        labels={
            "total_revenue": "Average Revenue",
            "Customer Segment": "Customer Segment"
        }
    )

    revenue_chart.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font_color="#F5F5F5",
        title_font_color="#FF7518",
        showlegend=False
    )

    st.plotly_chart(
        revenue_chart,
        use_container_width=True
    )

    st.markdown("---")



    # 2. Customer search
    st.markdown("### Find a Customer")

    customer_id = st.text_input(
        "Enter Customer ID",
        placeholder="Example: 1001"
    )

    # 3. Search customer records
    if customer_id:

        if customer_id.isdigit():

            search_id = int(customer_id)

            customer_result = segmented_data[
                segmented_data["customer_id"] == search_id
            ]

            if not customer_result.empty:

                customer = customer_result.iloc[0]

                st.success("Customer record found!")

                # 4. Identify customer segment
                customer_cluster = int(customer["Cluster"])

                customer_names = {
                    0: "Engaged Browsers",
                    1: "High-Value Customers",
                    2: "Quick Browsers"
                }

                st.markdown("### Customer Profile")

                st.metric(
                    "CUSTOMER SEGMENT",
                    customer_names[customer_cluster]
                )

                # 5. Display customer metrics
                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "TOTAL SESSIONS",
                    int(customer["total_sessions"])
                )

                col2.metric(
                    "TOTAL REVENUE",
                    f"{customer['total_revenue']:,.2f}"
                )

                col3.metric(
                    "TOTAL PURCHASES",
                    int(customer["total_purchases"])
                )

                col4, col5, col6 = st.columns(3)

                col4.metric(
                    "AVG. PAGES VIEWED",
                    f"{customer['average_pages_viewed']:.2f}"
                )

                col5.metric(
                    "AVG. TIME ON SITE",
                    f"{customer['average_time_on_site']:.2f} sec"
                )

                col6.metric(
                    "CART ADDITIONS",
                    int(customer["total_cart_additions"])
                )

                                # 6. Customer Activity Summary
                st.markdown("---")
                st.markdown("#### Customer Activity Summary")

                cart_additions = int(customer["total_cart_additions"])
                cart_abandonments = int(customer["total_cart_abandonments"])

                if cart_additions > 0:
                    abandonment_rate = (
                        cart_abandonments / cart_additions
                    ) * 100

                    abandonment_display = f"{abandonment_rate:.2f}%"
                else:
                    abandonment_display = "N/A"

                activity_col1, activity_col2 = st.columns(2)

                activity_col1.metric(
                    "CART ABANDONMENTS",
                    cart_abandonments
                )

                activity_col2.metric(
                    "CART ABANDONMENT RATE",
                    abandonment_display
                )

            else:
                st.warning("No customer found with this ID.")

        else:
            st.warning("Please enter a valid numeric Customer ID.")


elif page == "Strategic Insights":

    # 1. Page heading
    st.subheader("Strategic Insights")

    st.caption(
        "BUSINESS INTELLIGENCE  /  CUSTOMER BEHAVIOUR"
    )

    st.markdown("---")

    # 2. Segment insights
    st.markdown("### Key Customer Findings")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### High-Value Customers")
        st.metric("Average Revenue", "2,657.15")

        st.write(
            "Cluster 1 generates the highest average "
            "revenue per customer."
        )

    with col2:
        st.markdown("#### Cart Abandonment")
        st.metric("Cluster 1 Rate", "57.51%")

        st.write(
            "Cluster 1 has a lower average cart "
            "abandonment rate than the other segments."
        )

    with col3:
        st.markdown("#### Customer Engagement")
        st.metric("Cluster 0 Time", "1,239 sec")

        st.write(
            "Cluster 0 has the highest average "
            "time spent on the website."
        )
        # 3. Business Recommendations
    st.markdown("---")
    st.markdown("### Recommended Business Actions")

    st.caption(
        "DATA-DRIVEN STRATEGY  /  POTENTIAL ACTIONS"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 01 / Conversion Improvement")

        st.write(
            "Customers in Clusters 0 and 2 show higher "
            "average cart abandonment rates."
        )

        st.info(
            "Recommendation: Investigate checkout friction, "
            "unexpected costs and payment difficulties."
        )

        st.markdown("---")

        st.markdown("#### 02 / Customer Retention")

        st.write(
            "Cluster 1 has the highest average revenue "
            "and purchase rate."
        )

        st.info(
            "Recommendation: Explore loyalty programmes, "
            "personalised offers and retention campaigns."
        )

    with col2:
        st.markdown("#### 03 / Browsing Experience")

        st.write(
            "Cluster 0 has the highest average time "
            "spent on the website."
        )

        st.info(
            "Recommendation: Examine navigation patterns "
            "and product discovery to identify possible "
            "areas for improvement."
        )

        st.markdown("---")

        st.markdown("#### 04 / Segment Monitoring")

        st.write(
            "The three customer segments show different "
            "engagement and purchasing patterns."
        )

        st.info(
            "Recommendation: Monitor segment performance "
            "over time and evaluate campaign outcomes."
        )
            # 4. Customer Segment Comparison
    st.markdown("---")
    st.markdown("### Segment Performance Comparison")

    st.caption(
        "REVENUE ANALYSIS  /  CUSTOMER SEGMENTS"
    )

    # Calculate average revenue for each segment
    revenue_comparison = segmented_data.groupby("Cluster")[
        "total_revenue"
    ].mean().reset_index()

        # Define customer segment names
    cluster_labels = {
        0: "Engaged Browsers",
        1: "High-Value Customers",
        2: "Quick Browsers"
    }

    # Replace cluster numbers with segment names
    revenue_comparison["Customer Segment"] = (
        revenue_comparison["Cluster"].map(cluster_labels)
    )

    # Create the bar chart
    fig = px.bar(
        revenue_comparison,
        x="Customer Segment",
        y="total_revenue",
        color="Customer Segment",
        color_discrete_sequence=[
            "#FF7518",
            "#F5A05A",
            "#A6A6A6"
        ],
        title="Average Revenue by Customer Segment"
    )

    fig.update_layout(
        plot_bgcolor="#111111",
        paper_bgcolor="#111111",
        font_color="#F5F5F5",
        showlegend=False,
        xaxis_title="Customer Segment",
        yaxis_title="Average Revenue",
        title_font_color="#FF7518"
    )

    fig.update_xaxes(
        showgrid=False,
        color="#BDBDBD"
    )

    fig.update_yaxes(
        gridcolor="#333333",
        color="#BDBDBD"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
elif page == "Project Team":

    st.markdown("## Project Team")
    st.caption("THE PEOPLE AND CONTRIBUTIONS BEHIND CLUSTER MATRIX")

    st.markdown("---")

    st.markdown("### A Collaborative Project")

    st.write(
        "Cluster Matrix brings together data analysis, "
        "machine learning and business intelligence to "
        "understand e-commerce customer behaviour."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 01 / Arisha")
        st.markdown("**Data & Machine Learning**")

        st.write(
            "- Dataset inspection and preprocessing\n"
            "- Exploratory data analysis\n"
            "- Customer feature aggregation\n"
            "- K-Means clustering\n"
            "- Model evaluation and segment analysis"
        )

    with col2:
        st.markdown("### 02 / Alveera")
        st.markdown("**Dashboard & Business Intelligence**")

        st.write(
            "- Streamlit dashboard development\n"
            "- Customer directory and search\n"
            "- Interactive charts and visualisations\n"
            "- Customer segment presentation\n"
            "- Strategic insights and recommendations"
        )

    st.markdown("---")
    st.markdown("### Shared Contributions")

    st.write(
        "- Project planning and research\n"
        "- Interpretation of results\n"
        "- Testing and debugging\n"
        "- Documentation and final presentation"
    )

    st.markdown("---")

    st.markdown(
        "<h2 style='text-align:center; color:#FF7518;'>"
        "◈ CLUSTER MATRIX</h2>",
        unsafe_allow_html=True
    )

    st.caption(
        "Understand customers. Discover patterns. Find segments."
    )

    st.caption(
        "Developed as an academic project."
    )