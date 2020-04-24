#!/usr/bin/env python

import requests
import json
import os
import sys

#Get fligh API
todayDep = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=DEP&day=today&useScheduleTimeOnly=false")
parsed = json.loads(todayDep.text)
schedule_dep = parsed['list']

#Get Flight information
dep_schTime_time = []
dep_lastest_time = []
dep_status=[]
dep_destination=[]
dep_airline=[]
dep_flight_no=[]
dep_terminal=[]
dep_gate=[]



