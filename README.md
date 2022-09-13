# python_test_project
Python test project for SoftVision

Part 1. Created FastAPI base project:
- Created User model (id, name, age, email)
- Created Game model (id, name)
Created Endpoints:
- /games (getting list of all games and users who connected to this games)
- /users (getting list of all users and info about games for each user)
- /user/{user_id} (getting info about current user and info about all connected games)
- /user/{user_id}/game/{game_id} (Connect user go game)

Part 2 (Advanced).
- Used SQLAlchemy for store my models

It's easy to test using the FastAPI Swagger UI.
