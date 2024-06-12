# Homework 6

from abc import ABC, abstractmethod

class Countries(ABC):

    @abstractmethod
    def georgia_budget(self):
        pass

    @abstractmethod
    def georgia_population(self):
        pass

    @abstractmethod
    def georgia_currency(self):
        pass

class Georgia(Countries):
    def __init__(self, budget, population, currency):
        self.budget = budget
        self._population = population
        self.__currency = currency

    def georgia_budget(self):
        print(f"Budget: {self.budget}")

    def georgia_population(self):
        print(f"Population: {self._population}")

    def georgia_currency(self):
        print(f"Currency: {self.__currency}")

georgia = Georgia(30000000, 3500000, "Gel")

georgia.georgia_budget()
georgia.georgia_population()
georgia.georgia_currency()
