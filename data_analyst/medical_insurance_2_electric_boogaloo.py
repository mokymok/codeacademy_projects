# Create calculate_insurance_cost() function below: 
def calculate_insurance_costage(age,sex,bmi,num_of_children,smoker,name):
  estimated_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
  print("The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars.")
  return estimated_cost
# Initial variables for Maria 
m_age=28
m_sex=0  
m_bmi=26.2
m_num_of_children =3
m_smoker=0

# Estimate Maria's insurance cost
maria_insurance_cost=calculate_insurance_costage(28,0,26.2,3,0,"Maria")

# Initial variables for Omar
o_age=35
o_sex=1 
o_bmi=22.2
o_num_of_children=0
o_smoker=1  

# Estimate Omar's insurance cost 
omar_insurance_cost=calculate_insurance_costage(35,1,22.2,0,1,"Omar")
