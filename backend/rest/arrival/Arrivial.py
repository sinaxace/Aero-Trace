#!/usr/bin/env python

import requests
import json
import os
import sys


# Get fligh API
# yesterdayArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=yesterday&useScheduleTimeOnly=false")
todayArr = requests.get(
    "https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=today&useScheduleTimeOnly=false")
#tomorrowArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=tomorrow&useScheduleTimeOnly=false")

# Get file path
#fileDir = os.path.dirname(os.path.abspath(_file_))
# print(fileDir)

parsed = json.loads(todayArr.text)
schedule = parsed['list']
print(schedule)
# Get flight id
id_list = []
country_list = []
city_list = []

for id_ in schedule:
    # id_list.extend((id_["al"], id_['id2'], id_["schTime"][:10], id_["gate"], id_["term"], id_["routes"]))
    if id_["routes"][0]["cnty"] in country_list:
        pass
    else:
        country_list.append(id_["routes"][0]["cnty"])
    if id_["routes"][0]["city"] in city_list:
        pass
    else:
        city_list.append(id_["routes"][0]["city"])
print('-----country_list_dep--------')
print(country_list)
print('-----city_list--------')
print(city_list)
dic = {}

for country in schedule:
    for c in country_list:
        dic[c] = []
print('-----dic--------')
print(dic)


def adding_city(schedule, dic):

    for s in schedule:
        if s["routes"][0]["cnty"] in dic:
            if s["routes"][0]["city"] not in dic[s["routes"][0]["cnty"]]:
                dic[s["routes"][0]["cnty"]].append(s["routes"][0]["city"])
    return dic


country_city_list = adding_city(schedule, dic)
print('-----adding_city(schedule,dic)--------')
print(adding_city(schedule, dic))


# text = json.dumps(schedule, sort_keys=False, indent=4)
# #f = open(fileDir+"\\arrival.txt", "w")
# f.write(text)
# f.close()

# print(r.text)
# print(todayArr.text)
