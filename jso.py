import json as j
data={"name":"sumanth","age":21}
jsondata=j.dumps(data)
myjsondata=j.loads(jsondata)
print(myjsondata)