from abc import ABC,abstractmethod
class LlmService(ABC):
    @abstractmethod
    def prompt(self,method:str):
        pass
