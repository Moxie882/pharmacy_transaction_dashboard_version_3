[![Hugging Face](https://img.shields.io/badge/View-Live_Demo-yellow)](https://moxie882-build-pharmacy-transaction-dashboard-3.hf.space)

# pharmacy_transaction_dashboard_version_3

<!-- This project uses a dataset from a Sri Lankan pharmacy chain to create a dashboard and extract as many insights as possible from the data.
 -->
A dashboard built with Python and Panel that extracts insights from 'Pharmacy_OLTP_SLStyle_18Months.csv' dataset.

## 🔗 Live Demo
**Check out the live dashboard here:** 
https://moxie882-build-pharmacy-transaction-dashboard-3.hf.space

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
   <img width="1366" height="1238" alt="Screenshot_20260711-131431" src="https://github.com/user-attachments/assets/28dd8d66-d766-4aeb-8749-061d52ecd873" />
   <img width="1366" height="1185" alt="Screenshot_20260711-131446" src="https://github.com/user-attachments/assets/208cc723-2a38-4f2b-81e1-18b792f35a73" />
   <img width="1366" height="1187" alt="Screenshot_20260711-131456" src="https://github.com/user-attachments/assets/34dd91c7-ada2-4484-a541-2be12328eff8" />
   <img width="1366" height="1193" alt="Screenshot_20260711-131528" src="https://github.com/user-attachments/assets/54cc474a-8def-4aa0-8152-d83db5790fd5" />
   <img width="1366" height="1186" alt="Screenshot_20260711-131540" src="https://github.com/user-attachments/assets/c4ea6c61-9e39-4b49-be5f-57bf130d1dd7" />
   <img width="1366" height="1186" alt="Screenshot_20260711-131548" src="https://github.com/user-attachments/assets/8474636a-3fca-4491-a3e1-791c951aebbc" />
   <img width="1366" height="917" alt="Screenshot_20260711-131558" src="https://github.com/user-attachments/assets/26490cd4-6ec2-4248-b9d5-339dee35c405" />
   <img width="1366" height="933" alt="Screenshot_20260711-131606" src="https://github.com/user-attachments/assets/bdeadb1d-31e0-4106-bd2b-96a752ebd4d9" />
