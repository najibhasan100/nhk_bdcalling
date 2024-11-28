employeelist = []

choice = 0

while choice != 6:
    try:
        print("**** ABC Company Employee List ****")
        print("1. Add Employee")
        print("2. Update Employee Info")
        print("3. Delete Employee")
        print("4. Display Employees")
        print("5. Search Employee")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("#### Add an Employee ####")
            nemployee = input("Enter Employee Name: ")
            nposition = input("Enter Employee Position: ")
            nnumber = int(input("Enter Employee Number: "))
            nphone = int(input("Enter Employee Phone: "))
            employeelist.append([nemployee, nposition, nnumber, nphone])
            print("Employee Added Successfully!")
        elif choice == 2:
            print("##### Update Employee Info #####")
            index = input("Enter the Employee Name: ")
            for employee in employeelist:
                if employee[0] == index:
                    print(f"Current Info: {employee}")
                    employee[1] = input("Enter New Position: ")
                    employee[2] = int(input("Enter New Number: "))
                    employee[3] = int(input("Enter New Phone: "))
                    print("Employee Info Updated!")
                    break
            else:
                print("Employee Not Found")
        elif choice == 3:
            print("##### Delete Employee #####")
            dtar = input("Enter Employee Name to Delete: ")
            for employee in employeelist:
                if employee[0] == dtar:
                    employeelist.remove(employee)
                    print("Employee Deleted!")
                    break
            else:
                print("Employee Not Found")
        elif choice == 4:
            print("##### All Employees #####")
            if not employeelist:
                print("No Employees in the List.")
            else:
                for employee in employeelist:
                    print(f"Name: {employee[0]}, Position: {employee[1]}, Number: {employee[2]}, Phone: {employee[3]}")
        elif choice == 5:
            print("##### Search Employee #####")
            target = input("Enter Employee Name to Search: ")
            for employee in employeelist:
                if employee[0] == target:
                    print(f"Found Employee: {employee}")
                    break
            else:
                print("Employee Not Found")
        elif choice == 6:
            print("Program Exit")
        else:
            print("Enter a Valid Number Between 1 and 6")
    except ValueError:
        print("Invalid Input! Please Enter a Valid Number.")
