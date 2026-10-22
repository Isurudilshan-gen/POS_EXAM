from starlette.exceptions import HTTPException

from repositories import category_repository


def create_product(db, product_data):
    category = category_repository.get_category_by_id(db, product_data.category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    if not category.active:
        raise HTTPException(status_code=400, detail="cant create a product under inactive category")

