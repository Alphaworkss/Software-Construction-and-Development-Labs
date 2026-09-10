from dataclasses import dataclass


@dataclass
class Student:
    name: str
    marks: list[float]

    @property
    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    @property
    def grade(self) -> str:
        grading_scale = [
            (80, "A"),
            (70, "B"),
            (60, "C"),
            (50, "D"),
            (0, "F")
        ]

        for minimum, grade in grading_scale:
            if self.average >= minimum:
                return grade

        return "F"


def get_valid_marks(subject: str) -> float:
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Error: Marks must be between 0 and 100.")

        except ValueError:
            print("Error: Please enter a valid number.")


def get_student() -> Student:
    name = input("Enter student's name: ").strip()

    while not name:
        print("Error: Name cannot be empty.")
        name = input("Enter student's name: ").strip()

    subjects = ["Math", "English", "Computer"]
    marks = [get_valid_marks(subject) for subject in subjects]

    return Student(name=name, marks=marks)


def display_result(student: Student) -> None:
    print("\n" + "=" * 35)
    print("        STUDENT RESULT")
    print("=" * 35)
    print(f"Name    : {student.name}")
    print(f"Average : {student.average:.2f}")
    print(f"Grade   : {student.grade}")
    print("=" * 35)


def main() -> None:
    print("Student Grade Calculator")
    print("-" * 35)

    student = get_student()
    display_result(student)


if __name__ == "__main__":
    main()