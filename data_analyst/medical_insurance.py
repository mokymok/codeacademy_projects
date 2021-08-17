# create the initial variables below
age=28
sex=0
bmi=26.2
num_of_children=3
smoker=0
# Add insurance estimate formula below
insurance_cost=250*age-128*sex+370*bmi+435*num_of_children+24000*smoker-12500
print(f"This persons's insurance cost is {insurance_cost} dollars.")
# Age Factor
age+=4
new_insurance_cost=250*age-128*sex+370*bmi+435*num_of_children+24000*smoker-12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print(f'The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars.')
age=28
# BMI Factor
bmi+=3.1
new_insurance_cost=250*age-128*sex+370*bmi+435*num_of_children+24000*smoker-12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print(f'The change in cost of insurance after increasing the BMI by 3.1 years is {change_in_insurance_cost} dollars.')
bmi=26.2
# Male vs. Female Factor
sex=1
new_insurance_cost=250*age-128*sex+370*bmi+435*num_of_children+24000*smoker-12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print(f'The change in cost of insurance for being male instead of female is {change_in_insurance_cost} dollars.')
