import numpy as np
import pandas as pd

def simulate_survival(initial_savings, income_mean, income_std,
                      expense_mean, expense_std,
                      months=12, simulations=1000):

    survival_times = []
    broke_flags = []

    for _ in range(simulations):
        savings = initial_savings
        survived = months  # assume you survive full duration

        for month in range(months):
            income = max(0, np.random.normal(income_mean, income_std))
            expense = max(0, np.random.normal(expense_mean, expense_std))

            savings += income - expense

            if savings <= 0:
                survived = month + 1
                break

        survival_times.append(survived)
        broke_flags.append(1 if survived < months else 0)

    return pd.DataFrame({
        "survival_time": survival_times,
        "broke": broke_flags
    })


def calculate_metrics(results, months):
    prob_broke = results["broke"].mean()
    median_survival = results["survival_time"].median()
    worst_case = results["survival_time"].quantile(0.1)

    return {
        "probability_broke": prob_broke,
        "median_survival": median_survival,
        "worst_case": worst_case
    }