from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from ..models import reviews as model


def create(db: Session, request):
    new_item = model.Review(
        customer_id=request.customer_id,
        sandwich_id=request.sandwich_id,
        review_text=request.review_text,
        rating=request.rating
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    return db.query(model.Review).all()


def read_one(db: Session, item_id):
    item = db.query(model.Review).filter(model.Review.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Id not found!")

    return item


def update(db: Session, item_id, request):
    item = db.query(model.Review).filter(model.Review.id == item_id)

    if not item.first():
        raise HTTPException(status_code=404, detail="Id not found!")

    item.update(request.dict(exclude_unset=True), synchronize_session=False)

    db.commit()

    return item.first()


def delete(db: Session, item_id):
    item = db.query(model.Review).filter(model.Review.id == item_id)

    if not item.first():
        raise HTTPException(status_code=404, detail="Id not found!")

    item.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)