class DebtManager:
    def __init__(self):
        self.debtID = 0
        self.debts = {}


    def add_debt(self, debt_amount, birth_month, paid=0):
        self.debts[self.debtID] = {"debt_amount": debt_amount, "birth_month":
                birth_month, "paid": paid}
        self.debtID += 1


    def update(self):
        paid_debts = []
        for debtID in self.debts:
            if self.debts[debtID]["paid"] == self.debts[debtID]["debt_amount"]:
                paid_debts.append(debtID)

        for debtID in paid_debts:
            self.debts.pop(debtID)
