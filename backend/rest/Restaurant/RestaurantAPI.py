import requests
import json
import os
import sys
from itertools import chain

payload = {"topicCode": "EAT", "securityZoneCode": "", "subtopic": "All",
           "dataSourceId": "{1627256C-5E5E-428B-AC00-E845A54A5ECC}", "pageNumber": 1}

response = requests.post(
    "https://www.torontopearson.com/api/pointsofinterest/GetPointsOfInterestByTopic", params=payload)
data = response.text
parsed = json.loads(data)

# What is PointsOfInterest means ?
Restaurants_JSON = parsed["PointsOfInterest"]
text = json.dumps(Restaurants_JSON, sort_keys=True, indent=4)
# print(Restaurants_JSON)
# print('---------------------------------------')
# print(text)
# print('---------------------------------------')

Restaurants = {}
# Going through all restaurants and copy their information to a dictionary
# After that get this dictionary and assign to another dictionary since we want to search by restaurants name.
for title in Restaurants_JSON:

    current_restaurant = dict()
    name = title['Title']
    current_restaurant['Title'] = title['Title']
    current_restaurant['Description'] = title['Description']
    current_restaurant['Terminal'] = title['Terminal']

    # Here if restaurant is after security, we assign 0 else 1.
    if title['SecurityZoneName'] in 'after':
        current_restaurant['Seurity'] = '0'
    else:
        current_restaurant['Security'] = 1

    current_restaurant['Img'] = title['Url']+title['ThumbnailSrc']
    # Here we assign the dictionary to Main dictionary
    Restaurants[name] = current_restaurant


text = json.dumps(Restaurants_JSON, sort_keys=True, indent=4)
#Restaurants = json.dumps(Restaurants, separators=(',', ':'))
# print(Restaurants)
