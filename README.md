# personal-survival-risk-analyzer 
 Personal Survival Risk Analyzer (PSRA)

 Overview

The Personal Survival Risk Analyzer (PSRA) is a Monte Carlo–based simulation tool that estimates how long an individual can sustain their finances under uncertainty.

Instead of assuming fixed income and expenses, this model simulates thousands of possible financial scenarios to answer:

«“What are the chances I run out of money, and how long can I survive?”»

---

 Key Idea

This project uses Monte Carlo Simulation:

- Repeats a financial scenario many times (e.g., 1000 simulations)
- Introduces randomness in income and expenses
- Tracks when savings run out

This allows us to estimate:

- Probability of going broke
- Typical survival time
- Worst-case outcomes

---

 Features

-  Monte Carlo Simulation Engine
-  Randomized income and expense modeling
- Survival time distribution visualization
-  Risk metrics:
  - Probability of going broke
  - Median survival time
  - Downside risk (10th percentile)
-  Interactive UI built with Streamlit

---

Model Logic

Each simulation follows:

[
Savings_{t} = Savings_{t-1} + Income_{t} - Expense_{t}
]

Where:

- Income and Expense are random variables (Normal Distribution)
- Simulation stops when savings ≤ 0

---

 Outputs

The app provides:

- Probability of Bankruptcy
- Median Survival Time
- Downside Risk (10th percentile survival)
- Histogram of survival durations

---

 Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Streamlit

---

 How to Run

1. Clone the repository

git clone https://github.com/your-username/psra.git
cd psra

2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py

---

 Inputs

Users can adjust:

- Initial Savings
- Monthly Income (mean + uncertainty)
- Monthly Expenses (mean + uncertainty)
- Simulation Duration
- Number of Simulations

---

 Example Use Cases

- Evaluating financial stability before taking an internship
- Comparing cost of living between cities
- Budget planning under uncertainty
- Stress-testing personal finances

---

 Assumptions & Limitations

- Income and expenses follow a normal distribution
- No structural changes (e.g., job loss, promotions unless added)
- No inflation or long-term trends (can be extended)

---

 Future Improvements

- Add inflation and income growth
- Introduce shock events (job loss, medical emergencies)
- Scenario comparison (e.g., City A vs City B)
- Savings trajectory visualization
- Deployment as a public web app

---

 What This Project Demonstrates

- Understanding of probabilistic modeling
- Application of Monte Carlo simulation
- Ability to translate math → real-world decision tool
- Building interactive analytical tools with Python

---

 Author

dubois100

---

