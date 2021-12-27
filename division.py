question=input("Enter your division question here: ")
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