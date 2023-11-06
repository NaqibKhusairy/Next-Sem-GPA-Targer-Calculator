dash = "-" * 43

table1 = [
    ["1", "Calculate Target For Next Semester"],
    ["2", "Exit"]
]

print(dash)
print("Welcome To GPA Target Calculator")

while True:
    print(dash)
    for row in table1:
        for col in row:
            print(col, end="\t")
        print()
    print(dash)
    try:
        userchoose = int(input("Please Choose: "))

        if userchoose == 1:
            name = input("Enter Your Name: ")
            print(dash)
            while True:
                print(f"Hi {name}, Welcome to GPA Target Calculator\n"+dash)
                totalsem = input("Enter how many semesters you have completed or [x] to exit: ")
                print(dash)

                if totalsem.lower() == 'x':
                    print("Thank you for using Our System\nBye Bye!!!")
                    exit()

                try:
                    totalsem = int(totalsem)
                    if totalsem < 0:
                        print("Invalid input. Number of semesters should be a positive integer.")
                        print(dash)
                    else:
                        #calculate
                except ValueError:
                    print("Invalid input")
                    print(dash)
        elif userchoose == 2:
            print("Thank you for using Our System\nBye Bye!!!")
            exit()
        else:
            print("Invalid Choice!!!")
    except ValueError:
        print("Invalid Choice!!!")
