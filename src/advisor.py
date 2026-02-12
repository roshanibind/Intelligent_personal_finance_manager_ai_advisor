def financial_advice(income, expense):
    advice = []

    if expense > income:
        advice.append("Your expense exceed your income.")
    else:
        advice.append("good job! Your income is higher than expenses.")
    
    if expense > income * 0.7:
        advice.append("Try to reduce unwanted spendings like entertainment.")
    else:
        advice.append("Your spending is under control.")

    return advice