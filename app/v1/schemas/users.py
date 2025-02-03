from pydantic import BaseModel

from banpay.models.v1.users import RoleTypes


class UserPost(BaseModel):
    roles: list[RoleTypes]
    display_name: str
    phone_number: str


class UserPatch(BaseModel):
    roles: list[RoleTypes]
    display_name: str
    phone_number: str
