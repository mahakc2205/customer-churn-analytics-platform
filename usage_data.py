import pandas as pd
import numpy as np
customer_df=pd.read_csv('customer_master.csv')
customers_ids=customer_df['CustomerID'].to_list()
n_records=50000
services=['Mobile App','Website','ATM','Branch Visit']
usage_data={
    'CustomerID':np.random.choice(customers_ids,n_records),
    'ActivityDate':pd.to_datetime(np.random.choice(pd.date_range('2021-01-01','2021-12-31'),n_records)),
    'ServiceUsed':np.random.choice(services,n_records),
    'UsageAmount':np.round(np.random.uniform(100,10000,n_records),2),
    'SessionDuration':np.round(np.random.uniform(1,60,n_records),2)

}
usage_df=pd.DataFrame(usage_data)
print("Usage data shape :-",usage_df.shape)
print("\nFirst 5 rows :")
print(usage_df.head())

usage_df.to_csv('usage_data.csv',index=False) 
#Why use index=False?
# index=False tells pandas NOT to write the row numbers (index) into the CSV file.
# This keeps your CSV file clean, with only your actual data columns.
print('\nData saved to usage_data.csv')
