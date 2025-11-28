from data_access.transaction import Transaction
from data_access.repository import StudentRepository


class StudentService:
    @staticmethod
    def create_student(name: str, classroom_id: int | None = None) -> int:
        with Transaction() as cur:
            return StudentRepository.insert(cur, name, classroom_id)

    @staticmethod
    def update_student(student_id: int, name: str, classroom_id: int | None = None) -> None:
        with Transaction() as cur:
            StudentRepository.update(cur, student_id, name, classroom_id)

    @staticmethod
    def delete_student(student_id: int) -> None:
        with Transaction() as cur:
            StudentRepository.delete(cur, student_id)

    @staticmethod
    def get_student(student_id: int) -> dict | None:
        with Transaction() as cur:
            return StudentRepository.get_by_id(cur, student_id)

    @staticmethod
    def list_students() -> list[dict]:
        with Transaction() as cur:
            return StudentRepository.get_all(cur)

    @staticmethod
    def list_students_by_classroom(classroom_id: int) -> list[dict]:
        with Transaction() as cur:
            return StudentRepository.filter_by_classroom(cur, classroom_id)
