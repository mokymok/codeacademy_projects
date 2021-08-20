import codecademylib3_seaborn
from bs4 import BeautifulSoup as bs
import requests as r
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

req=r.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
doc=req.content
soup=bs(doc,'html.parser')
print(soup)

ratings=[]
rating=soup.find_all(attrs={'class':'Rating'})
for i in rating[1:]:
  i=float(i.get_text());ratings.append(i)
plt.hist(ratings)
plt.show()

company=soup.select('.Company')
companies=[]
for i in company[1:]:
  companies.append(i.get_text())

cocoperc=soup.select('.CocoaPercent')
cocoa=[]
for i in cocoperc[1:]:
  cocoa.append(float(i.get_text().strip('%')))

d={'Company':companies,'Rating':ratings,'CocoaPercentage':cocoa}
df=pd.DataFrame.from_dict(d)
mean=df.groupby('Company').Rating.mean()
top_ten=mean.nlargest(10)
print(top_ten)

plt.clf()
plt.scatter(df.CocoaPercentage,df.Rating)
z=np.polyfit(df.CocoaPercentage,df.Rating,1)
line_func=np.poly1d(z)
plt.plot(df.CocoaPercentage,line_func(df.CocoaPercentage),"r--")
plt.show()
