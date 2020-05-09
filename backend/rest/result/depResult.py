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
dep_flight_jsondata_all = {}
dep_flight_id_all={}
dep_flight_route_all={}
dep_flight_info_list_jsondata = {}
dep_destination_route = {}
dep_flight_list = []
# dep_flight_information_list=[]
dep_schTime_time = [] #"schTime": "2020-04-26T07:00:00-04:00",
dep_lastest_time = [] #"latestTm": "2020-04-26T06:46:00-04:00",
dep_status=[] #CAN DEP ONT DEL
dep_destination_list=[] #SHANGAI VIA TOKYP 
dep_destination = {}
dep_airline_id_single={}
dep_flight_no=[]
dep_terminal=[]# "term": "T3",
dep_gate=[] # "gate": "B38",
# dep_flight_info_list_jsondata['terminal']=[]
# dep_flight_info_list_jsondata ={'terminal':[],'status':[]}
# dep_flight_information_list.append(dep_flight_info_list_jsondata)

# dep_flight_info_list_jsondata['schTime']=[]
# dep_flight_info_list_jsondata['terminal'] =[]
# dep_flight_info_list_jsondata['latestTm'] =[]
# dep_flight_info_list_jsondata['status'] =[]
# dep_flight_info_list_jsondata ={'terminal':[],'status':[]}


dep_flight_information_list = []
# dep_flight_info_list_jsondata['schTime']=[]
# dep_flight_info_list_jsondata['terminal'] =[]
# dep_flight_info_list_jsondata['latestTm'] =[]
# dep_flight_info_list_jsondata['status'] =[]
# dep_flight_info_list_jsondata['terminal_test']=["a"]
#Get all flight detail
def dep_flight_schedule(schedule_dep):
    i=0
    for flight in schedule_dep:

        # dep_flight_information_list.append(dep_flight_info_list_jsondata)

        # i = 0
        # schTime =  
        # dep_flight_info_list_jsondata['schTime'] = flight["schTime"]
        # dep_flight_info_list_jsondata['schTime'].append(flight["schTime"])
        # dep_flight_info_list_jsondata['latestTm'].append(flight["latestTm"])
        # dep_destination_route = {'code':'',
        #                         'name':'',
        #                         'short':'',
        #                         'city':'',
        #                         'country':'',
        #                         'region':''}  

        dep_flight_info_list_jsondata ={'schTime':'',
                                        'latestTime':'',
                                        'terminal':'',
                                        'status':'', 
                                        'gate':'',
                                        'destination':[] }

                
        
        dep_flight_information_list.append(dep_flight_info_list_jsondata)

        # dep_flight_info_list_jsondata['status']= flight["status"]
        # dep_flight_info_list_jsondata['terminal'] = flight["term"]

        # dep_flight_info_list_jsondata['status'].append(flight["status"])
        # dep_flight_info_list_jsondata['terminal'].append(flight["term"])

        dep_flight_info_list_jsondata['schTime']= flight["schTime"]
        dep_flight_info_list_jsondata['latestTm']= flight["latestTm"]
        dep_flight_info_list_jsondata['terminal']= flight["term"]
        dep_flight_info_list_jsondata['status'] = flight["status"]
        dep_flight_info_list_jsondata['gate']= flight["gate"]

        dep_flight_route = flight["routes"]
        # dep_flight_info_list_jsondata['destination']= flight["routes"]
        
        j = 0
        for destination in dep_flight_route:
            dep_destination_route = {'code':'',
                                'name':'',
                                'short':'',
                                'city':'',
                                'country':'',
                                'region':''}  
            dep_flight_info_list_jsondata['destination'].append(dep_destination_route)
            dep_destination_route['code'] = destination['code']
            dep_destination_route['name'] = destination['name']
            dep_destination_route['short'] = destination['short']
            dep_destination_route['city'] = destination['city']
            dep_destination_route['country'] = destination['cnty']
            dep_destination_route['region'] = destination['region']

            print(destination)
            j += 1


        # dep_flight_information_list['latestTm'] .append(dep_flight_info_list_jsondata['latestTm'][i])

        # dep_flight_information_list[i]['status'].append(dep_flight_info_list_jsondata['status'][0])
        # dep_flight_information_list[i]['terminal'].append(dep_flight_info_list_jsondata['terminal'][0])

        # dep_flight_information_list[i]['status'] = dep_flight_info_list_jsondata['status'][i]
        # dep_flight_information_list[i]['terminal'] = dep_flight_info_list_jsondata['terminal'][i]



        # dep_terminal.append(flight["term"])
        
        # dep_flight_info_list_jsondata['terminal'].append(flight["term"])
        # dep_flight_information_list.append(dep_flight_info_list_jsondata)

        # dep_flight_info_list_jsondata[i]["inserts"].append({"term":flight["term"]})
        # dep_flight_info_list_jsondata['terminal'].append(flight["term"])
        # dep_flight_information_list.append(dep_flight_info_list_jsondata)
        # dep_flight_information_list.append({"status":flight["status"]},{"terminal":flight["term"]}])
        # dep_flight_information_list.append(dep_flight_info_list_jsondata)

        i += 1
        # dep_flight_information_list.append({"terminal":flight["term"]})
        # for terms in dep_terminal:
        #     i=0;
        #     dep_flight_information_list[i]["inserts"].append({"term":flight["term"]})
        #     i += 1 
        # if term in dep_flight_info_list_jsondata:
        #     dep_flight_info_list_jsondata['terminal'].append(term)
        # else:
        #     dep_flight_info_list_jsondata['terminal'] = [term]
        
        
        # dep_flight_information_list.append(dep_flight_info_list_jsondata)
    return dep_flight_information_list



# dep_flight_jsondata_all=dep_flight_information_list
# print(dep_flight_information_list)
print (json.dumps(dep_flight_schedule(schedule_dep), indent=4, sort_keys=True))



