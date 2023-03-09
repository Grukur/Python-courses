from abc import ABCMeta, abstractmethod
from Clase_18.Proyect_OOP.database import Database


class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass
