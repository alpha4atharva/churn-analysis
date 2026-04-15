# 📊 Customer Churn Analysis Project

A comprehensive data science project to understand and predict customer churn using advanced analytics, machine learning, and model interpretation techniques.

---

## 📌 Project Overview

This project analyzes customer churn patterns by examining call center interactions, billing history, customer support records, and email communications. The goal is to:

- **Understand** why customers churn
- **Identify** key churn drivers and patterns
- **Predict** which customers are likely to churn
- **Interpret** model decisions for actionable insights

---

## 📂 Data Architecture

### Datasets
| Dataset | Description | Records | Size |
|---------|-------------|---------|------|
| `renewal_calls.csv` | Renewal call transcripts, churn reasons, complaints | ~186K | ~50 MB |
| `billings.csv` | Customer billing & payment history | ~43K | ~43 MB |
| `cc_calls.csv` | Customer care/support call records | ~15K | ~5 MB |
| `emails.csv` | Customer email communications | ~25K | ~20 MB |

**Key Link:** All datasets use `Co_Ref` (Customer Reference ID) as the primary key.

### Data Directory Structure
```
data/
├── raw/                          # Original datasets (immutable)
│   ├── billings.csv
│   ├── cc_calls.csv
│   ├── emails.csv
│   └── renewal_calls.csv
├── cleaned/                       # Cleaned & processed datasets
│   ├── billings_cleaned.csv
│   ├── cc_calls_cleaned.csv
│   ├── emails_cleaned.csv
│   └── renewal_calls_cleaned.csv
├── merged/                        # Aggregated datasets
│   └── churn_dataset_merged.csv
├── ml_data/                       # ML-ready features
│   ├── features.csv
│   └── churn_labels.csv
└── powerbi_export/                # BI/Reporting exports
```

---

## 🔄 Pipeline Workflow

The project follows a **systematic 8-stage pipeline** executed sequentially:

### Stage Breakdown

```
┌─────────────────────────────────────────────────────────────┐
│                   CHURN ANALYSIS PIPELINE                    │
└─────────────────────────────────────────────────────────────┘

[1] DATA UNDERSTANDING
    └─ Explore raw datasets
    └─ Check distributions, missing values
    └─ Document data quality issues
    └─ Output: data_understanding.ipynb

[2] DATA CLEANING (4 notebooks, parallel processing friendly)
    ├─ billings_cleaning.ipynb → Clean billing data
    ├─ cc_calls_cleaning.ipynb → Clean support call data
    ├─ emails_cleaning.ipynb → Clean email data
    └─ renewal_calls_cleaning.ipynb → Clean renewal call data
    └─ Output: data/cleaned/

[3] DATA MERGING & AGGREGATION
    └─ Merge all cleaned datasets by Co_Ref
    └─ Aggregate metrics (call counts, email frequency, etc.)
    └─ Output: data/merged/churn_dataset_merged.csv

[4] EXPLORATORY DATA ANALYSIS (4 notebooks)
    ├─ billings_eda.ipynb → Billing trends & patterns
    ├─ cc_calls_eda.ipynb → Support interaction analysis
    ├─ emails_eda.ipynb → Email communication patterns
    └─ renewal_calls_eda.ipynb → Churn reason analysis
    └─ Output: reports/figures/

[5] FEATURE ENGINEERING
    └─ Create derived features
    └─ Handle categorical encoding
    └─ Feature scaling & normalization
    └─ Output: data/ml_data/features.csv

[6] HYPOTHESIS TESTING & STATISTICAL ANALYSIS
    └─ Test churn drivers (Chi-square, t-tests)
    └─ Correlation analysis
    └─ Statistical significance reporting
    └─ Output: reports/hypothesis_testing_results.html

[7] MODEL BUILDING & EVALUATION
    └─ Train classification models:
       ├─ Logistic Regression
       ├─ Random Forest
       ├─ XGBoost
       └─ LightGBM
    └─ Cross-validation & hyperparameter tuning
    └─ Evaluation: Accuracy, Precision, Recall, AUC-ROC
    └─ Output: models/, reports/model_comparison.html

[8] MODEL INTERPRETATION & EXPLAINABILITY
    └─ SHAP feature importance
    └─ LIME local explanations
    └─ Partial dependence plots
    └─ Decision tree visualization
    └─ Output: reports/explainability_report.html

└─ FINAL OUTPUT: Predictions + Actionable Insights
```

---

## 🚀 Quick Start

### 1. Clone & Setup

