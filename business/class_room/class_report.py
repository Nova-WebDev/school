from data_access.transaction import Transaction
from data_access.repository import ClassroomRepository, StudentRepository, GradeRepository, SubjectRepository
from business.logic import calculate_average, is_student_grade_a, is_student_failed_by_average


def class_report(classroom_id: int) -> None:
    with Transaction() as cur:
        class_info = ClassroomRepository.get_by_id(cur, classroom_id)
        if not class_info:
            print("Class not found")
            return

        students = StudentRepository.filter_by_classroom(cur, classroom_id)

        failed_count = 0
        a_count = 0
        student_avg = []

        subject_scores = {}

        for student in students:
            grades = GradeRepository.filter_by_student(cur, student["id"])
            scores = [g["score"] for g in grades]
            avg = calculate_average(scores)

            if is_student_failed_by_average(scores):
                failed_count += 1
            if is_student_grade_a(scores):
                a_count += 1

            if avg is not None:
                student_avg.append({"student": student["name"], "avg": avg})

            for g in grades:
                sid = g["subject_id"]
                if sid not in subject_scores:
                    subject_scores[sid] = {}
                subject_scores[sid][student["name"]] = g["score"]

        max_avg_student = max(student_avg, key=lambda s: s["avg"]) if student_avg else None
        min_avg_student = min(student_avg, key=lambda s: s["avg"]) if student_avg else None

        subjects = {s["id"]: s["name"] for s in SubjectRepository.get_all(cur)}

        subject_avg = {
            sid: calculate_average(list(scores.values())) if scores else None
            for sid, scores in subject_scores.items()
        }

        subject_minmax = {}
        for sid, scores_map in subject_scores.items():
            if not scores_map:
                subject_minmax[sid] = {"min": None, "max": None}
                continue
            items = list(scores_map.items())
            min_student, min_score = min(items, key=lambda x: x[1])
            max_student, max_score = max(items, key=lambda x: x[1])
            subject_minmax[sid] = {
                "min": {"score": min_score, "student": min_student},
                "max": {"score": max_score, "student": max_student},
            }

    print(f"Class: {class_info['id']} - {class_info['name']}")
    print(f"Failed students count: {failed_count}")
    print(f"A grade students count: {a_count}")

    if max_avg_student:
        print(f"Highest average: {max_avg_student['avg']} by {max_avg_student['student']}")
    if min_avg_student:
        print(f"Lowest average: {min_avg_student['avg']} by {min_avg_student['student']}")

    print("Subject averages:")
    for sid, avg in subject_avg.items():
        if avg is not None:
            print(f"  {subjects.get(sid, f'Subject {sid}')}: {avg}")

    print("Subject min/max scores:")
    for sid, mm in subject_minmax.items():
        subject_name = subjects.get(sid, f"Subject {sid}")
        if mm["min"]:
            print(f"  {subject_name} - Min: {mm['min']['score']} by {mm['min']['student']}")
        if mm["max"]:
            print(f"  {subject_name} - Max: {mm['max']['score']} by {mm['max']['student']}")
