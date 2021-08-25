import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts=nba_2010.pts[nba.fran_id=='Knicks']
nets_pts=nba_2010.pts[nba.fran_id=='Nets']

diff_means_2010=np.mean(knicks_pts)-np.mean(nets_pts)

plt.hist(knicks_pts,alpha=0.8,normed=True,label='knicks')
plt.hist(nets_pts,alpha=0.8,normed=True,label='nets')
plt.legend()
plt.show();plt.clf()

knicks_pts_14=nba_2014.pts[nba.fran_id=='Knicks']
nets_pts_14=nba_2014.pts[nba.fran_id=='Nets']

diff_means_2014=np.mean(knicks_pts_14)-np.mean(nets_pts_14)
print(diff_means_2010,diff_means_2014)
plt.hist(knicks_pts_14,alpha=0.8,normed=True,label='knicks')
plt.hist(nets_pts_14,alpha=0.8,normed=True,label='nets')
plt.legend()
plt.show();plt.clf()

sns.boxplot(data=nba_2010,x='fran_id',y='pts')
plt.show();plt.clf()

loc_res_freq=pd.crosstab(nba_2010.game_result,nba_2010.game_location)
print(loc_res_freq)

loc_res_prop=loc_res_freq/len(nba_2010)
print(loc_res_prop)

chi2,pval,dof,expected=chi2_contingency(loc_res_prop)
print(expected)

cov_2010=np.cov(nba_2010.forecast,nba_2010.point_diff)
print(cov_2010)

corr_2010,p=pearsonr(nba_2010.forecast,nba_2010.point_diff)
print(corr_2010)

plt.scatter('forecast','point_diff',data=nba_2010)
plt.xlabel('forecasted win probability')
plt.ylabel('point differential')
plt.show()
