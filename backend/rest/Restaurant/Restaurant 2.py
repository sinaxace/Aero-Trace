import requests
import json
import os
import sys

payload = {"topicCode":"EAT","securityZoneCode":"","subtopic":"All","dataSourceId":"{1627256C-5E5E-428B-AC00-E845A54A5ECC}","pageNumber":1}

response = requests.post("https://www.torontopearson.com/api/pointsofinterest/GetPointsOfInterestByTopic", params=payload)
data = response.text
parsed = json.loads(data)
titles = parsed["PointsOfInterest"]
text = json.dumps(titles, sort_keys=True, indent=4)

print(text)
title_list = []
for title in titles:
    name=title['Title']
    title_list.append(name)
    text = json.dumps(titles, sort_keys=True, indent=4)

print(title_list)