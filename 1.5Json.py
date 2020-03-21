import json

x = '{ "name" : "Gilbert Hyman Goes", "angkatan" : 2017, "nim" : "D121171306" }'

y = json.loads(x)
print(y['nim'])