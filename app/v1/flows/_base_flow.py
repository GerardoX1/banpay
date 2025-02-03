from infra.mongo import MongoRepository

from banpay.services.v1.users import UserModel, UserService


class Flow:
    def __init__(self, repository: MongoRepository):
        self._repository = repository
        self._service = UserService(repository)

    def _get(self, user_id: str) -> UserModel:
        user = self._service.get(user_id)
        if not user:
            raise UserNotFound(user_id)
        return user
