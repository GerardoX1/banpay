from pydantic import BaseModel

from banpay.models.v1.users import RoleTypes
from banpay.models.base_models.


class UserPost(BaseModel):
    roles: list[RoleTypes]
    display_name: str
    phone_number: str

class QueryInput(QueryableModel):
    tenant_id: Optional[str] = Field(
        filter=True, alias="tenant_id", condition="=="
    )
    search: Optional[str]
    created_at_gt: int = Field(
        default=get_today_millis_with_timedelta(),
        filter=True,
        alias="created_at",
        condition=">=",
    )
    created_at_lt: int = Field(
        default=get_today_millis_with_timedelta(1),
        filter=True,
        alias="created_at",
        condition="<=",
    )
    created_by: Optional[str] = Field(
        filter=True, alias="created_by.id", condition="=="
    )
    pod_id: Optional[str] = Field(filter=True, alias="pod_id", condition="==")
