from app.db.database import Base
from sqlalchemy import String, Integer, Column, ForeignKey, Table
from sqlalchemy.orm import relationship

user_game = Table('user_game', Base.metadata,
                  Column('user_id', ForeignKey(
                         'users.id'), primary_key=True),
                  Column('game_id', ForeignKey(
                         'games.id'), primary_key=True)
                  )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    games = relationship("Game", secondary="user_game", back_populates="users")

    def __str__(self) -> str:
        return f"{self.name}"


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    users = relationship("User", secondary="user_game", back_populates="games")

    def __str__(self) -> str:
        return f"{self.name}"
