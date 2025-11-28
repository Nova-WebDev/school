from data_access.transaction import Transaction
from data_access.repository import SchoolRepository, ClassroomRepository, StudentRepository, GradeRepository
from business.logic import calculate_average, is_student_grade_a, is_student_failed_by_average


def school_report(school_id: int) -> None:
    with Transaction() as cur:
        school_info = SchoolRepository.get_by_id(cur, school_id)
        if not school_info:
            print("School not found")
            return

        classrooms = ClassroomRepository.filter_by_school(cur, school_id)

        failed_count = 0
        a_count = 0
        class_avgs = []

        for classroom in classrooms:
            students = StudentRepository.filter_by_classroom(cur, classroom["id"])
            class_scores = []

            for student in students:
                grades = GradeRepository.filter_by_student(cur, student["id"])
                scores = [g["score"] for g in grades]
                avg = calculate_average(scores)

                if is_student_failed_by_average(scores):
                    failed_count += 1
                if is_student_grade_a(scores):
                    a_count += 1

                if avg is not None:
                    class_scores.append(avg)

            class_avg = calculate_average(class_scores)
            class_avgs.append({"class": classroom["name"], "avg": class_avg})

        best_class = max([c for c in class_avgs if c["avg"] is not None], key=lambda c: c["avg"], default=None)
        worst_class = min([c for c in class_avgs if c["avg"] is not None], key=lambda c: c["avg"], default=None)

    print(f"School: {school_info['id']} - {school_info['name']}")
    print(f"Failed students count: {failed_count}")
    print(f"A grade students count: {a_count}")

    print("Class averages:")
    for c in class_avgs:
        if c["avg"] is not None:
            print(f"  {c['class']}: {c['avg']}")

    if best_class:
        print(f"Best class: {best_class['class']} with avg {best_class['avg']}")
    if worst_class:
        print(f"Worst class: {worst_class['class']} with avg {worst_class['avg']}")
