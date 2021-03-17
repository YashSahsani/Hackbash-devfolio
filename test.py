import requests
import json
import time
data = {"password":"DuBaraMatPuchna"}
a = json.loads(requests.post("http://localhost:3000/api/login",json=data).text)
print(a)
data_n = {"ItemName":"item3","price":"11495"}
result = requests.post("http://localhost:3000/api/CreateAsset",headers={"Authorization":"Bearer "+a['token']},json=data_n)
print(result.text)
#data_n = {"ItemName":"LeBron witness 6 ep","component_name":"sole","dict":{"location":"USA","vendor":"nike"}}
#result = requests.post("http://localhost:3000/api/AddComponentInfo",headers={"Authorization":"Bearer "+a['token']},json=data_n)
#print(result.text)
#data_n = {"ItemName":"LeBron witness 6 ep","component_name":"material","dict":{"location":"USA","vendor":"nike"}}
result = requests.post("http://localhost:3000/api/AddComponentInfo",headers={"Authorization":"Bearer "+a['token']},json=data_n)
print(result.text)
data_n = {"ItemName":"LeBron witness 6 ep","component_name":"salces","dict":{"location":"Chain","vendor":"nike"}}
result = requests.post("http://localhost:3000/api/AddComponentInfo",headers={"Authorization":"Bearer "+a['token']},json=data_n)
print(result.text)
