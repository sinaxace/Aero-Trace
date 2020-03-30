#!/usr/bin/env python

import requests
import json
import os
import sys


#Get fligh API
# yesterdayArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=yesterday&useScheduleTimeOnly=false")
todayArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=today&useScheduleTimeOnly=false")
#tomorrowArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=tomorrow&useScheduleTimeOnly=false")

#Get file path
fileDir = os.path.dirname(os.path.abspath(__file__))
print(fileDir)

parsed = json.loads(todayArr.text)
schedule = parsed['list']
#Get flight id
id_list = []
for id_ in schedule:
    name = id_['id2']
    id_list.append(name)
print(id_list)    
text = json.dumps(schedule, sort_keys=False, indent=4)
f = open(fileDir+"\\arrival.txt", "w")
f.write(text)
f.close()

# print(r.text)
# print(text)