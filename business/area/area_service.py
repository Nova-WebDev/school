from data_access.transaction import Transaction
from data_access.repository import AreaRepository


class AreaService:
    @staticmethod
    def create_area(name: str) -> int:
        with Transaction() as cur:
            return AreaRepository.insert(cur, name)

    @staticmethod
    def update_area(area_id: int, name: str) -> None:
        with Transaction() as cur:
            AreaRepository.update(cur, area_id, name)

    @staticmethod
    def delete_area(area_id: int) -> None:
        with Transaction() as cur:
            AreaRepository.delete(cur, area_id)

    @staticmethod
    def get_area(area_id: int) -> dict | None:
        with Transaction() as cur:
            return AreaRepository.get_by_id(cur, area_id)

    @staticmethod
    def list_areas() -> list[dict]:
        with Transaction() as cur:
            return AreaRepository.get_all(cur)
