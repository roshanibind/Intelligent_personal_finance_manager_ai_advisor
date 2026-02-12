import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.analyzer import calculate_summary
from src.advisor import financial_advice
from src.visualizer import plot_expenses

st.set_page_config(page_title="Personal Finance Manager (AI advisor)", layout = "wide")

st.title(" Intelligent Personal Finance Manage(AI advisor)")

# ---- File Upload ----
uploaded_file = st.file_uploader("Upload your transactions CSV", type=["csv"])

if uploaded_file is not None:
    # 1️⃣ READ DATA FIRST
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Transaction Data")
    st.dataframe(df)

    income, expense, saving = calculate_summary(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"{income}")
    col2.metric("Total Expense", f"{expense}")
    col3.metric("Saving", f"{saving}")

    st.subheader("Expense Analysis")
    fig = plot_expenses(df)
    st.pyplot(fig)

    st.subheader("AI FINANCIAL ADVICE")
    advice = financial_advice(income, expense)
    for tip in advice:
        st.write(".", tip)

else:
    st.info("Please upload a CSV file to begin analysis")

