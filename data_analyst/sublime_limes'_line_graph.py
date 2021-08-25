import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12,8))
plt.show()
ax1=plt.subplot(1,2,1)
x_vals=range(len(months))
plt.plot(x_vals,visits_per_month,marker='o')
plt.xlabel('months')
plt.ylabel('visits')
ax1.set_xticks(x_vals)
ax1.set_xticklabels(months)
plt.title('visits per month')
ax2=plt.subplot(1,2,2)
plt.plot(x_vals,key_limes_per_month,color='green',marker='o')
plt.plot(x_vals,persian_limes_per_month,color='blue',marker='o')
plt.plot(x_vals,blood_limes_per_month,color='red',marker='o')
plt.legend(['key limes','persian limes','blood limes'],loc=1)
ax2.set_xticks(x_vals)
ax2.set_xticklabels(months)
plt.xlabel('months')
plt.ylabel('limes sold')
plt.title('limes sold per month')
plt.show()
plt.savefig('funny_lime_pic.png')
