from data_access.transaction import Transaction
from data_access.repository import AreaRepository, SchoolRepository, ClassroomRepository, StudentRepository, GradeRepository
from business.logic import calculate_average, is_student_grade_a, is_student_failed_by_average


def area_report(area_id: int) -> None:
    with Transaction() as cur:
        area_info = AreaRepository.get_by_id(cur, area_id)
        if not area_info:
            print("Area not found")
            return

        schools = SchoolRepository.filter_by_area(cur, area_id)

        failed_count = 0
        a_count = 0
        school_avg_list = []

        for school in schools:
            classrooms = ClassroomRepository.filter_by_school(cur, school["id"])
            school_scores = []

            for classroom in classrooms:
                students = StudentRepository.filter_by_classroom(cur, classroom["id"])
                for student in students:
                    grades = GradeRepository.filter_by_student(cur, student["id"])
                    scores = [g["score"] for g in grades if isinstance(g, dict) and "score" in g]

                    if scores:
                        if is_student_failed_by_average(scores):
                            failed_count += 1
                        if is_student_grade_a(scores):
                            a_count += 1
                        avg = calculate_average(scores)
                        if avg is not None:
                            school_scores.append(avg)

            school_avg = calculate_average(school_scores)
            school_avg_list.append({"school": school["name"], "avg": school_avg})

        best_school = max([s for s in school_avg_list if s["avg"] is not None], key=lambda s: s["avg"], default=None)
        worst_school = min([s for s in school_avg_list if s["avg"] is not None], key=lambda s: s["avg"], default=None)

    print(f"Area: {area_info['id']} - {area_info['name']}")
    print(f"Failed students count: {failed_count}")
    print(f"A grade students count: {a_count}")

    print("School averages:")
    for s in school_avg_list:
        if s["avg"] is not None:
            print(f"  {s['school']}: {s['avg']}")

    if best_school:
        print(f"Best school: {best_school['school']} with avg {best_school['avg']}")
    if worst_school:
        print(f"Worst school: {worst_school['school']} with avg {worst_school['avg']}")
