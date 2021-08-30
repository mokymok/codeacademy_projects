city_name = 'Istanbul, Turkey'
pop_1927 = 691000
pop_2017 = 15029231

pop_change = pop_2017 - pop_1927

percentage_gr = (pop_change / pop_1927) * 100
annual_gr = percentage_gr / 90

def pop_growth(year_past, year_present, pop_past, pop_present):
  growth_rate = (((pop_present - pop_past)/ pop_past) * 100)/(year_present - year_past)
  return growth_rate

set_one = pop_growth(1927, 2017, pop_1927, pop_2017)
print(annual_gr, set_one)

set_two = pop_growth(1950, 2000, 983000, 8831800)
print(set_two)

report = f'The annual percentage change rate in population in Istanbul, Turkey from 1927 to 2017 was {set_one}.'

print(report)
