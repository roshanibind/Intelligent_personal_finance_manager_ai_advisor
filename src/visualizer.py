import matplotlib.pyplot as plt

def plot_expenses(df):
    expense_df = df[df["type"] == "Expense"]

    fig, ax = plt.subplots()   # ✅ correct function

    expense_df.groupby("category")["amount"].sum().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")
    ax.set_title("Expense Distribution by Category")

    return fig
