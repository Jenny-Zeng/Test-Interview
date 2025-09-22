import json
# data = {'name':'jenny','age':30,'ip':["127.0.0.1","10.210.32.28"]}
# print(type(data)) #<class 'dict'>
# json_str = json.dumps(data)
# print(json_str)
# pretty_json = json.dumps(data, indent=2)
# print(pretty_json)

json_data = '{"name": "jenny", "age": 30, "ip": ["127.0.0.1", "10.210.32.28"]}'
python_obj = json.loads(json_data)
print(python_obj)



