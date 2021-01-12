import numpy as np
import matplotlib.pyplot as plt
from distributions import NormalDistribution


class Agent :
    def __init__ (self, name, money, income, expenses, income_changes,
            expenses_changes, hiring_possibility, firing_possibility, age=216):
        self.name = name
        self.age = age
        self.initial_age = age
        self.money = money
        self.income = income
        self.expenses = expenses
        self.working = False
        self.results = {"age": [], "money": [], "income": [], "expenses": [], "working": []}
        if self.income != 0:
            self.working = True
        self.hiring_possibility = NormalDistribution(hiring_possibility[0],
                hiring_possibility[1])
        self.firing_possibility = NormalDistribution(firing_possibility[0],
                firing_possibility[1])
        self.income_changes = NormalDistribution(income_changes[0],
                income_changes[1])
        self.expenses_changes = NormalDistribution(expenses_changes[0],
                expenses_changes[1])
        self.previncome = self.income * 0.9


    def update (self):
        self.age +=1
        if not self.working:
            if self.hiring_possibility.random() >= 1:
                self.working = True
                self.hiring_possibility.mu += 0.05
                self.income = self.previncome * 0.9
                self.previncome = self.income
        elif self.firing_possibility.random() >= 1:
            self.income = 0
            self.working = False
            self.firing_possibility.mu += 0.05
        self.money += self.income - self.expenses
        self.income *= self.income_changes.random()
        self.expenses *= self.expenses_changes.random()

        self.add_results(self.age, self.money, self.income, self.expenses,
                self.working)


    def add_results(self, age, money, income, expenses, working):
        self.results["age"].append(age)
        self.results["money"].append(money)
        self.results["income"].append(income)
        self.results["expenses"].append(expenses)
        self.results["working"].append(working)


    def plot(self, entry):
        plt.plot(range(self.initial_age, self.age), self.results[entry], label=entry)
        plt.legend()

