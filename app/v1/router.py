from fastapi import APIRouter, FastAPI

from .resources import users

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(users.router)

app = FastAPI()
app.include_router(api_router)
