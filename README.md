## `README.md`

```md
# Intelligent Personal Finance Manager (AI Advisor)

An AI-powered web application that helps users analyze their income, expenses, savings, and provides basic financial advice using data analysis.

---

##  Features
- Upload transaction data (CSV)
- Calculate total income, expenses, and savings
- Visualize expenses by category
- Get simple AI-based financial advice
- Easy-to-use Streamlit interface

---

##  Tech Stack
- Python
- Streamlit
- Pandas
- Matplotlib

---

## Project Structure
```

personal_finance_manager/
│
├── app.py
├── data/
│   └── expenses.csv
├── src/
│   ├── analyzer.py
│   ├── advisor.py
│   ├── visualizer.py
│   └── data_loader.py
├── requirements.txt
└── README.md

````

---

## 📊 Sample CSV Format
```csv
date,description,type,amount,category
2025-01-01,Salary,Income,50000,Job
2025-01-05,Rent,Expense,18000,Rent
````

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##AI Logic

* Income and expense summary using Pandas
* Expense visualization using Matplotlib
* Rule-based AI advice based on spending patterns

---

## Future Improvements

* Monthly trend analysis
* ML-based expense prediction
* Advanced AI financial recommendations

---

## 👩‍💻 Author

**Roshani**

````

---


