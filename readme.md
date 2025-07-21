Customer Churn Prediction & Retention Analytics Project
Project Overview
Goal:
Build a realistic, end-to-end data analytics platform that predicts customer churn and helps understand customer behavior, using simulated data and real data engineering/analytics tools.
Why:
Retaining customers is cheaper than acquiring new ones.
Understanding churn helps improve products, services, and revenue.
This project demonstrates real-world data engineering and analytics skills.
Tools & Technologies Used
Python (pandas, numpy)
VS Code (or any code editor)
CSV files (for data storage and sharing)
SQL (for querying and analysis)

Project Steps & Explanations

1. Data Generation
   a. Customer Master Data
   What: Basic info for each customer (ID, name, age, gender, city, state, join date, type, status).
   Why: This is the main table that identifies every customer. All other data (usage, payment, etc.) is linked to these customers using their unique CustomerID.
   How: Used Python, pandas, and numpy to create 10,000 fake customers with realistic details. Saved as customer_master.csv.
   b. Usage/Activity Data
   What: Simulates how customers use services (date, service type, amount, session duration).
   Why: Usage patterns help identify at-risk (churning) customers.
   How: Used Python, pandas, and numpy to generate 50,000 random usage records, each linked to a customer. Saved as usage_data.csv.
   c. Payment/Billing Data
   What: Simulates billing and payment behavior (bill date, amount, payment status, payment date, method).
   Why: Payment issues are a major reason for churn.
   How: Used Python to generate 20,000 payment records, with logic for on-time, late, and missed payments. Saved as payment_data.csv.
   d. Support/Complaint Data
   What: Records of customer support or complaint tickets (customer, date, issue type, resolution time, satisfaction).
   Why: Helps understand if unhappy customers (many complaints or slow resolutions) are more likely to churn.
   How: Used Python to generate 8,000 support/complaint records, each linked to a customer. Saved as support_data.csv.
2. Data Cleaning & Integration
   How: Used pandas to read, clean, and merge data from CSV files.
   Why: Clean, integrated data is needed for accurate analysis.
3. Data Merging and Analysis
   What: Combined (merged) all the different data files—customer, usage, payment, and support—using the common column CustomerID.
   Why: Merging lets you analyze customer behavior across all aspects (usage, payment, support) together.
   How:
   Loaded all CSV files into pandas DataFrames.
   Merged usage, payment, and support data with customer data using CustomerID.
   Example analyses:
   Calculated average usage amount by payment status (Paid, Late, Missed).
   Counted the number of complaints per customer.
   Found the average number of complaints per customer.
   Merged complaints data with customer details to see which types of customers complain more.
   Saved merged and analyzed tables as new CSV files for further analysis.
