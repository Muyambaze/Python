# Function to get student data (you can change the initial data or extend it later)
def get_student_data():
    # Initial dictionary with names as keys and scores as values
    return {
        "Alice": 87,
        "Babie":61,
        "Bob": 73,
        "Sammie":76,
        "Clara": 92,
        "Daniel": 65,
        "Evelyn": 58,
        "Jackie":46,
    }


# Function to calculate grades based on score
def calculate_grade(score):
    if score >= 90:
        return 'A+'
    elif score >= 80:
        return 'A'
    elif score >= 75:
        return 'B+'
    elif score >= 70:
        return 'B'
    elif score >= 65:
        return 'C+'
    elif score >= 60:
        return 'C'
    elif score >= 55:
        return 'D+'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


# Function to calculate class statistics: min, max, and average score
def class_statistics(*scores):
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return minimum, maximum, average


# Recursive function to sum numbers from 1 to n
def sum_scores(n):
    if n == 1:
        return 1
    return n + sum_scores(n - 1)


# print student grades using
def print_all_student_grades(student_data):
    print("\n--- Student Grades ---")
    for name, score in student_data.items():
        grade = calculate_grade(score)
        print(f"{name}: Score = {score}, Grade = {grade}")


# Function to filter top performers using lambda and filter
def filter_top_performers(student_data):
    scores = student_data.values()
    _, _, average = class_statistics(*scores)
    top_students = dict(filter(lambda item: item[1] > average, student_data.items()))
    return top_students


# Function to interact with user and show student's score and grade
def check_student_score(student_data):
    name = input("Enter student name: ")
    if name in student_data:
        score = student_data[name]
        grade = calculate_grade(score)
        print(f"{name}: Score = {score}, Grade = {grade}")
    else:
        print("Student not found.")


# Function to add a new student to the dictionary
def add_new_student(student_data):
    name = input("Enter new student name: ")
    try:
        score = int(input("Enter score: "))
        student_data[name] = score
        print(f"Added {name} with score {score}")
    except ValueError:
        print("Invalid score. Must be an integer.")


# Menu system to navigate the program
def menu_system():
    student_data = get_student_data()

    while True:
        print("\n=== Student Grade System Menu ===")
        print("1. View all student grades")
        print("2. View class statistics")
        print("3. View top performers")
        print("4. Check student score")
        print("5. Add new student")
        print("6. Recursive sum from 1 to n")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            print_all_student_grades(student_data)
        elif choice == '2':
            stats = class_statistics(*student_data.values())
            print(f"Class Stats → Min: {stats[0]}, Max: {stats[1]}, Avg: {stats[2]:.2f}")
        elif choice == '3':
            top = filter_top_performers(student_data)
            print("--- Top Performers ---")
            for name, score in top.items():
                print(f"{name}: Score = {score}")
        elif choice == '4':
            check_student_score(student_data)
        elif choice == '5':
            add_new_student(student_data)
        elif choice == '6':
            try:
                n = int(input("Enter n: "))
                print(f"Sum from 1 to {n} is {sum_scores(n)}")
            except ValueError:
                print("Invalid input. Enter an integer.")
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")


menu_system()
