import pandas as pd
import numpy as np
from datetime import datetime ,timedelta
np.random.seed(42)
n_customers=10000
def generate_customer_data():
    customer_ids=[f'CUST{i:05d}'for i in range (1,n_customers+1)]
    names=['Ankit','Priya','Rahul','Neha','Amit', 'Sneha', 'Vikram', 'Pooja', 'Raj', 'Meera']
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']
    states = ['MH', 'DL', 'KA', 'TN', 'WB', 'TG', 'MH', 'GJ']
    data={
        'CustomerID':customer_ids,
        'Name':np.random.choice(names,n_customers),
        'Age':np.random.randint(18,65,n_customers),
        'Gender': np.random.choice(['M', 'F'], n_customers),
        'City':np.random.choice(cities,n_customers),
        'States':np.random.choice(states,n_customers),
        'JointDate':pd.date_range('2022-01-01',periods=n_customers,freq='D'),
        'CustomerType':np.random.choice(['Premium','Regular'],n_customers,p=[0.2,0.8]),
        'Status':['Active']*n_customers
    
    }
    return pd.DataFrame(data)

customer_df=generate_customer_data()
print('Customer data shape :',customer_df.shape)
print("\nFirst 5 rows :")
print(customer_df.head())
customer_df.to_csv('customer_master.csv',index=False)
print("\nData saved to customer_master.csv")





