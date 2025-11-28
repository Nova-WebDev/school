from data_access.transaction import Transaction
from data_access.repository import (
    SubjectRepository,
    GradeRepository,
    StudentRepository,
    ClassroomRepository,
    SchoolRepository,
    AreaRepository,
)
from business.logic import calculate_average, is_subject_failed


def subject_report(subject_id: int) -> None:
    with Transaction() as cur:
        subject = SubjectRepository.get_by_id(cur, subject_id)
        if not subject:
            print("Subject not found")
            return

        grades = GradeRepository.filter_by_subject(cur, subject_id)

        failed_count = 0
        class_scores: dict[int, list[float]] = {}
        school_scores: dict[int, list[float]] = {}
        area_scores: dict[int, list[float]] = {}

        for g in grades:
            score = g["score"]
            student = StudentRepository.get_by_id(cur, g["student_id"])
            if not student:
                continue

            classroom = ClassroomRepository.get_by_id(cur, student["classroom_id"]) if student.get("classroom_id") else None
            school = SchoolRepository.get_by_id(cur, classroom["school_id"]) if classroom and classroom.get("school_id") else None
            area = AreaRepository.get_by_id(cur, school["area_id"]) if school and school.get("area_id") else None

            if is_subject_failed(score):
                failed_count += 1

            if classroom:
                class_scores.setdefault(classroom["id"], []).append(score)
            if school:
                school_scores.setdefault(school["id"], []).append(score)
            if area:
                area_scores.setdefault(area["id"], []).append(score)

        best_class = None
        if class_scores:
            best_class_id, scores = max(class_scores.items(), key=lambda x: (calculate_average(x[1]) or -1))
            class_info = ClassroomRepository.get_by_id(cur, best_class_id)
            best_class = {
                "class_id": class_info["id"],
                "class_name": class_info["name"],
                "avg": calculate_average(scores),
            }

        best_school = None
        if school_scores:
            best_school_id, scores = max(school_scores.items(), key=lambda x: (calculate_average(x[1]) or -1))
            school_info = SchoolRepository.get_by_id(cur, best_school_id)
            best_school = {
                "school_id": school_info["id"],
                "school_name": school_info["name"],
                "avg": calculate_average(scores),
            }

        best_area = None
        if area_scores:
            best_area_id, scores = max(area_scores.items(), key=lambda x: (calculate_average(x[1]) or -1))
            area_info = AreaRepository.get_by_id(cur, best_area_id)
            best_area = {
                "area_id": area_info["id"],
                "area_name": area_info["name"],
                "avg": calculate_average(scores),
            }

    print(f"Subject: {subject['id']} - {subject['name']}")
    print(f"Failed students count: {failed_count}")

    if best_class:
        print(f"Best class in {subject['name']}: {best_class['class_name']} with avg {best_class['avg']}")
    if best_school:
        print(f"Best school in {subject['name']}: {best_school['school_name']} with avg {best_school['avg']}")
    if best_area:
        print(f"Best area in {subject['name']}: {best_area['area_name']} with avg {best_area['avg']}")
