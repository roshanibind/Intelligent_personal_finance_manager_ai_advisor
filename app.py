import streamlit as st
import pandas as pd
from src.analyzer import calculate_summary
from src.advisor import financial_advice
from src.visualizer import plot_expenses

st.set_page_config(page_title="Personal Finance Manager (AI Advisor)", layout="wide")
st.title("Intelligent Personal Finance Manager (AI Advisor)")

# ---- Initialize Session State ----
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# ---- User Input Form ----
st.subheader("Add Transaction")

with st.form("transaction_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    txn_type = st.selectbox("Type", ["Income", "Expense"])
    amount = st.number_input("Amount", min_value=0.0, step=100.0)
    category = st.text_input("Category")

    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        st.session_state.transactions.append({
            "date": date,
            "description": description,
            "type": txn_type,
            "amount": amount,
            "category": category
        })
        st.success("Transaction added successfully!")

# ---- Convert to DataFrame ----
if st.session_state.transactions:
    df = pd.DataFrame(st.session_state.transactions)

    st.subheader("Transaction History")
    st.dataframe(df)

    # ---- Summary ----
    income, expense, saving = calculate_summary(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹ {income}")
    col2.metric("Total Expense", f"₹ {expense}")
    col3.metric("Savings", f"₹ {saving}")

    # ---- Visualization ----
    st.subheader("Expense Analysis")
    fig = plot_expenses(df)
    st.pyplot(fig)

    # ---- AI Advice ----
    st.subheader("AI Financial Advice")
    advice = financial_advice(income, expense, df)

    for tip in advice:
        st.write("•", tip)
else:
    st.info("No transactions added yet.")
