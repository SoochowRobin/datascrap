import json

# practice with json dump: to convert python object to json object
data = [{'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}]

data2 = json.dumps(data)
# class 'str': cause it is json string
print(type(data2))
# class list: cause it is list
print(type(data))
print(data2)

# convert json to python type
data_python = json.loads(data2)
print(data_python)
print(type(data_python))