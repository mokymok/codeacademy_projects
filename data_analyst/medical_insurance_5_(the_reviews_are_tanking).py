names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)
medical_records=list(zip(insurance_costs,names))
print(medical_records)
num_medical_records=len(medical_records)
print(f"There are {num_medical_records} medical records.")
first_medical_record=medical_records[0]
print(f"Here is the first medical record: {first_medical_record}")
print(f"Here are the medical records sorted by insurance cost: {sorted(medical_records)}")
cheapest_three=sorted(medical_records)[0:3]
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}")
priciest_three=sorted(medical_records)[-3:]
print(f"Here are the three cheapest insurance costs in our medical records: {priciest_three}")
occurances_paul=names.count("Paul")
print(f"There are {occurances_paul} individuals with the name Paul in our medical records.")
