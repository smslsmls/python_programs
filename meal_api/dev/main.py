import send_message
import refresh
import meal_api
import values

meal = meal_api.meal_menu()

for i in range(3):
    if len(meal[values.meal_name[i]])==0:
        meal[values.meal_name[i]].append('없음')

data = {
    'object_type': 'text',
    'text': "",
    'link': {
        'web_url': 'http://dodam.b1nd.com',
        'mobile_web_url': 'http://dodam.b1nd.com'
    },
    'button_title': '도담도담'
}

breakfast_data = data.copy()

lunch_data = data.copy()

dinner_data = data.copy()

breakfast_data['text'] = '-조식 : '+', '.join(meal['조식'])

lunch_data['text'] = '-중식 : '+', '.join(meal['중식'])

dinner_data['text'] = '-석식 : '+', '.join(meal['석식'])

args={
    'date': values.time_str(),
    'breakfast' : ' ,'.join(meal['조식'][2:]),
    'lunch' : ' ,'.join(meal['중식'][2:]),
    'dinner' : ' ,'.join(meal['석식'][2:])
}

refresh.f_auth_refresh()
print(send_message.send_message_id(74472,args))
print(send_message.send_message_object(breakfast_data))
print(send_message.send_message_object(lunch_data))
print(send_message.send_message_object(dinner_data))