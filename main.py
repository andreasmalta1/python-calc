import math


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def sq_root(num1):
    return math.sqrt(num1)


def power_of(num1, num2):
    return math.pow(num1, num2)


mem = None


def input_nums():
    global mem
    print("Enter sqrt num for square root")
    while True:
        a = input("Please input number 1: ")
        if a == "mem" and mem:
            a = mem
            print(f"Memorised number is: {mem}")
            break
        elif a == "mem" and not mem:
            print("Memory is empty")
        else:
            a = float(a)
            break
    while True:
        b = input("Please input number 2: ")
        if b == "mem" and mem:
            b = mem
            print(f"Memorised number is: {mem}")
            break
        elif b == "mem" and not mem:
            print("Memory is empty")
        else:
            b = float(b)
            break

    while True:
        while True:
            operator = input("Please enter operator '+' '-' '*' '/': ")
            if operator == "+":
                answer = addition(a, b)
                if answer - int(answer) == 0:
                    answer = int(answer)
                print(answer)
                break
            elif operator == "-":
                answer = subtraction(a, b)
                if answer - int(answer) == 0:
                    answer = int(answer)
                print(answer)
                break
            elif operator == "*":
                answer = multiplication(a, b)
                if answer - int(answer) == 0:
                    answer = int(answer)
                print(answer)
                break
            elif operator == "/":
                answer = division(a, b)
                if answer - int(answer) == 0:
                    answer = int(answer)
                print(answer)
                break
            else:
                print("Try Again")

        while True:
            keep_val = input("Enter 'c' to start again | 'k' to keep value | 'm' to memorise value: ").lower()
            if keep_val == "c":
                input_nums()
            elif keep_val == "m":
                mem = answer
                input_nums()
            elif keep_val == "k":
                a = answer
                print(f"Number 1 = {a}")
                b = float(input("Please input number 2: "))
                break
            else:
                print("Try Again")


input_nums()

print(sq_root(64))
print(sq_root(122))
print(power_of(5, 5))
print(power_of(7, 9))
