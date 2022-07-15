import requests
import json
from datetime import date, datetime
import values


def filter_func(a):
    if a == '*':
        return False
    if a == '.':
        return False
    if a >= '0' and a <= '9':
        return False
    if a == '(' and a == ')':
        return False
    return True

def filter_func2(a):
    if a == '*':
        return False
    return True

def date_2_str(d):
    date_str = str(d.year)
    if d.month < 10:
        date_str += '0'
    date_str += str(d.month)
    if d.day < 10:
        date_str += '0'
    date_str += str(d.day)
    return date_str


def meal_menu():
    with open(values.value_json, 'r') as fp:
        past_json = json.load(fp)

    past_time = date(past_json['year'], past_json['month'], past_json['day'])

    curr_time = datetime.now().date()

    date_str=date_2_str(curr_time)

    if curr_time > past_time:
        response = requests.post(
            'https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=fa297ba8a3404d6aa5d6aa12b2b11818&Type=json&ATPT_OFCDC_SC_CODE=D10&SD_SCHUL_CODE=7240454&MLSV_YMD='+date_str)
        data = response.json()
        with open(values.meal_data, "w") as fp:
            json.dump(data, fp)
        meal_json = data
        # meal=response.json()["DDISH_NM"]
    else:
        with open(values.meal_data, "r") as fp:
            meal_json = json.load(fp)
        # meal=

    curr_json = {'year': curr_time.year,
                 'month': curr_time.month, 'day': curr_time.day}
    with open(values.value_json, 'w') as fp:
        json.dump(curr_json, fp)

    meal_data = []

    for i in range(meal_json['mealServiceDietInfo'][0]['head'][0]['list_total_count']):

        meal_data.append(meal_json['mealServiceDietInfo'][1]['row'][i]['DDISH_NM'])

    data = {'조식': [], '중식': [], '석식': []}
    for i in range(meal_json['mealServiceDietInfo'][0]['head'][0]['list_total_count']):
        meal = meal_data[i].split('<br/>')
        for food in meal:
            # data[values.meal_name[i]].append(''.join(list(filter(filter_func, food))))
            data[values.meal_name[i]].append(''.join(list(filter(filter_func2,food.split(' ')[0]))))
    return data