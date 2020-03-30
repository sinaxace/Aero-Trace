import requests
import json
import os



# r = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=today&useScheduleTimeOnly=false")
r = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=today&useScheduleTimeOnly=false")
# path = os.getcwd()
# print(path)
parsed = json.loads(r.text)
text = json.dumps(parsed, sort_keys=False, indent=4)
f = open("arrival.txt", "w")
f.write(text)
f.close()

# print(r.text)
# print(text)