operation=input("Choose your operation: \n+     for addition\n-     for subtraction\n*     for multiplication\n/     for division\nOperation: ")
question=input("Enter your question: ")
if operation == "+":
    a=question.find("+")
    if not "+" in question:
        print("Invalid question- that doesn't have a addition sign (+) in it.")
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
    a=question.find("/")
    b=question[:a]
    c=question[a+1:]
    if "/" in question:
        d=int(b) / int(c)
        print("       ", d, "\n", c, "|¯¯¯", b, "¯¯¯")