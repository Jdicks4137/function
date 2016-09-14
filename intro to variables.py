# Josh Dickey 9/12/16
# this program calculates simple and compound interest and then solves for the difference

# allows computer to ask user to imput values to solve the equation
principle_amount = input("what is the principle amount?")
annual_rate = input("what is the annual interest rate?")
years_transacted = input("how many years was the money deposited or borrowed for?")
times_compounded = input("how many times is the interest compounded?")

# formulas to calculate simple and compound interest and the difference.
simple_interest = float(principle_amount) * float(annual_rate) * float(years_transacted)

compound_interest = float(principle_amount) * (1 + float(annual_rate) / float(times_compounded)) ** \
                                              (float(times_compounded) * float(years_transacted))

difference = compound_interest - simple_interest

# computer displays answers
print("The simple interest is", simple_interest, "and the compound interest is",
      compound_interest, "the difference is", difference)
