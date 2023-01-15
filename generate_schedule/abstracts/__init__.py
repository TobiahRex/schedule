from abc import ABC, abstractmethod

# Abstract base class for days
class AbstractDay(ABC):
    def __init__(self):
        self.activities = []

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def generate(self):
        pass