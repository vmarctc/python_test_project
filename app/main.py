from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import game, user

description = """
Gaming platform API helps you do awesome stuff. 🚀
## Game
You will be able to:
* **Get games (get list of all games and users who connected to this games)**.
## User
You will be able to:
* **Get specific user (get info about specific user
 and info about all connected games)**
* **Get users (get list of all users and info about
 all connected games for each user)**
* **Connect to game. When user send this request.
 Need to create one obj like User - Game.**

"""

tags_metadata = [
    {
        "name": "Game",
        "description": "Operations with Game"
    },
    {
        "name": "User",
        "description": "Operations with User"
    },
    {
        "name": "Redirect",
        "description": "Redirect to docs page"
    }
]

app = FastAPI(title='Gaming Platform', description=description,
              openapi_tags=tags_metadata)

app.include_router(game.router)
app.include_router(user.router)


@app.get("/", tags=["Redirect"])
def redirect():
    return RedirectResponse("/docs")
