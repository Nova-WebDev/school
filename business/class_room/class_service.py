from data_access.transaction import Transaction
from data_access.repository import ClassroomRepository


class ClassroomService:
    @staticmethod
    def create_classroom(name: str, school_id: int | None = None) -> int:
        with Transaction() as cur:
            return ClassroomRepository.insert(cur, name, school_id)

    @staticmethod
    def update_classroom(classroom_id: int, name: str, school_id: int | None = None) -> None:
        with Transaction() as cur:
            ClassroomRepository.update(cur, classroom_id, name, school_id)

    @staticmethod
    def delete_classroom(classroom_id: int) -> None:
        with Transaction() as cur:
            ClassroomRepository.delete(cur, classroom_id)

    @staticmethod
    def get_classroom(classroom_id: int) -> dict | None:
        with Transaction() as cur:
            return ClassroomRepository.get_by_id(cur, classroom_id)

    @staticmethod
    def list_classrooms() -> list[dict]:
        with Transaction() as cur:
            return ClassroomRepository.get_all(cur)

    @staticmethod
    def list_classrooms_by_school(school_id: int) -> list[dict]:
        with Transaction() as cur:
            return ClassroomRepository.filter_by_school(cur, school_id)
