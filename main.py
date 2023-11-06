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
                print(f"Hi {name.upper()}, Welcome to GPA Target Calculator\n{dash}")
                totalsem = input("Enter how many semesters you have completed or [x] to exit: ")
                print(dash)

                if totalsem.lower() == 'x':
                    print("Thank you for using Our System\nBye Bye!!!")
                    exit()
                else:
                    try:
                        totalsem = int(totalsem)
                        if totalsem < 0:
                            print("Invalid input. Number of semesters should be a positive integer.")
                            print(dash)
                        else:
                            totalgpa = 0
                            sem = 1
                            while sem <= totalsem :
                                try:
                                    gpa = float(input(f"Please enter your GPA for Semester {sem}: "))

                                    if gpa > 4 or gpa < 0:
                                        print("Invalid input !!")
                                        print(dash)
                                        sem -= 1
                                    else : 
                                        totalgpa +=gpa
                                except ValueError:
                                    print("Invalid input !!")
                                    print(dash)
                                    sem -= 1
                                sem += 1

                            try:
                                if gpa <= 4 and gpa >= 0 :
                                    cgpa = totalgpa / totalsem
                                print(f"Your CGPA for Sem {totalsem} = {cgpa:.2f}")
                                target = 3.5 * (totalsem + 1) - totalgpa

                                if cgpa >= 3.5 :
                                    print(dash)
                                    print(f"{name.upper()}!!!, Just Maintain your Pointer and you can get Dekan\n"+dash)
                                else :
                                    if target <= 4 : 
                                        print(dash)
                                        print(f"{name.upper()}!!!, You Must Target At Least {target:.2f} for your GPA in Semester {totalsem+1} "+
                                            "to get CGPA 3.5 to Get Dean\n"+dash)
                                    else :
                                        target = (3.5*totalsem-totalgpa)/0.5
                                        print(dash)
                                        print(f"{name.upper()}!!!, You must work harder so that you can get the desired pointer "+
                                             f"because to get a CGPA of 3.5, you need to get a GPA of 4.0 every Semester for {target+1} Semester\n"+dash)
                                break
                            except:
                                break

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
