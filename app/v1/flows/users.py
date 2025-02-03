from app.v1.flows._base_flow import Flow
from app.v1.schemas.users import UserPost
from banpay.models.v1.users import UserModel


class UserFlow(Flow):
    def create(self, data: UserPost) -> dict:
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def get_all(self, data: UserPost) -> dict:
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def gey_by_id(self, data: UserPost) -> dict:
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def patch(self, data: UserPost) -> dict:
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def delete(self, data: UserPost) -> dict:
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}
