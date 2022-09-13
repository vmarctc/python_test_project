from sqlalchemy.orm import Session, joinedload
from schemas import UserSchema
from models import Game, User
from db.database import engine

with Session(bind=engine) as session:
    pass
    # user1 = User(name="vitalik", age=26, email="vitalik@com.ua")
    # user2 = User(name="jack", age=18, email="jack@com.ua")
    # user3 = User(name="John Wick", age=36, email="wick@com.ua")

    # game1 = Game(name="dota")
    # game2 = Game(name="csgo")
    # game3 = Game(name="valorant")
    # game4 = Game(name="pubg")

    # user1.games = [game1, game2]
    # user2.games = [game3, game4]

    # session.add_all([user1, user2, user3, game1, game2, game3, game4])
    # session.commit()
