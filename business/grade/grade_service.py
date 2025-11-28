from data_access.transaction import Transaction
from data_access.repository import GradeRepository
from business.logic import is_valid_score


class GradeService:
    @staticmethod
    def create_grade(student_id: int, subject_id: int, score: float) -> int:
        if not is_valid_score(score):
            raise ValueError("Invalid score: must be between 0 and 20")
        with Transaction() as cur:
            return GradeRepository.insert(cur, student_id, subject_id, score)

    @staticmethod
    def update_grade(grade_id: int, score: float) -> None:
        if not is_valid_score(score):
            raise ValueError("Invalid score: must be between 0 and 20")
        with Transaction() as cur:
            GradeRepository.update(cur, grade_id, score)

    @staticmethod
    def delete_grade(grade_id: int) -> None:
        with Transaction() as cur:
            GradeRepository.delete(cur, grade_id)

    @staticmethod
    def get_grade(grade_id: int) -> dict | None:
        with Transaction() as cur:
            return GradeRepository.get_by_id(cur, grade_id)

    @staticmethod
    def list_grades() -> list[dict]:
        with Transaction() as cur:
            return GradeRepository.get_all(cur)

    @staticmethod
    def list_grades_by_student(student_id: int) -> list[dict]:
        with Transaction() as cur:
            return GradeRepository.filter_by_student(cur, student_id)

    @staticmethod
    def list_grades_by_subject(subject_id: int) -> list[dict]:
        with Transaction() as cur:
            return GradeRepository.filter_by_subject(cur, subject_id)
