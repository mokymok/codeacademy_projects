import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
# print(healthcare.head())
# print(healthcare['DRG Definition'].unique())
chest_pain=healthcare[healthcare['DRG Definition']=='313 - CHEST PAIN']
alabama_chest_pain=chest_pain[chest_pain['Provider State']=='AL']
costs=alabama_chest_pain[' Average Covered Charges '].values

# plt.boxplot(costs)
# plt.show()

states=chest_pain['Provider State'].unique()
data=[]
for state in states:
  data.append(chest_pain[chest_pain['Provider State']==state][' Average Covered Charges '].values)
plt.figure(figsize=(20,6))
plt.boxplot(data,labels=states)
plt.show()
