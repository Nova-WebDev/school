from data_access.transaction import Transaction
from data_access.repository import StudentRepository, GradeRepository, SubjectRepository
from business.logic import (
    calculate_average,
    is_student_grade_a,
    is_student_failed_by_average,
    is_subject_failed,
)


def student_report(student_id: int) -> None:
    with Transaction() as cur:
        student = StudentRepository.get_by_id(cur, student_id)
        if not student:
            print("Student not found")
            return

        grades = GradeRepository.filter_by_student(cur, student_id)

        scores = [g["score"] for g in grades]
        avg = calculate_average(scores)
        is_a = is_student_grade_a(scores)
        is_failed_by_avg = is_student_failed_by_average(scores)

        failed_subjects = [g for g in grades if is_subject_failed(g["score"])]
        failed_count = len(failed_subjects)

        min_subject = None
        max_subject = None
        if grades:
            min_subject = min(grades, key=lambda g: g["score"])
            max_subject = max(grades, key=lambda g: g["score"])
            min_subject["subject_name"] = SubjectRepository.get_by_id(cur, min_subject["subject_id"])["name"]
            max_subject["subject_name"] = SubjectRepository.get_by_id(cur, max_subject["subject_id"])["name"]

    print(f"Student: {student['id']} - {student['name']}")
    print(f"Average: {avg if avg is not None else 'None'}")
    print(f"Failed subjects count: {failed_count}")
    print(f"Is A average (>=18): {is_a}")
    print(f"Is failed by average (<12): {is_failed_by_avg}")
    if min_subject:
        print(f"Min score: {min_subject['score']} in {min_subject['subject_name']}")
    if max_subject:
        print(f"Max score: {max_subject['score']} in {max_subject['subject_name']}")
