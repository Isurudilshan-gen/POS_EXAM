from starlette.exceptions import HTTPException

from repositories import category_repository


def get_category(db, category_id: int):
    category = category_repository.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category