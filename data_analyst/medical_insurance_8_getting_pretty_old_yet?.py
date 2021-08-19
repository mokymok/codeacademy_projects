# Add your code here
medical_costs={}
medical_costs["Marina"]=6607.0
medical_costs["Vinay"]=3225.0
medical_costs.update({"Connie":8886.0,"Isaac":16444.0,"Valentina":6420.0})
print(medical_costs,end='\n\n')
medical_costs["Vinay"]=3325.0
print(medical_costs,end='\n\n')
total_cost=0
for i in medical_costs.values():total_cost+=i
print(f"Average Insurance Cost: {total_cost/len(medical_costs)}\n")
names=[i for i in medical_costs.keys()]
ages=[27,24,43,35,52]
zipped_ages=zip(names,ages)
names_to_ages={i:j for i,j in zipped_ages}
# could also do //names_to_ages={i:j for i,j in zip([i for i in medical_costs.keys()],[27,24,43,35,52])}// to make it a one-liner instead of four
print(names_to_ages)
marina_age=names_to_ages.get("Marina",None)
print(f"Marina's age is {marina_age}\n")
medical_records={}
medical_records["Marina"]={"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.\n")
medical_records.pop("Vinay")
for i,j in medical_records.items():print(f"{i} is a {j['Age']} year old {j['Sex']} {j['Smoker']} with a BMI of {j['BMI']} and insurance cost of {j['Insurance_cost']}")
