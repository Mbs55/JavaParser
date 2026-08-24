from src.api.schemas.analyze import *
def StrToM(p:ProjectData)->dict:
    Map:dict={}
    for m in p.methods:
        Map[m.id]=m
    return Map


    