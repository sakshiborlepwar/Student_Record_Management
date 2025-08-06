import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')
conn.commit()

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (name, age, grade))
    conn.commit()
    print("Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    print("------------------------")


def search_student():
    student_id = input("Enter student ID to search: ")
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row:
        print(f"\nID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter student ID to update: ")
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if cursor.fetchone() is None:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    age = input("Enter new age: ")
    grade = input("Enter new grade: ")

    cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?",
                   (name, age, grade, student_id))
    conn.commit()
    print("Student updated successfully.")


def delete_student():
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student deleted successfully.")


def main():
    while True:
        print("\n==== Student Record Management System ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()


if __name__ == "__main__":
    main()
