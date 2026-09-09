# lab3 for D0009E
# Av Simon Svanberg
# Menysystem för Lab2


# Uppgift 0
'''
Write the number for what you want to do:
1. Bounce numbers
2. Cross sum of the digits of a number
3. Equation solver for f(x)=x^2-1 with Newton-Raphson method

'''
# Google:ade upp hur man gör importerar funktioner från andra mappar
import sys
from pathlib import Path
labs_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(labs_folder))

# Därefter importerades funktioner från systermappen Lab2
from Lab2.lab2_uppg1 import bounce, tvarsumma, solve, f_test1


def lab2_selector(choice):
    # Menyöversikt
    print("Your options:\n" \
    "1. Bounce numbers\n" \
    "2. cross sum of the digits of a number\n" \
    "3. Equation solver for f(x)=x^2-1 with Newton-Raphson method")

    # Basic samling if-satser vilka jämförs med ett input:at nummer för att
    # få önskat "state" i menysystemet.
    if choice == 1:
        print("choice 1")
        n = int(input("Bounce what number: "))
        bounce(n)

                
    elif choice == 2:
        print("choice 2")
        n = int(input("Get the cross sum of what number: "))
        print("Result =", tvarsumma(n))
        
    elif choice == 3:

        print("choice 3\n" \
        "Solver for f(x)=x^2-1")
        x0 = float(input("What starting value: "))
        precision = float(input("What precision/stepsize: "))
        print("Local minimum/maximum at x =", solve(f_test1, x0, precision))
    else:
        print("Not a valid choice")

lab2_selector(int(input("Write the number for what you want to do: ")))
