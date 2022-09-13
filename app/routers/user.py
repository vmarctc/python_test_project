from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from app.db.database import get_session
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import NoResultFound

import app.models as models
import app.schemas as schemas

router = APIRouter()


@router.get("/users", response_model=List[schemas.UserSchema],
            status_code=status.HTTP_200_OK, tags=["User"])
def users(session: Session = Depends(get_session)):
    return session.query(models.User).options(
        joinedload(models.User.games)
    ).all()


@router.get("/user/{user_id}", response_model=schemas.UserSchema,
            status_code=status.HTTP_200_OK, tags=["User"])
def get_user(user_id: int, session: Session = Depends(get_session)):
    try:
        user = session.query(models.User).options(joinedload(
            models.User.games)).where(models.User.id == user_id).one()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} doesn't exist.")

    return user


@router.put("/user/{user_id}/game/{game_id}",
            response_model=schemas.UserSchema,
            status_code=status.HTTP_200_OK, tags=["User"])
def connect_to_game(user_id: int, game_id: int,
                    session: Session = Depends(get_session)):
    try:
        user = session.query(models.User).options(joinedload(
            models.User.games)).where(models.User.id == user_id).one()

        game = session.query(models.Game).options(joinedload(
            models.Game.users)).where(models.Game.id == game_id).one()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} or "
            f"game with id {game_id} doesn't exist.")

    if game in user.games:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User already playing in {game}")
    else:
        user.games.append(game)

    session.commit()

    return user
