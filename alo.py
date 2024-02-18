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

for i in list(map(str, json_object.keys())):
    print(i)
    for j in json_object[i]:
        print(' ', j)

        for l in json_object[i][j]:
            if type(l) is str:
                print(l, "s")
            else:print('    ', l)