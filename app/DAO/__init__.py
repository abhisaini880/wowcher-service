from databases.mysql import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        print("yield connection")
        yield db
    finally:
        print("close connection")
        db.close()
