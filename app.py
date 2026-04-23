print("PSRA FILE LOADED")
import streamlit as st
import matplotlib.pyplot as plt 
from psra import simulate_survival, calculate_metrics

st.title("Personal Survival Risk Analyzer")

initial_savings = st.number_input("Initial Savings", value= 50000)
income_mean = st.number_input("Monthly Income", value=15000)
income_std = st.number_input("Income Uncertainty", value=2000)

expense_mean = st.number_input("Monthly Expenses", value=12000)
expense_std = st.number_input("Expense Uncertainty", value=2000)

months = st.slider("Simulation Duration (months)", 1, 24, 12)
simulations = st.slider("Number of Simulations", 100, 5000, 1000)

if st.button("Run Analysis"):
        result = simulate_survival(initial_savings, income_mean, income_std, expense_mean, expense_std, months, simulations)
        metrics = calculate_metrics(result, months)

        st.subheader("Results")

        st.write(f"Probability of going broke: **{metrics['probability_broke']:.2%}**")
        st.write(f"Median survival time: **{metrics['median_survival']} months**")
        st.write(f"Worst-case(10th percentile): **{metrics['worst_case']}months**")

        st.subheader("Survival Distribution")

        fig, ax = plt.subplots()
        ax.hist(result["survival_time"], bins=months)
        ax.set_xlabel("Months Survived")
        ax.set_ylabel("Frequency")

        st.pyplot(fig)