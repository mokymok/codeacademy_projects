names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost=0
for i in actual_insurance_costs:total_cost+=i
average_cost=total_cost/len(actual_insurance_costs)
print(f"Average Insurance Cost: {average_cost} dollars.\n")
for i in range(len(names)):
  name=names[i]
  insurance_cost=actual_insurance_costs[i]
  print(f"The insurance cost for {name} is {insurance_cost} dollars.")
  if insurance_cost>average_cost:print(f"The insurance cost for {name} is above average.\n")
  elif insurance_cost<average_cost:print(f"The insurance cost for {name} is below average.\n")
  else:print(f"The insurance cost for {name} is equal to the average.\n")
updated_estimated_costs=[round(1.1*i,1) for i in estimated_insurance_costs]
print(updated_estimated_costs)
