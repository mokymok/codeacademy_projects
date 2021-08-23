import codecademylib
import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))

views=ad_clicks.groupby('utm_source').nunique()
print(views)

ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source=ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot=clicks_by_source.pivot(index='utm_source',columns='is_click',values='user_id').reset_index()
clicks_pivot['percent_clicked']=(clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False]))*100
print(clicks_pivot)

clicks_experimental=ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(clicks_experimental)

a_clicks=ad_clicks[ad_clicks.experimental_group== 'A']
b_clicks=ad_clicks[ad_clicks.experimental_group== 'B']

a_clicks_by_day=a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
a_clicks_pivot=a_clicks_by_day.pivot(index='day',columns='is_click',values='user_id').reset_index()
a_clicks_pivot['percent_clicked']=(a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False]))*100
print(a_clicks_pivot)

b_clicks_by_day=b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_clicks_pivot=b_clicks_by_day.pivot(index='day',columns='is_click',values='user_id').reset_index()
b_clicks_pivot['percent_clicked']=(b_clicks_pivot[True]/(b_clicks_pivot[True]+b_clicks_pivot[False]))*100
print(b_clicks_pivot)
