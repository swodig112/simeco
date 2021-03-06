import numpy as np
import matplotlib.pyplot as plt
from distributions import NormalDistribution
from credits import Debt, Loan


class Agent:
    def __init__(self, name, money, income, expenses, income_changes,
                 expenses_changes, excess_spending, Loan, Debt, age=216):
        self.name = name
        self.age = age
        self.initial_age = age
        self.money = money
        self.income = income
        self.previncome = income
        self.expenses = expenses
        self.working = 0
        self.Debt = Debt
        self.Loan = Loan
        self.hire = 0.20
        self.fire = 0.01
        self.excess_spending = excess_spending
        self.excess_spending_per_month = 0
        self.income_changes = income_changes
        self.expenses_changes = expenses_changes
        # self.Loan.get_loan(NormalDistribution(2000,200), NormalDistribution(5*12,6),NormalDistribution(15,3))
        self.results = {"age": [], "money": [], "income": [], "expenses": [],
                        "working": [], "total_debt": [], "excess_spending": []}

    def update(self):
        self.age += 1

        self.working = self.working_possibility(
            self.working, self.hire, self.fire)
        if(self.working):
            if(self.income == 0):
                self.income = 0.9 * self.previncome
                #self.income = 1000 * (1.01**((self.age - self.initial_age)//12))
            self.income += self.income_changes.random()

        elif(not self.working):
            if(self.income):
                self.previncome = self.income
            self.income = 0
        self.expenses += self.expenses_changes.random()

        self.money = self.pay_credit(
            self.money, self.income, self.expenses, self.Debt.sum_debt(), self.Loan.sum_loan(self.age))
        self.excess_spending_per_month = abs(self.excess_spending.random())
        self.money *= self.excess_spending_per_month
        self.add_results(self.age, self.money, self.income, self.expenses,
                         self.working, self.excess_spending_per_month)

    def working_possibility(self, past_inf, hire, fire):
        if past_inf:
            return np.random.choice([0, 1], p=[fire, 1 - fire])
        else:
            return np.random.choice([1, 0], p=[hire, 1 - hire])

    def add_results(self, age, money, income, expenses, working, excess_spending):
        self.results["age"].append(age)
        self.results["money"].append(money)
        self.results["income"].append(income)
        self.results["expenses"].append(expenses)
        self.results["working"].append(working)
        self.results["total_debt"].append(
            self.Debt.sum_debt_amount() + self.Loan.sum_loan_amount(self.age))
        self.results["excess_spending"].append(excess_spending)

    def pay_credit(self, money, income, expenses, sum_debt, sum_loan):

        money += income - expenses - sum_debt - sum_loan
        if(money < 0):
            self.Debt.add_debt((money) * (-1), np.random.randint(1, 24))
            money = 0
        self.Debt.update()
        self.Loan.update(self.age)
        return money

    def plot(self, entry):
        plt.plot(range(self.initial_age, self.age),
                 self.results[entry], label=entry)
        plt.legend()

    def plot_histogram(self, entry):
        plt.hist(self.results[entry], bins=100)
        plt.show()

    def show(self):
        plt.show()
