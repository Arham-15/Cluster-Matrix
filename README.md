# ◈ Cluster Matrix

### E-Commerce Customer Intelligence & Behavioural Segmentation

**Understand customers. Discover patterns. Find segments.**

Cluster Matrix is a machine learning and data analysis project focused on understanding e-commerce customer behaviour.

The idea behind this project is simple: every customer interacts with an online store differently. Some browse more, some spend more time exploring products, and some make purchases more often than others.

Instead of looking at all customers as one group, Cluster Matrix uses **K-Means clustering** to identify different customer segments and understand how their behaviour varies.

The project also includes an interactive Streamlit dashboard to explore the results and connect the analysis with useful business insights.

---

## What This Project Does

- Analyses customer activity and purchasing patterns.
- Converts session-level data into customer-level information.
- Uses machine learning to group customers with similar behaviour.
- Compares customer segments based on revenue and activity.
- Presents the results through an interactive dashboard.
- Highlights findings that can help businesses understand their customers better.

## Dataset

**Name:** Indian E-Commerce Customer Behavior & Purchase  
**Created by:** Kundan Bedmutha  
**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/kundanbedmutha/indian-e-commerce-customer-behavior-and-purchase)

The dataset contains 25,000 simulated e-commerce session records with 29 columns.

It includes information about customer sessions, purchases, revenue, pages viewed, time spent on the website, cart activity, devices, and marketing channels.

For this project, session records are grouped by customer so that we can study overall customer behaviour rather than looking at each session separately.

*Dataset credit: Kundan Bedmutha. Please refer to the original Kaggle page for the creator's usage terms.*

## How It Works

The project follows a few main steps:

**1. Data Exploration**

First, I inspected the dataset to understand its structure, columns, data types, missing values, and customer activity.

**2. Customer-Level Data**

Since the original data contains individual sessions, I grouped the records using customer IDs. This helped create a summary of each customer's activity.

**3. Feature Selection**

I selected five features for clustering:

- Total sessions
- Total revenue
- Average pages viewed
- Average time on site
- Total cart additions

**4. Feature Scaling**

I used `StandardScaler` to bring the selected features onto a comparable scale before applying the clustering algorithm.

**5. Customer Clustering**

I applied the K-Means algorithm and selected three clusters for the final dashboard.

**6. Model Evaluation**

I compared different cluster configurations using the Elbow Method, Silhouette Score, and Davies-Bouldin Index. I also compared K-Means with Agglomerative Clustering.

## Customer Segments

The final model groups 8,442 customers into three segments.

| Cluster | Segment | Customers |
|---|---|---:|
| 0 | Engaged Browsers | 2,855 |
| 1 | High-Value Customers | 2,644 |
| 2 | Quick Browsers | 2,943 |

Each segment represents a different pattern in the customer data:

- **Engaged Browsers:** Spend more time on the website on average, but generate comparatively lower revenue.
- **High-Value Customers:** Have higher average revenue, more sessions, and more cart additions.
- **Quick Browsers:** Spend less time on the website on average and generate comparatively lower revenue.

These names are based on the average behaviour of each cluster. They do not describe every individual customer.

## Model Results

The final dashboard uses K-Means with three clusters.

| Setting | Value |
|---|---:|
| Algorithm | K-Means |
| Number of clusters | 3 |
| Silhouette Score | 0.2070 |
| Davies-Bouldin Index | 1.5456 |
| Random State | 42 |
| Initialisations | 10 |

I chose three clusters mainly because they provide a reasonably balanced and understandable segmentation. It was not the best configuration across every evaluation metric.

## The Dashboard

The dashboard is built using Streamlit and has six main sections:

| Section | What It Shows |
|---|---|
| Command Center | Customer snapshot and revenue performance |
| Segment Intelligence | Customer segments and their behaviour |
| Model Studio | Model settings and evaluation results |
| Customer Directory | Customer search, filters, and individual profiles |
| Strategic Insights | Key findings and business recommendations |
| Project Team | Project members and contributions |

## Tech Stack

- **Python** for the main programming work
- **Pandas** for data processing and analysis
- **Scikit-learn** for scaling and clustering
- **Streamlit** for the dashboard
- **Plotly** for interactive charts
- **Matplotlib** for data visualisations
- **Joblib** for saving and loading the trained model

## Project Structure

```text
Cluster-Matrix/
│
├── app.py
├── data/
│   └── Ecommerce.csv
│
├── data_analysis/
│   ├── inspect_data.py
│   ├── exploratory_analysis.py
│   ├── session_inspection.py
│   ├── customer_aggregation.py
│   ├── model_evaluation.py
│   ├── agglomerative_comparison.py
│   ├── final_validation.py
│   └── model_validation.py
│
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── outputs/
│   ├── graphs/
│   └── results/
│       └── customer_segments_final.csv
│
├── src/
│   ├── data_processing.py
│   └── train_model.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Running the Project

**1. Clone the repository**

```bash
git clone https://github.com/arishakhn-coder/Cluster-Matrix.git
cd Cluster-Matrix
```

**2. Install the required packages**

```bash
pip install -r requirements.txt
```

**3. Run the dashboard**

```bash
streamlit run app.py
```

Open the local URL shown in your terminal, usually:

```text
http://localhost:8501
```

**To train the model again:**

```bash
python src/train_model.py
```

The original dataset needs to be available at `data/Ecommerce.csv` for the training script and dashboard to work.

## Validation

I also checked the final output to make sure the customer records and model assignments were consistent.

- 8,442 unique customers in the original data.
- 8,442 customer records in the final output.
- No duplicate customer IDs.
- No missing values in the final customer dataset.
- All 8,442 cluster assignments matched when reproduced using the saved model.

This checks consistency on the same dataset. It does not measure performance on unseen customers.

## A Few Limitations

- The dataset contains simulated customer interactions.
- Cluster names are interpretations of the results, not confirmed customer types.
- The choice of three clusters prioritises interpretability over the best score on every metric.
- The results may differ when applied to a different dataset.

## Project Team

**Arisha Khanam**  
Data Analysis & Machine Learning

**Alveera Haidari**  
Dashboard Development & Business Intelligence

**Integral University**  
B.Tech, Computer Science and Engineering  
(Data Science & Artificial Intelligence)  
Academic Year: 2026–2027

---

*Built as an academic project to explore customer behaviour through data analysis, machine learning, and visualisation.*

**◈ Cluster Matrix**  
*Understand customers. Discover patterns. Find segments.*