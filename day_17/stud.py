students = []


def studBase():
    print("Select an operation:")
    print("1. Register student")
    print("2. Update student Info")
    print("3. Delete student info")
    print("4. Display all students")
    print("5. Exit")

    while True:
        try:
            choice = input("Enter an option: \n")
            if choice not in ["1", "2", "3", "4", "5"]:
                raise ValueError("Invalid choice")

            # Process student name only when required
            if choice in ["1", "2", "3"]:
                name = input("Enter your name: \n")
                level = input("Enter your class: \n")
                if not level.isnumeric():
                    print("Please enter a valid class (numeric).")
                    continue
            # Handle each option
            if choice == "1":  # Register student
                studInfo = {"name": name, "class": level}
                students.append(studInfo)
                print(f"Student {name} registered successfully.")

            elif choice == "2":  # Update student info
                student_found = False
                for student in students:
                    if student["name"] == name:
                        student_found = True
                        print(
                            f'Current info - Name: {student["name"]}, Class: {student["class"]}'
                        )
                        new_level = input("Enter your new class: \n")
                        if new_level.isnumeric():
                            student["class"] = new_level
                            print(f"Student {name} updated successfully.")
                            break
                        else:
                            print("Please enter a valid class (numeric).")
                            break
                if not student_found:
                    print(f"Student {name} not found.")

            elif choice == "3":  # Delete student info
                student_found = False
                for student in students:
                    if student["name"] == name:
                        student_found = True
                        students.remove(student)
                        print(f"Student {name} deleted successfully.")
                        break
                if not student_found:
                    print(f"Student {name} not found.")

            elif choice == "4":  # Display all students
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(f'Name: {student["name"]}, Class: {student["class"]}')

            elif choice == "5":  # Exit
                print("Exiting the program.")
                break

        except ValueError:
            print("Invalid input. Please try again.")

        finally:
            new_choice = input("Do you wish to continue (yes/no)? ")
            if new_choice.lower() != "yes":
                print("Exiting program.")
                break


# Start the student management system
studBase()
