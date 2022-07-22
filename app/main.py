from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import models
from app.database import engine
from routers import post, user, auth, vote

#from .config import settings


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


origins = ["*"]
"""
while True:
    try:
         conn = psycopg2.connect(host='localhost', database='myapp', user='postgres',
                                 password='mick', cursor_factory=RealDictCursor)

         cursor = conn.cursor()
         print("Database connection was succesfull!")
         break
    except Exception as error:
         print("Connecting to database failed")
         print("Error: ", error)
         time.sleep(3)

"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)





