import json
with open('../../../vulns.json','r') as file:
    data:json=json.load(file)

def vulnsMapping(data:json)->dict:
    vulnsMap:json={}
    for k,v in data.items():
        for i in v["apis"]:
            vulnsMap[i]=k
    return vulnsMap

    
