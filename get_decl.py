# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:56:42 2017

@author: Viator
"""

import requests
import json
from time import sleep
"""
data2 = []

"""print("Fetching page #%s" % 1)

r = requests.get("http://declarations.com.ua/search?format=json").json()

data += r["results"]["object_list"]"""

for decl in range(30000, 100001):
    sleep(0.01)
    try:
        subr = requests.get(
        "http://declarations.com.ua/declaration/%s?format=json" % decl).json()
        data2.append(subr["declaration"])
    except: None

print("Declarations exported %s" % len(data2))"""
with open("decl30_100k.json", "w") as fp:
    json.dump(data2, fp)