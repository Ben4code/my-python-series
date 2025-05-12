import random
import string

def generate_password():
  # Get user inputs
  length = int(input("Enter the desired password length: ").strip())
  include_uppercase = input("Include uppercase letters? (Yes/No) ").strip().lower()
  include_special = input("Include special characters? (Yes/No) ").strip().lower()
  include_digits = input("Include digits? (Yes/No) ").strip().lower()
  
  # Validate password length.
  if length < 4:
    print("Password length cannot be less than 4")
    return
  
  # Form hash
  lower = string.ascii_lowercase
  uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
  special = string.punctuation if include_special == "yes" else ""
  digits = string.digits if include_digits == "yes" else ""
  all_characters = lower + uppercase + special + digits
  
  # Preserve user requirements
  required_characters = []
  if include_uppercase == "yes":
    required_characters.append(random.choice(uppercase))  
  
  if include_special == "yes":
    required_characters.append(random.choice(special))  
  
  if include_digits == "yes":
    required_characters.append(random.choice(digits))  

  # Append rest of hash
  remaining_character_count = length - len(required_characters)
  password = required_characters
  for _ in range(remaining_character_count):
    password.append(random.choice(all_characters))
  
  # Shuffle and parse to string.
  random.shuffle(password)
  return "".join(password)



password = generate_password()
print(password)