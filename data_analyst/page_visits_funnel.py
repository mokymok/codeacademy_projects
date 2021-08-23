import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',parse_dates=[1])
cart = pd.read_csv('cart.csv',parse_dates=[1])
checkout = pd.read_csv('checkout.csv',parse_dates=[1])
purchase = pd.read_csv('purchase.csv',parse_dates=[1])
print(visits.head(5),cart.head(5),checkout.head(5),purchase.head(5))

visit_cart=pd.merge(visits,cart,how='left')
total_cust=len(visit_cart)
print(total_cust)

is_null=len(visit_cart[visit_cart.cart_time.isnull()])
print(is_null)

percent_not_buying=(is_null/float(total_cust))*100
print(percent_not_buying)

checkout_cart=pd.merge(checkout,cart,how='right')
checkout_null=len(checkout_cart[checkout_cart.checkout_time.isnull()])
print(checkout_null)

all_data=visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head(5))

total_checkout_no_purchase=100-((len(all_data[~all_data.purchase_time.isnull()])/float(len(all_data[~all_data.checkout_time.isnull()])))*100)
print(total_checkout_no_purchase)

all_data['time_to_purchase']=all_data.purchase_time-all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
