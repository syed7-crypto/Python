students = {
    "student1": {"name": "Alice", "age": 20, "grade": 85},
    "student2": {"name": "Bob", "age": 22, "grade": 90},
}
next_id = len(students) + 1

def add_student():
    global next_id
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = int(input("Enter student's grade: "))
    students[f"student{next_id}"] = {"name": name, "age": age, "grade": grade}
    next_id += 1


def view_students():
    for student_id, info in students.items():
        print(f"Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")

def search_student():
    s_name = input("Enter student's name to search: ")
    for student_id, info in students.items():
        if info['name'].lower() == s_name.lower():
            print(f"Student Found! \nName: {info['name']}\n Age: {info['age']}\n Grade: {info['grade']}")
            return
    print("Student not found.")

def delete_student():
    s_name = input("Enter student's name to delete: ")
    for student_id, info in students.items():
        if info['name'].lower() == s_name.lower():
            del students[student_id]
            print(f"Student {student_id} deleted Successfully!")
            return
    print("Student not found.")
        
def average_marks():
    total,count=0,0
    for student_id, info in students.items():
        total+= info["grade"]
        count=count+1
    if count == 0:
        print("No students available.")
        return
    avg=total/count   
    print(f"Average grade: {avg}")

def update_student():
    s_name = input("Enter student's name to update: ")
    for student_id, info in students.items():
        if info['name'].lower() == s_name.lower():
            new_name = input("Enter new name (leave blank to keep current): ")
            new_age = input("Enter new age (leave blank to keep current): ")
            new_grade = input("Enter new grade (leave blank to keep current): ")
            if new_name.strip():
                info['name'] = new_name
            if new_age.strip():
                info['age'] = int(new_age)
            if new_grade.strip():
                info['grade'] = int(new_grade)
            print(f"Student {student_id} updated successfully.")
            return
    print("Student not found.")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Students")
        print("4. Delete Student")
        print("5. Average Marks")
        print("6. Update Student")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            average_marks()
        elif choice == 6:
            update_student()
        elif choice == 7:
            break
        else:
            print("Invalid Choice")

main()
    