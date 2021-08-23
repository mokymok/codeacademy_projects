import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files=glob.glob("states*.csv")
 
df_list=[]
for filename in files:df_list.append(pd.read_csv(filename))
census=pd.concat(df_list)
print(census.dtypes,census.columns,census.head(5))

census.Income=census.Income.replace('\$','',regex=True)
print(census.head(5))

gender_split=census.GenderPop.str.split('_')
census['Men']=gender_split.str.get(0)
census['Women']=gender_split.str.get(1)

census.Men=census.Men.str[:-1]
census.Women=census.Women.str[:-1]

census.Men=pd.to_numeric(census.Men)
census.Women=pd.to_numeric(census.Women)

census=census.fillna(value={'Women':census.TotalPop-census.Men})

census=census.drop_duplicates(subset=['State'])
print(census)

plt.scatter(census.Women,census.Income,color=['red','green'])
plt.xlabel('Women');plt.ylabel('Income');plt.show();plt.cla()

for i in['Hispanic','White','Black','Native','Asian','Pacific']:
  census[i]=census[i].str[:-1]
  census[i]=pd.to_numeric(census[i])
  census=census.fillna(value={i:census[i].mean()})
  plt.hist(census[i]);plt.title(i);plt.xlabel('Percentage');plt.ylabel('Num States');plt.show();plt.cla()
