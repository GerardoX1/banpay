from math import ceil

from app.v1.flows._base_flow import Flow
from app.v1.schemas.query_params import QueryInput
from app.v1.schemas.users import UserPatch, UserPost
from banpay.models.v1.users import UserModel


class UserFlow(Flow):
    def create(self, data: UserPost) -> dict:
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def paginated_query(self, query_params: QueryInput) -> dict:
        # revisar que se haga bien el paginado
        count, users = self._service.paginated_query(
            page=query_params.page,
            limit=query_params.limit,
            and_conditions=query_params.filters(),
            sort=query_params.sort,
        )
        response = {"users": users}
        if users:
            response.update(
                {
                    "page_limit": query_params.limit,
                    "total_pages": ceil(count / query_params.limit),
                    "items_count": count,
                }
            )
        return response

    def gey_by_id(self, data: UserPost) -> dict:
        # falta el get by id
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def patch(self, user_id: str, body: UserPatch) -> dict:
        user = self._get(user_id)
        user_updated = user.updated_copy(
            {
                **body.model_dump(by_alias=True, exclude_unset=True),
            }
        )
        user: UserModel = self._service.update(user_updated.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}

    def delete(self, data: UserPost) -> dict:
        # falta el delete
        user_data = UserModel(**data.model_dump())
        user: UserModel = self._service.create(user_data.model_dump(by_alias=True))
        return {"user": user.model_dump(by_alias=True)}
