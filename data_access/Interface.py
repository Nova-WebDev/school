from abc import ABC, abstractmethod

class IRepository(ABC):
    @staticmethod
    @abstractmethod
    def insert(cur, name):
        pass

    @staticmethod
    @abstractmethod
    def update(cur, pk, name):
        pass

    @staticmethod
    @abstractmethod
    def delete(cur, pk):
        pass

    @staticmethod
    @abstractmethod
    def get_by_id(cur, pk):
        pass

    @staticmethod
    @abstractmethod
    def get_all(cur):
        pass
