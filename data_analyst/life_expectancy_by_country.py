import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
print(data.head())

life_expec=data['Life Expectancy']
life_expec_quarts=np.quantile(life_expec,[.25,.5,.75])
# print(life_expec_quarts)
plt.hist(life_expec,bins=40)
plt.show();plt.clf()

gdp=data.GDP
gdp_med=np.quantile(gdp,.5)
# print(gdp_med)
low_gdp=data[data.GDP<=gdp_med]
high_gdp=data[data.GDP>gdp_med]

low_gdp_quarts=np.quantile(low_gdp['Life Expectancy'],[.25,.5,.75])
high_gdp_quarts=np.quantile(high_gdp['Life Expectancy'],[.25,.5,.75])
plt.hist(high_gdp['Life Expectancy'],alpha=.5,label='high gdp')
plt.hist(low_gdp['Life Expectancy'],alpha=.5,label='low gdp')
plt.legend()
plt.show()
