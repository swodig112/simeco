import numpy as np
from distributions import NormalDistribution
import matplotlib.pyplot as plt


class Debt:
    def __init__(self):
        self.debtID = 0
        self.debt = {}

    def add_debt(self, total_debt, month, paid=0):
        self.debtID += 1
        self.debt[self.debtID] = {
            "total_debt": total_debt, "month": month, "paid": paid}

    def sum_debt(self):
        sum = 0
        for i in self.debt:
            sum += self.debt[i]["total_debt"] / self.debt[i]["month"]
        return sum

    def sum_debt_amount(self):
        sda = 0
        for debtID in self.debt:
            sda += self.debt[debtID]["total_debt"] - (self.debt[debtID]["paid"] * (
                self.debt[debtID]["total_debt"] / self.debt[debtID]["month"]))
        return sda

    def update(self):
        rem_debt = []
        for i in self.debt:
            rem_debt.append(i)
        for i in rem_debt:
            self.debt[i]["paid"] += 1
            if (self.debt[i]["paid"] == self.debt[i]["month"]):
                self.debt.pop(i)


class Loan:
    def __init__(self):
        self.loanID = 0
        self.loan = {}

    def get_loan(self, value, time, payment):
        age = 216
        for i in range(20):
            age += int(time.random())
            self.add_loan(int(value.random()), int(payment.random()), 0, age)

    def add_loan(self, total_loan, payment, interest, start_month, paid=0):
        self.loanID += 1
        self.loan[self.loanID] = {"total_loan": total_loan, "payment": payment,
                                  "interest": interest, "start_month": start_month, "paid": paid}

    def sum_loan(self, age):
        sum = 0
        for i in self.loan:
            if age >= self.loan[i]["start_month"]:
                sum += self.loan[i]["total_loan"] / self.loan[i]["payment"]
        return sum

    def sum_loan_amount(self, age):
        sda = 0
        for loanID in self.loan:
            if age >= self.loan[loanID]["start_month"]:
                sda += self.loan[loanID]["total_loan"] - (self.loan[loanID]["paid"] * (
                    self.loan[loanID]["total_loan"] / self.loan[loanID]["payment"]))
        return sda

    def update(self, age):
        rem_loan = []
        for i in self.loan:
            rem_loan.append(i)
        for i in rem_loan:
            if age >= self.loan[i]["start_month"]:
                self.loan[i]["paid"] += 1
                if (self.loan[i]["paid"] == self.loan[i]["payment"]):
                    self.loan.pop(i)
