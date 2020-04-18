#!/usr/bin/env python

import requests
import json
import os
import sys


#Get fligh API
todayDep = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=DEP&day=today&useScheduleTimeOnly=false")
