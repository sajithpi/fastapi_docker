from . model import engine,Base
print("Database created")
Base.metadata.create_all(engine)