#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plot


def main(N, M):
    age = np.zeros(N)
    money = np.full(N, 1000, dtype=np.float64)
    income = np.zeros(N, dtype=np.float64)
    previncome = np.zeros(N, dtype=np.float64)
    expenses = np.full(N, 100, dtype=np.float64)
    income_changes = np.random.normal(155, 5, (M, N))
    expenses_changes = np.random.normal(15, 5, (M, N))
    working = np.zeros(N, dtype=bool)
    tax = np.zeros(N, dtype=np.float64)
    fire = 0.01
    hire = 0.20
    working_possibility_getting_fired = np.random.choice(
        [0, 1], p=[fire, 1 - fire], size=(M, N))
    working_possibility_getting_hired = np.random.choice(
        [0, 1], p=[hire, 1 - hire], size=(M, N))

    loan_payment_amount = np.random.normal(150, 30, (N, 20))
    loan_return_amount = loan_payment_amount * \
        np.random.normal(13, 1, (N, 20)).astype(int)
    interest = np.random.normal(15, 2, (N, 20))
    loan_amount = loan_return_amount * (100 / (interest + 100))
    loan_time = np.random.normal(5 * 12, 6, (N, 20))
    loan_time = np.cumsum(loan_time, axis=1)
    loan_payment_table = np.zeros((M, N))
    agent = {"money": np.zeros((N, M)), "income": np.zeros((N, M)), "expenses": np.zeros(
        (N, M)), "debt": np.zeros((N, M)), "Tax": np.zeros((N, M))}

    for i in range(N):
        for j in range(20):
            loan_payment_table[int(loan_time[i, j]):int(
                loan_time[i, j] + loan_return_amount[i, j] / loan_payment_amount[i, j]), i] = -1 * loan_payment_amount[i, j]
            loan_payment_table[int(loan_time[i, j]):int(
                loan_time[i, j] + loan_return_amount[i, j] / loan_payment_amount[i, j]), i] += loan_amount[i, j]

    for m in range(M):
        age += 1
        workingcopy = working.copy()
        working[np.invert(
            workingcopy)] = working_possibility_getting_hired[m, np.invert(workingcopy)]
        working[workingcopy] = working_possibility_getting_fired[m, workingcopy]
        previncome[np.bitwise_and(workingcopy, np.invert(
            working))] = income[np.bitwise_and(workingcopy, np.invert(working))] * 0.9
        income[np.bitwise_and(working, np.invert(
            workingcopy))] = previncome[np.bitwise_and(working, np.invert(workingcopy))]
        income[np.invert(working)] = 0
        tax[workingcopy] = 0.06 * income[workingcopy]
        income += income_changes[m]
        expenses += expenses_changes[m]

        money += income - expenses + loan_payment_table[m] - tax

        agent["money"][:, m] = money
        agent["income"][:, m] = income
        agent["expenses"][:, m] = expenses
        agent["Tax"][:, m] = tax
        #agnet["debt"][:, m ] = debt

    plt.plot(agent["money"][0])
    plt.plot(agent["income"][0])
    plt.plot(agent["expenses"][0])
    plt.plot(agent["Tax"][0])
    plt.show()

    np.save("data.npy", agent)


if __name__ == "__main__":
    main(10, 12)
