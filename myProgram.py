# Name: Garry Singh
# Assignment: Assignment 7 myProgram.py
import random

test_bank = [
  {"Question": "1 + 1", "Answer": "2"},
  {"Question": "2 + 2", "Answer": "4"},
  {"Question": "3 + 3", "Answer": "6"},
  {"Question": "4 + 4", "Answer": "8"},
  {"Question": "5 + 5", "Answer": "10"},
  {"Question": "1 + 2", "Answer": "3"},
  {"Question": "2 + 3", "Answer": "5"},
  {"Question": "3 + 4", "Answer": "7"},
  {"Question": "4 + 5", "Answer": "9"},
  {"Question": "5 + 3", "Answer": "8"},
  {"Question": "2 - 1", "Answer": "1"},
  {"Question": "5 - 2", "Answer": "3"},
  {"Question": "6 - 3", "Answer": "3"},
  {"Question": "8 - 4", "Answer": "4"},
  {"Question": "10 - 5", "Answer": "5"},
  {"Question": "2 × 2", "Answer": "4"},
  {"Question": "3 × 2", "Answer": "6"},
  {"Question": "4 × 2", "Answer": "8"},
  {"Question": "6 ÷ 2", "Answer": "3"},
  {"Question": "10 ÷ 2", "Answer": "5"}
]


def choose_question(test_bank: list[dict]) -> dict:
    return random.choice(test_bank)

def run_quiz(num_of_questions : int, test_bank: list[dict]) -> int:
    
    total_correct = 0

    for i in range(1, num_of_questions+1):
        question = choose_question(test_bank)
        ans = input(f"\nWhat is {question["Question"]}: ")

        if ans == question["Answer"]:
            print("Correct")
            total_correct += 1
        else:
            print(f"The correct answer was {question["Answer"]}")
    
    return total_correct




def main() -> None:
    print("\nWelcome to the simple math quiz")
    num_of_questions = int(input("How many questions would you like to solve? 1-20: "))
    num_Correct = run_quiz(num_of_questions, test_bank)

    print(f"\nYou got {num_Correct} out of {num_of_questions} which is {(num_Correct/num_of_questions)*100:.0f}%")


if __name__ == "__main__":
    main()