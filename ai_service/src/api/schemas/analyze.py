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

class MethodInfo(BaseModel):
     id:str
     name:str
     signature:str
     qualifiedSignature:str
     className:str
     packageName:str
     filePath:str
     beginLine:int
     endLine:int
     sourceCode:str
     returnType:str
     genericTypes:list[str]
     thrownExceptions:list[str]
     visibility:str
     isEntryPoint:bool
     httpMethod:str
     endpoint:str
     isStatic:bool
     isFinal:bool
     isAbstract:bool
     isSynchronized:bool
     isNative:bool
     imports:list[str]
     annotations:list[str]
     outgoingCalls:list[str]
     incomingCalls:list[str]
     parameters:list[str]
     variables:list[str]
     isConstructor:bool
     containsLambda:bool


class ClassInfo(BaseModel):
     id:str
     className:str
     qualifiedName:str
     packageName:str
     filePath:str
     beginLine:int
     endLine:int
     sourceCode:str
     isClass:bool
     isInterface:bool
     isEnum:bool
     isRecord:bool
     visibility:str
     isAbstract:bool
     isFinal:bool
     superClass:str
     implementedInterfaces:list[str]
     constructors:list[str]
     methods:list[str]
     fields:list[str]
     annotations:list[str]
     imports:list[str]
     dependencies:list[str]
     genericTypes:list[str]

class ProjectData(BaseModel):
     Methods:list[MethodInfo]
     Classes:list[ClassInfo]

     
class AnalyzeRequest(BaseModel):
    Project:ProjectData