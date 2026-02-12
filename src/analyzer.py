def calculate_summary(df):
    income = df[df["type"]== "Income"]["amount"].sum()
    expense = df[df["type"]== "Expense"]["amount"].sum()
    saving = income - expense

    return income, expense, saving