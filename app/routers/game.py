from typing import List
from fastapi import APIRouter, status, Depends
from app.db.database import get_session
from sqlalchemy.orm import Session, joinedload

import app.models as models
import app.schemas as schemas

router = APIRouter()


@router.get("/games", response_model=List[schemas.GameSchema],
            status_code=status.HTTP_200_OK, tags=["Game"])
def games(session: Session = Depends(get_session)):
    return session.query(models.Game).options(
        joinedload(models.Game.users)
    ).all()