```bash
# Clone the repository
git clone <repo-url>
cd churn-analysis

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate         # Windows
# or
source venv/bin/activate      # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Full Pipeline

```bash
# Execute entire analysis workflow
python run_pipeline.py
```

**Output:**
```
[1/8] Running notebooks/01_data_undestanding/data_understanding.ipynb...
[2/8] Running notebooks/02_data_cleaning/billings_cleaning.ipynb...
[3/8] Running notebooks/02_data_cleaning/cc_calls_cleaning.ipynb...
...
✓ Pipeline completed successfully!
```

### 4. Run Individual Stages

```bash
# Data understanding only
jupyter notebook notebooks/01_data_undestanding/data_understanding.ipynb

# Data cleaning (choose specific dataset)
jupyter notebook notebooks/02_data_cleaning/billings_cleaning.ipynb

# Model building
jupyter notebook notebooks/07_model_building_evaluation/model_build_eval.ipynb
```

---

## 📓 Notebook Directory

### Stage 1: Data Understanding
- **File:** `notebooks/01_data_undestanding/data_understanding.ipynb`
- **Purpose:** Load, inspect, and document all raw datasets
- **Outputs:** Data quality report, missing value summary, distribution analysis

### Stage 2: Data Cleaning (4 notebooks)
| Notebook | Dataset | Tasks |
|----------|---------|-------|
| `billings_cleaning.ipynb` | billings.csv | Handle nulls, outliers, date parsing |
| `cc_calls_cleaning.ipynb` | cc_calls.csv | Clean duration, timestamps |
| `emails_cleaning.ipynb` | emails.csv | Process text, remove duplicates |
| `renewal_calls_cleaning.ipynb` | renewal_calls.csv | Extract churn reasons, sentiment |

### Stage 3: Data Merging
- **File:** `notebooks/03_data_merging/aggregation_merging.ipynb`
- **Purpose:** Combine all cleaned datasets and create aggregate features

### Stage 4: EDA & Visualization (4 notebooks)
| Notebook | Focus | Key Visualizations |
|----------|-------|-------------------|
| `billings_eda.ipynb` | Revenue trends | Revenue by churn, payment patterns |
| `cc_calls_eda.ipynb` | Support interactions | Call frequency, resolution time |
| `emails_eda.ipynb` | Communication | Email volume, response rates |
| `renewal_calls_eda.ipynb` | Churn analysis | Churn reasons, keywords, sentiment |

### Stage 5: Feature Engineering
- **File:** `notebooks/05_feature_engineering/feature_engineering.ipynb`
- **Features Created:**
  - Behavioral: call frequency, email volume, payment delays
  - Engagement: support interaction recency, complaint sentiment
  - Financial: revenue trends, payment reliability scores

### Stage 6: Hypothesis Testing
- **File:** `notebooks/06_hypothesis_testing/hypothesis_testing.ipynb`
- **Tests:**
  - Do churned customers have more support calls?
  - Is payment delay correlated with churn?
  - Do specific renewal call keywords predict churn?

### Stage 7: Model Building & Evaluation
- **File:** `notebooks/07_model_building_evaluation/model_build_eval.ipynb`
- **Models:** Logistic Regression, Random Forest, XGBoost, LightGBM
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1, AUC-ROC

### Stage 8: Model Interpretation
- **File:** `notebooks/08_model_interpretation/explainability.ipynb`
- **Techniques:** SHAP, LIME, Permutation Importance, Partial Dependence

---

## 🛠 Technology Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.8+ |
| **Data Processing** | pandas, numpy, scipy |
| **Visualization** | matplotlib, seaborn, plotly |
| **Machine Learning** | scikit-learn, XGBoost, LightGBM |
| **Model Interpretation** | SHAP, LIME |
| **Notebooks** | Jupyter, nbconvert |
| **Orchestration** | Python subprocess |

---

## 📋 Requirements

See `requirements.txt` for full list:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
scipy>=1.7.0
xgboost>=1.5.0
lightgbm>=3.3.0
shap>=0.40.0
joblib>=1.0.0
jupyter>=1.0.0
nbconvert>=6.0.0
```

### Installation
```bash
pip install -r requirements.txt
```

---

## 📊 Expected Outputs

After running the full pipeline:

```
reports/
├── hypothesis_testing_results.html    # Statistical test results
├── model_comparison.html              # Model performance comparison
├── explainability_report.html         # Feature importance & SHAP plots
└── figures/
    ├── churn_distribution.png
    ├── feature_importance.png
    ├── confusion_matrices.png
    └── shap_summary_plots.png

models/
├── logistic_regression_model.pkl
├── random_forest_model.pkl
├── xgboost_model.pkl
└── lightgbm_model.pkl

data/ml_data/
├── features.csv                       # Final features for modeling
└── predictions.csv                    # Model predictions
```

