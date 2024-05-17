#!/usr/bin/env python

import requests
import json
import os
import sys

# Get fligh API
todayDep = requests.get(
    "https://gtaa-fl-prod.azureedge.net/api/flights/list?type=DEP&day=today&useScheduleTimeOnly=false")
parsed = json.loads(todayDep.text)
schedule_dep = parsed['list']
print(schedule_dep)
# Get Country
id_list_dep = []
country_list_dep = []
city_list_dep = []

# Get all country anc city no duplicate
for id_ in schedule_dep:
    if id_["routes"][0]["cnty"] in country_list_dep:
        pass
    else:
        country_list_dep.append(id_["routes"][0]["cnty"])
    if id_["routes"][0]["city"] in country_list_dep:  # Is it country or city_list_dep ?
        pass
    else:
        city_list_dep.append(id_["routes"][0]["city"])
print('-----country_list_dep--------')
print(country_list_dep)
print('-----city_list_dep--------')
print(city_list_dep)

# create dictionary country
dic_country_city_dep_list = {}
for country in schedule_dep:
    for c in country_list_dep:
        dic_country_city_dep_list[c] = []
print('-----dic_country_city_dep_list--------')
print(dic_country_city_dep_list)


def adding_city_dep(schedule_dep, dic_country_city_dep_list):
    for s in schedule_dep:
        if s["routes"][0]["cnty"] in dic_country_city_dep_list:
            if s["routes"][0]["city"] not in dic_country_city_dep_list[s["routes"][0]["cnty"]]:
                dic_country_city_dep_list[s["routes"][0]["cnty"]].append(
                    s["routes"][0]["city"])
    return dic_country_city_dep_list


country_city_list = adding_city_dep(schedule_dep, dic_country_city_dep_list)
print('-----print(adding_city_dep(schedule_dep------')
print(adding_city_dep(schedule_dep, dic_country_city_dep_list))
