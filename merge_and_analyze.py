import pandas as pd
customer_df=pd.read_csv('customer_master.csv')
payment_df=pd.read_csv('payment_data.csv')
support_df=pd.read_csv('support_data.csv')
usage_df=pd.read_csv('usage_data.csv')
usage_merged=pd.merge(usage_df,customer_df,on='CustomerID',how='left')
payment_merged=pd.merge(payment_df,customer_df,on='CustomerID',how='left')
support_merged=pd.merge(support_df,customer_df,on='CustomerID',how='left')
#Average usage amount by payment status
usage_payment = pd.merge(usage_df, payment_df[['CustomerID', 'PaymentStatus']], on='CustomerID', how='left')
print(usage_payment.groupby('PaymentStatus')['UsageAmount'].mean())
#no of complaints per customer
complaints_per_customer=support_df.groupby('CustomerID').size().reset_index(name='NumComplaints')
print(complaints_per_customer.head())
usage_merged.to_csv('usage_with_customer.csv', index=False)
payment_merged.to_csv('payment_with_customer.csv', index=False)
support_merged.to_csv('support_with_customer.csv', index=False)
complaints_per_customer.to_csv('complaints_per_customer.csv', index=False)
#find customer with most complaints
print(complaints_per_customer.sort_values('NumComplaints', ascending=False).head(10))
#find average complaints per customer
print(complaints_per_customer['NumComplaints'].mean())

complaints_merged = pd.merge(complaints_per_customer, customer_df, how='left')
print(complaints_merged.head())


