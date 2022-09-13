from database import engine, Base

print("Creating database ....")

Base.metadata.create_all(engine)
