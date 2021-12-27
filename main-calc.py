operation=input("Choose your operation: \n+     for addition\n-     for subtraction\n*     for multiplication\n/     for division\n")
question=input("Enter your question: ")
if operation == "+":
    a=question.find("+")
    if not "+" in question:
        print("Invalid question- that doesn't have a addition sign (+) in it.")
    question=input("Enter your addition question here: ")
    a=question.find("+")
    b=question[:a]
    c=question[a+1:]
    if "+" in question:
        d=int(b) + int(c)
        print("\n", b, "+", "\n", c, "\n", "____", "\n", d)
if operation == "-":
    a=question.find("-")
    if not "-" in question:
        print("Invalid question- that doesn't have a subtraction sign (-) in it.")
    question=input("Enter your subtraction question here: ") 
    a=question.find("-")
    b=question[:a]
    c=question[a+1:]
    if "-" in question:
        d=int(b) - int(c)
        print("\n", b, "-", "\n", c, "\n", "____", "\n", d)
if operation == "*":
    a=question.find("*")
    if not "*" in question:
        print("Invalid question- that doesn't have a multiplication sign (*) in it.")
    question=input("Enter your multiplication question here: ")
    a=question.find("*")
    b=question[:a]
    c=question[a+1:]
    if "*" in question:
        d=int(b) * int(c)
        print("\n", b, "*" "\n", c, "\n", "____", "\n", d)
if operation == "/":
    a=question.find("/")
    if not "/" in question:
        print("Invalid question- that doesn't have a division sign (/) in it.")
    question=input("Enter your division question here: ")
    a=question.find("/")
    b=question[:a]
    c=question[a+1:]
    if "/" in question:
        d=int(b) / int(c)
        print("       ", d, "\n", b, "|¯¯¯", c, "¯¯¯")