# Josh Dickey 9/21/16
# This program solves quadratic equations


def print_instructions():
    """This gives the user instructions and information about the program"""
    print("This program will solve any quadratic equation. You will be asked to input the values for "
          "a, b, and c to allow the program to solve the equation.")


def get_first_coefficient():
    """This allows the user to input the values for a"""
    a = float(input("what is the value of a?"))
    return a


def get_second_coefficient():
    """This allows the user to input the values for b"""
    b = float(input("what is the value of b?"))
    return b


def get_third_coefficient():
    """This allows the user to input the values for c"""
    c = float(input("what is the value of c?"))
    return c


def calculate_roots(a, b, c):
    """this is the formula the computer will calculate"""
    x = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    y = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    return x, y


def main():
    """this is the function that runs the entire program"""
    print_instructions()
    first_coefficient = get_first_coefficient()
    second_coefficient = get_second_coefficient()
    third_coefficient = get_third_coefficient()
    root1, root2 = calculate_roots(first_coefficient, second_coefficient, third_coefficient)
    print("the first root is:", root1, "and the second root is:", root2)


main()