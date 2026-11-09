# ◈ Cluster Matrix
### E-Commerce Customer Intelligence & Behavioural Segmentation

**Understand customers. Discover patterns. Find segments.**

Cluster Matrix is a machine learning project that explores e-commerce customer behaviour through data analysis and clustering. It groups customers based on their shopping activity and engagement patterns, helping identify meaningful customer segments.

**🚀 Live Dashboard:** [Launch Cluster Matrix](https://cluster-matrix.streamlit.app/)

---

## Dashboard Preview

![Cluster Matrix Dashboard](assets/dashboard_preview.png)

---

## ✦ Project Overview

The project uses customer interaction data to understand how customers browse, engage with products, add items to their carts, and make purchases.

The workflow includes:

- Data cleaning and exploratory data analysis
- Customer-level feature aggregation
- Feature scaling and K-Means clustering
- Model evaluation and comparison
- Interactive dashboard development
- Business insights and recommendations

## 📊 Dataset

**Dataset:** [Indian E-Commerce Customer Behavior & Purchase](https://www.kaggle.com/datasets/kundanbedmutha/indian-e-commerce-customer-behavior-and-purchase)  
**Creator:** Kundan Bedmutha

The dataset contains 25,000 simulated e-commerce session records and 29 columns. After grouping session records by customer, the project produces a customer-level dataset containing **8,442 unique customers**.

The original dataset is not included in this repository. To run the training pipeline, download it from Kaggle and place `Ecommerce.csv` inside the `data/` folder.

## ⚙️ Methodology

### Customer Aggregation

Session-level records are grouped by customer to calculate features such as:

- Total sessions
- Total purchases
- Total revenue
- Average pages viewed
- Average time spent on the website
- Total cart additions
- Total cart abandonments

### Customer Segmentation

K-Means clustering is applied using five selected features:

1. Total sessions
2. Total revenue
3. Average pages viewed
4. Average time on site
5. Total cart additions

The features are standardised using `StandardScaler` before clustering.

The final dashboard uses **three customer segments**, containing all 8,442 customers.

### Model Evaluation

The model selection process considers:

- Elbow Method
- Silhouette Score
- Davies-Bouldin Index
- PCA-based cluster visualisation
- Comparison with Agglomerative Clustering

Three clusters were selected as a practical and interpretable choice. They were not the best-performing option across every evaluation metric.

## 🔍 Customer Segments

The three clusters show different patterns in customer activity and purchase behaviour.

| Segment | Observed pattern |
|---|---|
| Cluster 0 | Lower revenue, fewer sessions, longer average time on site |
| Cluster 1 | Higher revenue, more sessions, more cart additions |
| Cluster 2 | Lower revenue, fewer sessions, shorter average time on site |

These descriptions are based on cluster averages. They are interpretations of the data, not fixed labels for individual customers.

## 🖥️ Dashboard Sections

The Streamlit dashboard contains six main sections:

| Section | Purpose |
|---|---|
| Command Center | Customer and revenue snapshot |
| Segment Intelligence | Cluster distribution and comparison |
| Model Studio | Model configuration and evaluation |
| Customer Directory | Customer-level search and filtering |
| Strategic Insights | Findings and business recommendations |
| Project Team | Project contributors |

## 🛠️ Technology Stack

- **Python** for data processing and machine learning
- **Pandas** for data manipulation
- **Scikit-learn** for scaling and clustering
- **Matplotlib & Seaborn** for analysis visualisations
- **Plotly** for interactive charts
- **Streamlit** for the dashboard
- **Git & GitHub** for version control

## 📁 Project Structure

```text
Cluster-Matrix/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── dashboard_preview.png
│
├── data/
│   └── (Place Ecommerce.csv here after downloading)
│
├── data_analysis/
│   ├── customer_aggregation.py
│   ├── exploratory_analysis.py
│   ├── model_evaluation.py
│   ├── model_validation.py
│   └── agglomerative_comparison.py
│
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── outputs/
│   ├── graphs/
│   └── results/
│
└── src/
    ├── data_processing.py
    └── train_model.py
```

*Note: The raw dataset is kept locally and excluded from GitHub. The `data/` folder may need to be created after downloading the dataset.*

## ▶️ Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/arishakhn-coder/Cluster-Matrix.git
cd Cluster-Matrix
```

**2. Install the dependencies**


pip install -r requirements.txt


**3. Add the dataset**

Place `Ecommerce.csv` inside the `data/` folder.

**4. Run the dashboard**


streamlit run app.py


## 📌 Limitations

- The dataset contains simulated customer interactions.
- Cluster descriptions are interpretations based on average feature values.
- Three clusters were selected with interpretability in mind, rather than being optimal across every evaluation metric.
- Results may differ when applied to real-world or different customer datasets.

## 👥 Project Team

**Arisha Khanam**  
Data Analysis & Machine Learning

**Alveera Haidari**  
Dashboard Development & Business Intelligence

**Integral University**  
B.Tech, Computer Science and Engineering  
(Data Science & Artificial Intelligence)  
Academic Year: 2026–2027

---

<div align="center">

### ◈ Cluster Matrix

*Understand customers. Discover patterns. Find segments.*

</div>