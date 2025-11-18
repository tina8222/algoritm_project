import json

# x =  '{ "name":"John", "age":30, "city":"New York", "isteacher":false,"ismarried":true,"lastname":null}'

# print(x)
# y = json.loads(x)

# print(y['name'])

# convert json to py use louds

# x =  { "name":"John", "age":30, "city":"New York", "isteacher":False,"ismarried":True,"lastname":None}

# y = json.dumps(x)
# print(y)
# print(type(y))
# convert py to json use dumps



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=3,sort_keys=True))