---

## 💡 Key Findings (Template)

### Churn Drivers Identified
1. **High Support Call Frequency** - Customers with >5 support calls have 3x higher churn rate
2. **Payment Delays** - Average 2-week delay correlates with churn
3. **Negative Sentiment in Renewal Calls** - "Competitor mentioned" keywords predict churn
4. **Communication Gap** - Low email engagement after billing events

### Model Performance
- **Best Model:** LightGBM
- **AUC-ROC:** 0.87
- **Precision:** 0.84 (fewer false alarms)
- **Recall:** 0.79 (catches most churners)

### Recommendations
1. Proactive outreach after support incident #3
2. Payment delay intervention within 7 days
3. Win-back campaigns for competitor-mentioned customers
4. Engagement campaigns during low-email periods

---

## 📁 Project Structure

```
churn-analysis/
├── README.md                          # This file
├── run_pipeline.py                    # Orchestration script
├── requirements.txt                   # Dependencies
│
├── data/
│   ├── raw/                          # Original datasets
│   ├── cleaned/                       # Cleaned datasets
│   ├── merged/                        # Merged datasets
│   ├── ml_data/                       # ML-ready features
│   └── powerbi_export/                # BI exports
│
├── notebooks/
│   ├── 01_data_undestanding/
│   │   └── data_understanding.ipynb
│   ├── 02_data_cleaning/
│   │   ├── billings_cleaning.ipynb
│   │   ├── cc_calls_cleaning.ipynb
│   │   ├── emails_cleaning.ipynb
│   │   └── renewal_calls_cleaning.ipynb
│   ├── 03_data_merging/
│   │   └── aggregation_merging.ipynb
│   ├── 04_eda_visualization/
│   │   ├── billings_eda.ipynb
│   │   ├── cc_calls_eda.ipynb
│   │   ├── emails_eda.ipynb
│   │   └── renewal_calls_eda.ipynb
│   ├── 05_feature_engineering/
│   │   └── feature_engineering.ipynb
│   ├── 06_hypothesis_testing/
│   │   └── hypothesis_testing.ipynb
│   ├── 07_model_building_evaluation/
│   │   └── model_build_eval.ipynb
│   └── 08_model_interpretation/
│       └── explainability.ipynb
│
├── models/                            # Trained model artifacts
├── reports/                           # Analysis reports & visualizations
└── figures/                           # Charts & graphs
```

---

## 🔐 How run_pipeline.py Works

The orchestration script automates the entire analysis workflow:

```python
# Sequential execution of all stages
python run_pipeline.py

# Features:
# ✓ Runs each notebook in order
# ✓ Stops if any stage fails
# ✓ Shows progress: [1/8], [2/8], etc.
# ✓ Saves execution logs
```

### Manual Stage Execution

If you prefer manual control:

```bash
# Run individual stage
jupyter notebook notebooks/01_data_undestanding/data_understanding.ipynb

# Or execute and save
jupyter nbconvert --to notebook --execute notebooks/02_data_cleaning/billings_cleaning.ipynb
```

---

## 🤝 Contributing

### Workflow
1. Create a new branch: `git checkout -b feature/your-analysis`
2. Make changes to relevant notebooks
3. Test the pipeline: `python run_pipeline.py`
4. Commit and push: `git push origin feature/your-analysis`
5. Create a Pull Request

### Guidelines
- Keep notebooks focused on one task
- Add markdown comments explaining analysis steps
- Include visualizations with interpretations
- Save intermediate outputs to `data/` directory
- Update this README if adding new stages

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: jupyter"
```bash
pip install jupyter nbconvert
```

### Issue: Pipeline stops at specific notebook
1. Check the notebook manually: `jupyter notebook notebooks/XX_stage_name/`
2. Look for cell errors
3. Fix the issue and re-run: `python run_pipeline.py`

### Issue: Memory error on large datasets
- Process datasets in chunks within notebooks
- Increase system RAM or use distributed processing
- Filter unnecessary columns early

### Issue: Missing data files
- Ensure `data/raw/` contains all 4 CSV files
- Check file permissions
- Verify file paths in notebooks use relative paths

---

## 📄 License

This project is confidential and for internal use only.

---

## ✅ Checklist for Running Analysis

- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install requirements: `pip install -r requirements.txt`
- [ ] Verify `data/raw/` contains all 4 CSV files
- [ ] Run pipeline: `python run_pipeline.py`
- [ ] Review outputs in `reports/` and `models/`
- [ ] Check visualizations in `reports/figures/`
- [ ] Document findings and recommendations

---

**Happy analyzing! 🚀**
