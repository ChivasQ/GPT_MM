import json

file = open("test.txt", "r")
s = file.read()



indexf = s.find('{')
indexl = len(s) - s[::-1].find('}')
print(indexf, indexl)
s = s[indexf:indexl]

json_object = json.loads(s)
print(type(json_object))
print(json_object)
print(json_object.keys())
