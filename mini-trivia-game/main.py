import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "bool",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def trivia_game():
  question_list = list(questions.keys())
  total_questions = 5
  player_score = 0
  selected_question = random.sample(question_list, total_questions)
  
  for idx, question in enumerate(selected_question):
    print(f"{idx + 1}. {question}")
    user_answer = input("Enter your answer: ").lower().strip()

    if questions[question] == user_answer:
      print("Correct answer! \n")
      player_score += 1
    else: 
      print("Incorrect answer! \n")
      
  print(f"Your total score is {player_score}/{total_questions}")
    
trivia_game()