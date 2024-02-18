# -*- coding: utf-8 -*-
import sys
def iterate_json(json_data, level=0):
    sys.stdout.reconfigure(encoding='utf-8')
    if type(json_data) == dict:
        for key, value in json_data.items():
            print(f"{'├' * level} {key}")
            iterate_json(value, level + 1)
    elif type(json_data) == list:
        for item in json_data:
            iterate_json(item, level)
    else:
        print(f"{'———' * level} {json_data}")
#

import json

file = open("test.txt", "r", encoding="utf-8")
s = file.read()
indexf = s.find('{')
indexl = len(s) - s[::-1].find('}')
print(indexf, indexl)
s = s[indexf:indexl]

json_data = json.loads(s)

iterate_json(json_data)