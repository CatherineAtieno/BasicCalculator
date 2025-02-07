# CODE CRAFTERS PRESENTATION
import random
import operator
import time

def get_random_question():
    """
    Generates a random math question with two numbers and an operation.
    """
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }
    
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(operations.keys()))
    
    # Ensure division is always valid
    if op == '/' and num2 == 0:
        num2 = 1
    
    question = f"{num1} {op} {num2}"
    answer = operations[op](num1, num2)
    
    return question, round(answer, 2)  # Round for better readability

def calculator_game():
    """
    Starts the calculator game where the player solves random math problems.
    """
    print("Welcome to the Python Calculator Game!")
    print("Solve the given math problems. Type 'exit' to quit.")
    
    score = 0  # Player's score
    
    while True:
        question, correct_answer = get_random_question()
        
        try:
            user_input = input(f"What is {question}? ")
            
            if user_input.lower() == 'exit':
                print(f"Game Over! Your final score is {score}")
                break
            
            user_answer = float(user_input)
            
            if user_answer == correct_answer:
                print("Correct! You earn 1 point.")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        
        except ValueError:
            print("Invalid input! Please enter a number or type 'exit' to quit.")
        
        time.sleep(1)

if __name__ == "__main__":
    calculator_game()
