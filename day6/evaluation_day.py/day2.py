
question = input(print("Enter question number(From 1-10):"))

match question:
    case 1:

        #Q1 BUs Reservation System
        destination = input("Enter destination (Kolkata/Delhi/Mumbai) ")
        student = input("Are you a student? (yes/no): ")

        fare = 0
        if destination == "Kolkata":
            fare = 500
        elif destination == "Delhi":
            fare = 800

        elif destination == "Mumbai":
            fare = 1200

        if student == "yes":
            fare = fare*0.9 #10% discount

        print("Total Fare : ", fare)


    case 2:
        #Q2
        ratings =[4,5,3,4,5]
        print(ratings)
        avg = sum(ratings)/len(ratings)
        print(avg)
        if avg >= 4.5:
            print("Excellent")
        elif avg >= 3.5:
            print("Good")
        else:
            print("Needs Improvement")

        
    case 3:
        #Q3

        print("1. Burger - 100")
        print("2. Pizza - 200")
        print("3. Sandwich - 80")

        choice = int(input("Enter choice: "))
        qty = int(input("Enter quantity: "))

        match choice:
            case 1:
                total = 100 * qty
            case 2:
                total = 200 * qty
            case 3:
                total = 80 * qty
            case _:
                total = 0
                print("Invalid Choice")

        print("Total Bill =", total)


    case 4:
        #4
        marks= {
            "Phy" : 98,
            "Che" : 89,
            "Eng" : 78
        }
        total = sum(marks.values())
        percentage = total/len(marks)

        print("Percentage =", percentage)

        if percentage >= 90:
            print("Grade : A")
        elif percentage >= 80:
            print("Grade : B")
        elif percentage >= 70:
            print("Grade : C")
        else:
            print("Grade : D")

    case 5:

        #Q5
        vehicles = {"WB01A1234","WB02A5678"}
        new_vehicles = input("Enter vehicles number: ")

        if new_vehicles in vehicles:
            print("Duplicate Registration:")
        else:
            vehicles.add(new_vehicles)
            print("Registration Successfull")

    case 6:

        #Q6
        days = input("Enter late days: ")

        if days <= 5:
            fine = days * 2
        elif days <= 10:
            fine = days * 5
        else:
            fine = days * 10

        print("Fine Amount =",fine)


    case 7:
        #Q7
        choice = input(print("Enter choices: (1:Triangle, 2:Square, 3:Diamond)" ))
        match choice:
            case 1:
                n = 5

                for i in range(1, n + 1):
                    print("*" * i)

            case 2:

                n = 5

                for i in range(n):
                    print("*" * n)

            case 3:
                n = 5

                for i in range(1, n + 1):
                    print(" " * (n - i) + "*" * (2 * i - 1))

                for i in range(n - 1, 0, -1):
                    print(" " * (n - i) + "*" * (2 * i - 1))

    case 8:

        #Q8
            ratings = [4, 5, 3, 4, 5]

            average = sum(ratings) / len(ratings)

            print("Average Feedback Score =", average)

    case 9:

        #Q9
        employees = {
            101: "Rahul",
            102: "Amit",
            103: "Priya"
        }
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee Name:", employees[emp_id])
        else:
            print("Employee Not Found")


    case 10:

        #Q10

        club1 = {"Rahul", "Amit", "Priya", "Riya"}
        club2 = {"Priya", "Riya", "Suman", "Ankit"}

        common = club1.intersection(club2)

        print("Common Members:")
        print(common)












        













    
    








