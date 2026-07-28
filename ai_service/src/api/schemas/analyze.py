from pydantic import BaseModel
from enum import Enum
class Status(Enum):
     SAFE="SAFE"
     VULNERABLE="VULNERABLE"
class Risk(Enum):
     CRITICAL="CRITICAL"
     HIGH="HIGH"
     MEDIUM="MEDIUM"
     LOW="LOW"

class Vulns(BaseModel):
    type:str
    severity:str
    cwe:str
    line:int
    description:str
    recommendation:str


class AnalyzeResponse(BaseModel):
        status:Status
        overall_risk:Risk
        confidence:float
        summary:str
        vulnerabilities:list[Vulns]


class AnalyzeRequest(BaseModel):
    id:int
    method:str