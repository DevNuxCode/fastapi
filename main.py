from fastapi import FastAPI
from routes.user import router as user_router



from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/api")

