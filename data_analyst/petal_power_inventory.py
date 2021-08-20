import codecademylib
import pandas as pd

inventory=pd.read_csv('inventory.csv')
print(inventory.head(10))
staten_island=inventory.iloc[0:9]
product_request=staten_island['product_description']
seed_request=inventory[(inventory.product_type =='seeds')&(inventory.location =='Brooklyn')]
inventory['in_stock']=inventory.quantity.apply(lambda x:True if x>0else False)
inventory['total_value']=inventory.price*inventory.quantity
inventory['full_description']=inventory.apply(lambda row:'{} - {}'.format(row.product_type,row.product_description),axis=1)
print(inventory)
