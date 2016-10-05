# Josh Dickey 10/5/16
# this program generates a random math problem in either addition, subtraction, or multiplication
import random


def maximum_value():
    """this allows the user to insert the maximum value"""
    maximum = float(input("what is the maximum value?"))
    return maximum


def correct_answer(problem, x, y):
    """this is the correct answer to the problem which is calculated by the program"""
    if problem == '-':
        return x - y
    elif problem == '*':
        return x * y
    else:
        return x + y


def response():
    """this allows the program to receive a response from the user"""
    respond = float(input("your answer"))
    return respond


def operation():
    """this allows the user to select the type of problem they wish to solve"""
    problem_type = input("please select the type of problem you want: addition, subtraction, or multiplication.")
    return problem_type


def main():
    """this is the main function that runs the program"""
    maximum = maximum_value()
    problem = operation()
    x = random.randint(0, maximum)
    y = random.randint(0, maximum)
    print("what is", x, problem, y)
    user_answer = response()
    if user_answer == correct_answer(problem, x, y):
        print("You are correct! Thanks for playing.")
    else:
        print("You suck at math. Honestly how can you not solve", x, problem, y, "? The correct answer was",
              correct_answer(problem, x, y), "You don't deserve to play this game again! Goodbye!")


main()
