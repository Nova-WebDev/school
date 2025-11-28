from data_access.transaction import Transaction
from data_access.repository import SubjectRepository


class SubjectService:
    @staticmethod
    def create_subject(name: str) -> int:
        with Transaction() as cur:
            return SubjectRepository.insert(cur, name)

    @staticmethod
    def update_subject(subject_id: int, name: str) -> None:
        with Transaction() as cur:
            SubjectRepository.update(cur, subject_id, name)

    @staticmethod
    def delete_subject(subject_id: int) -> None:
        with Transaction() as cur:
            SubjectRepository.delete(cur, subject_id)

    @staticmethod
    def get_subject(subject_id: int) -> dict | None:
        with Transaction() as cur:
            return SubjectRepository.get_by_id(cur, subject_id)

    @staticmethod
    def list_subjects() -> list[dict]:
        with Transaction() as cur:
            return SubjectRepository.get_all(cur)
