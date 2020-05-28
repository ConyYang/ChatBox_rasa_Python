import json

with open('timezones.json') as f:
  data = json.load(f)

pacific = data[1]


city_dict_combine = {}

for i in range(len(data)):
    city_list = []
    city_dict = {}
    for city in data[i]['utc']:
        try:
            city_list.append(city.split('/')[1])
        except IndexError:
            pass
        city_list_filter = list(filter(lambda city_i: city_i[:3] != 'GMT', city_list))

    for city in city_list_filter:
        city_dict[city] = data[i]['text']
    city_dict_combine.update(city_dict)

# print(city_dict_combine)

with open('../city_name_timezone.json', 'w') as fp:
    json.dump(city_dict_combine, fp)