from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {
  "I": "Income",
  "E": "Expense"
}

def get_date(prompt, allow_default=False):
  date_str = input(prompt)
  
  if allow_default and not date_str:
    return datetime.today().strftime(date_format)
  
  try:
    valid_date = datetime.strptime(date_str, date_format)
    return valid_date.strftime(date_format)
  except ValueError: 
    print("Invalid date format. Please enter correct date format in dd-mm-YYYY.")
    return get_date(prompt, allow_default)

def get_amount():
  try:
    amount = float(input("Enter an amount: " ))
    if amount <= 0:
      raise ValueError("Amount must be a positive number ")
    return amount
  except ValueError as e:
    print(e)
    return get_amount()     

def get_description():
  try:
    description = str(input("Enter a description: "))
    if len(description) < 3:
      print("Description must be at least 4 characters long.")
    return description
  except ValueError as e:
    print(e)
    return get_description ()   

def get_category():
  try:
    category = str(input("Enter a category ('I' for Income or 'E' for Expense): ")).upper()
    if category not in CATEGORIES:
      print("Please enter  'I' for Income or 'E' for Expense")
      return get_category()
    return CATEGORIES[category]
  except ValueError as e:
    print(e)
    return get_category()   