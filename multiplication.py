question=input("Enter your multiplication question here: ")
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