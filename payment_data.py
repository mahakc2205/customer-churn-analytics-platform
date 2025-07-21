import pandas as pd
import numpy as np
customer_df=pd.read_csv('customer_master.csv')
customer_ids=customer_df['CustomerID'].to_list()
n_records=20000
payment_status=['Paid','Late','Missed']
payment_methods=['Card','UPI','Net Banking','Wallet']
payment_data={
    'CustomerID':np.random.choice(customer_ids,n_records),
    'BillDate': pd.to_datetime(np.random.choice(pd.date_range('2021-01-01', '2021-12-31'), n_records)),
    'Amount': np.round(np.random.uniform(500, 20000, n_records), 2),
    'PaymentStatus': np.random.choice(payment_status, n_records, p=[0.7, 0.2, 0.1]),  # 70% Paid, 20% Late, 10% Missed
    'PaymentMethod': np.random.choice(payment_methods, n_records)
}

payment_dates=[]

for status, bill_date in zip(payment_data['PaymentStatus'], payment_data['BillDate']):
        if status == 'Paid':
              payment_dates.append(bill_date + pd.Timedelta(days=np.random.randint(0, 6)))
        elif status == 'Late':
              payment_dates.append(bill_date + pd.Timedelta(days=np.random.randint(6, 21)))
        else:
              payment_dates.append(pd.NaT)


payment_data['PaymentDate']=payment_dates
payment_df=pd.DataFrame(payment_data)
print("Payment data shape:", payment_df.shape)
print("\nFirst 5 rows:")
print(payment_df.head())
payment_df.to_csv('payment_data.csv', index=False)
print("\nData saved to payment_data.csv")
