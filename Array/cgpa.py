def calculate_cgpa(grades, credit_hours):
    grade_points = {
        "O": 10.0,
        "A+": 9.0,
        "A": 8.0,
        "B+": 7.0,
        "B": 6.0,
        "C": 5.0,
        "D": 4.0,
        "F": 3.0,
    }

    total_grade_points = sum(
        grade_points.get(grade, 0) * credit
        for grade, credit in zip(grades, credit_hours)
    )
    total_credit_hours = sum(credit_hours)

    cgpa = total_grade_points / total_credit_hours
    return cgpa


# Example usage:
course_grades = ["O", "A+", "B", "A+", "A+", "A", "A+", "O", "O", "A+", "O", "A+"]
credit_hours = [2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1]

result_cgpa = calculate_cgpa(course_grades, credit_hours)
print("CGPA:", result_cgpa)
