import pandas as pd
import random

goals = [
    "Wealth Creation",
    "Retirement",
    "Child Education",
    "Emergency Fund",
    "House Purchase"
]

risks = ["Low", "Medium", "High"]

recommendations = {
    ("Low", "Retirement"): "Government Bonds",
    ("Low", "Emergency Fund"): "Fixed Deposit",
    ("Low", "House Purchase"): "Fixed Deposit",

    ("Medium", "Wealth Creation"): "Mutual Fund",
    ("Medium", "Child Education"): "Balanced Fund",
    ("Medium", "House Purchase"): "Balanced Fund",

    ("High", "Wealth Creation"): "Stocks",
    ("High", "Child Education"): "Mutual Fund",
    ("High", "Emergency Fund"): "Gold ETF",
}

rows = []

for _ in range(500):

    age = random.randint(21, 60)

    income = random.randint(25000, 150000)

    expenses = random.randint(10000, income - 5000)

    savings = income - expenses

    investment = random.randint(2000, min(25000, savings))

    goal = random.choice(goals)

    duration = random.randint(2, 25)

    risk = random.choice(risks)

    recommendation = recommendations.get(
        (risk, goal),
        "Mutual Fund"
    )

    rows.append([
        age,
        income,
        expenses,
        savings,
        investment,
        goal,
        duration,
        risk,
        recommendation
    ])

df = pd.DataFrame(rows, columns=[
    "Age",
    "Income",
    "Expenses",
    "Savings",
    "InvestmentAmount",
    "Goal",
    "Duration",
    "Risk",
    "Recommendation"
])

df.to_csv("data/dataset.csv", index=False)

print("Dataset created successfully!")