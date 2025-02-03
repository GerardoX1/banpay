from typing import Optional

from presentation.error import ErrorLocationEnum
from pydantic import Field

from banpay.models.base_models.queryable_model import QueryableModel


class QueryInput(QueryableModel):
    __location__ = ErrorLocationEnum.QUERY

    roles: Optional[str] = Field(
        alias="roles",
        default=None,
        json_schema_extra={"filter": True, "condition": "=="},
    )
    created_gt: Optional[int] = Field(
        alias="created_at",
        default=None,
        json_schema_extra={"filter": True, "condition": ">="},
    )
    created_lt: Optional[int] = Field(
        alias="created_at",
        default=None,
        json_schema_extra={"filter": True, "condition": "<="},
    )
