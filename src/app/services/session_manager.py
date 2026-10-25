from google.adk.sessions import DatabaseSessionService

from app.db.database import engine

session_service = DatabaseSessionService(db_engine=engine)