#!/usr/bin/env python3
import sys
sys.path.insert(1, "../classes")


from agent import Agent
from distributions import NormalDistribution
import credits
from time import time

t1 = time()
for i in range(1):
    loan = credits.Loan()
    loan.get_loan(NormalDistribution(2000, 200), NormalDistribution(
        5 * 12, 6), NormalDistribution(15, 3))
    agent = Agent("swodig", 1000, 0, 100, NormalDistribution(155, 5), NormalDistribution(
        15, 5), NormalDistribution(0.8, 0.05), loan, credits.Debt())
    for i in range(500):
        agent.update()
print(time() - t1)
agent.plot("money")
agent.plot("income")
agent.plot("expenses")
agent.show()
