import pandas as pd
import numpy as np

car_eval=pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

country_freq=car_eval.manufacturer_country.value_counts()
fourth_freq_country=country_freq.index[4]
print(fourth_freq_country)

country_prop=car_eval.manufacturer_country.value_counts(normalize=True)
japan_prop=country_prop['Japan']
print(japan_prop)

print(car_eval.buying_cost.unique())

buying_cost_cats=['low','med','high','vhigh']
car_eval.buying_cost=pd.Categorical(car_eval.buying_cost,buying_cost_cats,ordered=True)

med_cat_cost=np.median(car_eval.buying_cost.cat.codes)
print(med_cat_cost)

luggage_prop=car_eval.luggage.value_counts(normalize=True)
print(luggage_prop)

luggage_prop_2=car_eval.luggage.value_counts(dropna=False,normalize=True)
print(luggage_prop_2)

print(car_eval.luggage.value_counts(dropna=False)/len(car_eval.luggage))

frequency=(car_eval.doors=='5more').sum()
print(frequency)
proportion=(car_eval.doors=='5more').mean()
print(proportion)
