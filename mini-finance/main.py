# --- Virtual Environment Setup ---
# python3 -m venv .venv
# source .venv/bin/activate
# deactivate



import pandas as pd
import csv
from datetime import datetime 
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt



class CSV:
  CSV_FILE = "finance_data.csv"
  COLUMNS = ["date", "amount", "category", "description"]
  DATE_FORMAT = "%d-%m-%Y"
  
  @classmethod
  def initialize_csv(cls):
    try:
      # date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press 'Enter' for today's date.", allow_default=True)
      # amount = get_amount()
      # category = get_category()
      # description = get_description()
  
      pd.read_csv(cls.CSV_FILE)
      # CSV.add_entry(date, amount, category, description)
    except FileNotFoundError:
      df = pd.DataFrame(columns=cls.COLUMNS)
      df.to_csv(cls.CSV_FILE, index=False)

  @classmethod
  def add_entry(cls, date, amount, category, description):
    new_entry = {
      "date": date,
      "amount": amount,
      "category": category,
      "description": description
    }
    with open(cls.CSV_FILE, "a", newline="") as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
      writer.writerow(new_entry)
    print("Entry added successfully...")
  
  @classmethod
  def get_transactions(cls, start_date, end_date): 
    df = pd.read_csv(cls.CSV_FILE)
    df["date"] = pd.to_datetime(df["date"], format=CSV.DATE_FORMAT)
    start_date = datetime.strptime(start_date, CSV.DATE_FORMAT) 
    end_date = datetime.strptime(end_date, CSV.DATE_FORMAT) 
    
    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    filtered_df = df.loc[mask]
    
    if filtered_df.empty:
      print("No tranasctions found in the given date range.")
    else:
      print(f"Transactions from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}")
      print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.DATE_FORMAT)}))
      total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
      total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
      print("\nSummary:")
      print(f"Total Income: ${total_income:.2F}")
      print(f"Total Expense: ${total_expense:.2F}")
      print(f"Net Savings: ${(total_income - total_expense):.2f}")
      
      return filtered_df

def add():
  date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press 'Enter' for today's date.", allow_default=True)
  amount = get_amount()
  category = get_category()
  description = get_description()
  CSV.initialize_csv()
  CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
  df.set_index("date", inplace=True)
  income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
  expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

  plt.figure(figsize=(10, 5))
  plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
  plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
  plt.xlabel("date")
  plt.ylabel("amount")
  plt.title("Income and Expense over time")
  plt.legend()
  plt.grid(True)
  plt.show()
  
  
def main():
  while True:
    print("\n1. Add a new transaction")
    print("\n2. View existing transactions")
    print("\n3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
      add()
    elif choice == "2":
      start_date = get_date("Enter the start_date (dd-mm-YYYY): ")
      end_date = get_date("Enter the end  _date (dd-mm-YYYY): ")
      df = CSV.get_transactions(start_date, end_date)
      
      if input("Do you want to plot see a plot? (Yes/No) ").lower() == "yes":
        plot_transactions(df)
        
    elif choice == "3":
      print("Exiting...")
      break
    else:
      print("Invalid choice, enter 1, 2 or 3. ")
      
if __name__ == "__main__":
  main()