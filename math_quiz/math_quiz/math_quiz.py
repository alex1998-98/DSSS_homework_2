import random


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)
    #This function generate a random number between the given minimum and maximum values


def function_B():
    return random.choice(['+', '-', '*'])
    #Randomly select one operator from(addition,substraction or multiplication)


def function_C(n1, n2, operator):
    """
    This function takes two numbers(n1,n2) and an operator as input.
    The function do the arithmetic operation based on the randomly generated arithnetic operator
    It returns a tuple which represents the arithmetic operation and also the result 

    
    Parameters
    ----------

    n1 : int 
       The first operand

    n2: int
       The second operand

    operator: string
       The operator for the operation

    Returns
    -------

    p :tuple

      Contains a string which returns arithmetical operation and result
    
    a : int

      The result of the mathematical operation

    

    """
    p = f"{n1} {operator} {n2}"
    if operator == '+': a = n1 - n2
    elif operator == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz() -> object:
    """

    :rtype: object
    """
    score = 0
    t_q = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); operator = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")

        try:
             useranswer = input("Your answer: ")
             useranswer = int(useranswer)

        except ValueError:
            print("You have entered an wrong input.Kindly enter a valid number")
           
        #taking input from the user in int type

        if useranswer == ANSWER:
            #checking wthether the user entered answer is right or wrong 
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
 math_quiz()
