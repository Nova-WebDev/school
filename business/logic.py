def calculate_average(grades: list[float]) -> float | None:
    return sum(grades) / len(grades) if grades else None


def is_student_grade_a(grades: list[float]) -> bool:
    avg = calculate_average(grades)
    return avg is not None and avg >= 18


def is_valid_score(score: float) -> bool:
    return 0 <= score <= 20


def is_student_failed_by_average(grades: list[float]) -> bool:
    avg = calculate_average(grades)
    return avg is None or avg < 12


def is_subject_failed(score: float) -> bool:
    return score < 10
