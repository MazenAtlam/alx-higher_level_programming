#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    import calculator_1 as calc
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = str(argv[2])
    b = int(argv[3])
    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.sub(a, b)
    elif op == "*":
        result = calc.mul(a, b)
    elif op == "/":
        if b == 0:
            exit(1)

        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, op, b, result))
