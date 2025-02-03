from infra.mongo import MongoRepository

from banpay.services.v1.users import UserService


class Flow:
    def __init__(self, repository: MongoRepository):
        self._repository = repository
        self._service = UserService(repository)
