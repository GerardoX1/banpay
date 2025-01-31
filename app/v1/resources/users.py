from fastapi import APIRouter, Depends, Request, Response
from infra.mongo import MongoRepository
from presentation.status import Status

from app.libs import mongo_handler
from app.v1.exceptions.handler import exception_handler
from app.v1.flows.users import UserFlow
from app.v1.schemas.users import Message

router = APIRouter()


# ? [POST] <— /v1/endpoint
@router.post("/endpoint")
@exception_handler(response_status=Status.OK)
async def post_endpoint(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(mongo_handler.get_repository),
) -> dict:
    flow = UserFlow(repository=repository)
    parsed_model = Message.model_validate(await request.json())
    return {**parsed_model}
