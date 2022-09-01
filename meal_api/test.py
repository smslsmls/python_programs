import json
import values

def filter_func(a):
    if a == '*':
        return False
    if a == '.':
        return False
    if a >= '0' and a <= '9':
        return False
    return True

with open(values.meal_data,'r') as fp:
    meal_json=json.load(fp)

print(meal_json)

meal_data = []

for i in range(meal_json['mealServiceDietInfo'][0]['head'][0]['list_total_count']):

    meal_data.append(meal_json['mealServiceDietInfo'][1]['row'][i]['DDISH_NM'])

data = {'조식': [], '중식': [], '석식': []}
meal_name = ['조식', '중식', '석식']
for i in range(meal_json['mealServiceDietInfo'][0]['head'][0]['list_total_count']):
    meal = meal_data[i].split('<br/>')
    for food in meal:
        data[meal_name[i]].append(''.join(list(filter(filter_func, food))))
print(data)