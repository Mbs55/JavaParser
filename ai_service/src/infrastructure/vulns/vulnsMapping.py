import json

def vulnsMapping(data:json)->dict:
    vulnsMap:dict={}
    for k,v in data.items():
        for i in v["apis"]:
            vulnsMap[i]=k
    return vulnsMap

    

    
