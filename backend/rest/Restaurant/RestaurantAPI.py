import requests
import json
import os
import sys
from itertools import chain

payload = {"topicCode":"EAT","securityZoneCode":"","subtopic":"All","dataSourceId":"{1627256C-5E5E-428B-AC00-E845A54A5ECC}","pageNumber":1}

response = requests.post("https://www.torontopearson.com/api/pointsofinterest/GetPointsOfInterestByTopic", params=payload)
data = response.text
parsed = json.loads(data)
titles = parsed["PointsOfInterest"]
text = json.dumps(titles, sort_keys=True, indent=4)


#print(text)
title_list = []
Restaurants = {}
for title in titles:
    name = title['Title']
    current_restaurant = name
    current_restaurant = dict()
    current_restaurant['Title'] = name
    current_restaurant['Description'] = title['Description']
    current_restaurant['Terminal'] = title['Terminal']
    if title['SecurityZoneName'] in 'after':
        current_restaurant['Seurity'] = '0'
    else:
        current_restaurant['Security'] = 1
    current_restaurant['Img'] = title['Url']+title['ThumbnailSrc']
   # print(current_restaurant)
    Restaurants[name] = current_restaurant
    title_list.append(name)
    text = json.dumps(titles, sort_keys=True, indent=4)

#print(title_list)
print(Restaurants)