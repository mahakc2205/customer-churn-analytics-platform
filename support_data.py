import pandas as pd
import numpy as np
customer_df = pd.read_csv('customer_master.csv')
customer_ids = customer_df['CustomerID'].tolist()

n_records = 8000  # Number of support tickets to generate

issue_types = ['Login Issue', 'Payment Issue', 'Service Down', 'Account Blocked', 'Other']

support_data = {
    'CustomerID': np.random.choice(customer_ids, n_records),
    'TicketDate': pd.to_datetime(
        np.random.choice(pd.date_range('2021-01-01', '2021-12-31'), n_records)),
    'IssueType': np.random.choice(issue_types, n_records),
    'ResolutionTime': np.random.randint(1, 15, n_records),  # 1 to 14 days to resolve
    'SatisfactionScore': np.random.randint(1, 6, n_records)  # 1 (worst) to 5 (best)
}

support_df = pd.DataFrame(support_data)
print('Support data shape:', support_df.shape)
print('\nFirst 5 rows:')
print(support_df.head())

support_df.to_csv('support_data.csv', index=False)
print('\nData saved to support_data.csv')
