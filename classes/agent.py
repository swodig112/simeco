import numpy as np
from distributions import NormalDistribution


class Agent :
    def __init__ (self, name, money, income, expenses, income_changes,
            expenses_changes, hiring_possibility, firing_possibility, age=216):
        self.name = name
        self.age = age
        self.money = money
        self.income = income
        self.expenses = expenses
        self.working = False
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

