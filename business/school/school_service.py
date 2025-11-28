from data_access.transaction import Transaction
from data_access.repository import SchoolRepository


class SchoolService:
    @staticmethod
    def create_school(name: str, area_id: int | None = None) -> int:
        with Transaction() as cur:
            return SchoolRepository.insert(cur, name, area_id)

    @staticmethod
    def update_school(school_id: int, name: str, area_id: int | None = None) -> None:
        with Transaction() as cur:
            SchoolRepository.update(cur, school_id, name, area_id)

    @staticmethod
    def delete_school(school_id: int) -> None:
        with Transaction() as cur:
            SchoolRepository.delete(cur, school_id)

    @staticmethod
    def get_school(school_id: int) -> dict | None:
        with Transaction() as cur:
            return SchoolRepository.get_by_id(cur, school_id)

    @staticmethod
    def list_schools() -> list[dict]:
        with Transaction() as cur:
            return SchoolRepository.get_all(cur)

    @staticmethod
    def list_schools_by_area(area_id: int) -> list[dict]:
        with Transaction() as cur:
            return SchoolRepository.filter_by_area(cur, area_id)
