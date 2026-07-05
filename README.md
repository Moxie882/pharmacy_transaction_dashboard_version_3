[![Hugging Face](https://img.shields.io/badge/View-Live_Demo-yellow)](https://huggingface.co/spaces/Moxie882/Build_Pharmacy_Transaction_Dashboard_3)

# pharmacy_transaction_dashboard_version_3

<!-- This project uses a dataset from a Sri Lankan pharmacy chain to create a dashboard and extract as many insights as possible from the data.
 -->
A dashboard built with Python and Panel that extracts insights from 'Pharmacy_OLTP_SLStyle_18Months.csv' dataset.

## 🔗 Live Demo
**Check out the live dashboard here:** 
https://huggingface.co/spaces/Moxie882/Build_Pharmacy_Transaction_Dashboard_3

## 🚀 Overview
I explored the dataset and built a dashboard used to explore multiple facets of the pharmacy chain.

## 📊 Key Features
- **Interactive Filters:** Specific branch of the pharmacy chain can be selected to show insights specific to that branch.
- **Visual Analytics:** Best five (5) Performing Drugs in Sales, Worst five (5) Performing Drugs in Sales
- **Data Driven:** Processed using Pandas to ensure efficient performance and accurate reporting.

## 🛠 Tech Stack
- **Dashboarding:** [Panel](https://panel.holoviz.org/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
- **Deployment:** [Hugging Face Spaces](https://huggingface.co/)

## 📂 Project Structure
```text
├── data/               # Raw and processed datasets
├── src/                # Source code
│   └── dashboard.py    # Main Panel application
├── notebooks/          # Exploratory analysis (Jupyter Notebooks)
├── requirements.txt    # Dependencies
└── README.md
```

## ⚙️ How to Run Locally
If you want to run the dashboard on your own machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Moxie882/pharmacy_transaction_dashboard_version_3.git
   cd pharmacy_transaction_dashboard_version_3

2. **Install the requirements:**
   ```bash
   pip install -r requirements.txt


3. **Launch the dashboard:**
   ```bash
   panel serve src/dashboard.py --show


## Dashboard Preview
   <img width="1366" height="592" alt="dashboard_preview" src="https://github.com/user-attachments/assets/caac74d0-e4ff-4c41-ac7d-b28fc301c263" />
