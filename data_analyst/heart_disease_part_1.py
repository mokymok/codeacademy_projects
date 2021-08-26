# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
# print(chol_hd)
mean_chol_hd = np.mean(chol_hd)
# print(mean_chol_hd)

t_stat, pval = ttest_1samp(chol_hd, 240)
pval = pval / 2
# print(pval)

chol_no_hd = no_hd.chol
# print(chol_no_hd)
mean_chol_no_hd = np.mean(chol_no_hd)
# print(mean_chol_no_hd)

t_stat, pval = ttest_1samp(chol_no_hd, 240)
pval = pval / 2
# print(pval)

num_patients = len(heart)
# print(num_patients)

num_highfbs_patients = len(heart[heart.fbs == 1])
# print(num_highfbs_patients)

num_diabetes = 0.08 * num_patients
# print(num_diabetes) 

pval = binom_test(num_highfbs_patients, n = num_patients, p = 0.08, alternative = 'greater')
print(pval)
