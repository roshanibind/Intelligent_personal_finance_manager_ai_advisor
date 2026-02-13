def financial_advice(income, expense, df):
    advice = []

    if income == 0:
        advice.append(" No income recorded. Add income to generate advice.")
        return advice

    savings = income - expense
    savings_rate = (savings / income) * 100

    advice.append(f" Savings Rate: {savings_rate:.1f}%")

    # ---- Basic Financial Health ----
    if savings_rate < 20:
        advice.append(" You are saving less than 20% of your income. Increase savings immediately.")
    elif savings_rate < 40:
        advice.append(" Try increasing savings to at least 40% of income.")
    else:
        advice.append("Good savings discipline. Keep maintaining this level.")

    # ---- Category Analysis ----
    expense_df = df[df["type"] == "Expense"]
    category_spend = expense_df.groupby("category")["amount"].sum()

    advice.append("Category Spending Analysis:")

    for category, amount in category_spend.items():
        percent = (amount / income) * 100

        if percent > 30:
            reduction_target = amount * 0.2
            advice.append(
                f"'{category}' is {percent:.1f}% of income. "
                f"Reduce it by approx ₹{reduction_target:.0f} and redirect to savings/investments."
            )

        elif percent < 5:
            advice.append(
                f"'{category}' spending is under control ({percent:.1f}%)."
            )

    # ---- 50-20-30 Rule Suggestion ----
    needs_limit = income * 0.5
    wants_limit = income * 0.2
    savings_target = income * 0.3

    advice.append("Suggested Budget (50-20-30 Rule):")
    advice.append(f"   • Needs (50%): ₹{needs_limit:.0f}")
    advice.append(f"   • Wants (20%): ₹{wants_limit:.0f}")
    advice.append(f"   • Savings (30%): ₹{savings_target:.0f}")

    if savings < savings_target:
        gap = savings_target - savings
        advice.append(
            f" Increase savings by ₹{gap:.0f}. Reduce discretionary expenses like Entertainment/Shopping."
        )

    # ---- Emergency Fund Advice ----
    advice.append("Build an emergency fund equal to 3–6 months of expenses.")

    return advice
