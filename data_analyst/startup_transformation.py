import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
fin_data = pd.read_csv('financial_data.csv')

# code goes here
print(fin_data.head())

month=fin_data.Month
revenue=fin_data.Revenue
expenses=fin_data.Expenses


plt.plot(month,revenue);plt.xlabel('month');plt.ylabel('amount ($)');plt.title('revenue');plt.tight_layout();plt.show();plt.clf()
plt.plot(month,expenses);plt.xlabel('month');plt.ylabel('amount ($)');plt.title('expenses');plt.show();plt.clf()

expense_overview=pd.read_csv('expenses.csv')
print(expense_overview.head(7))
exp_cat=expense_overview.Expense
exp_prop=expense_overview.Proportion

plt.axis('Equal');plt.pie(exp_prop,labels=exp_cat);plt.title('expense categories');plt.show();plt.clf()

exp_cat=['Salaries','Advertising','Office Rent','Other']
exp_prop=[0.62,0.15,0.15,0.08]

plt.axis('Equal');plt.pie(exp_prop,labels=exp_cat);plt.title('expense categories');plt.show();plt.clf()
expense_cut='Salaries'

emp=pd.read_csv('employees.csv')
print(emp.head())

sort_emp=emp.sort_values(by=['Productivity'])
print(sort_emp)

cut_emp=sort_emp.head(100)
print(cut_emp)

transformation='standardization'

commute_times=emp['Commute Time']
commute_times_log=np.log(commute_times)
print(commute_times,commute_times.describe())

plt.hist(commute_times);plt.xlabel('minutes');plt.ylabel('number employees');plt.title('commute time frequency');plt.show();plt.clf()
plt.hist(commute_times_log);plt.ylabel('number employees');plt.title('commute time frequency (logarithmic)');plt.show()
