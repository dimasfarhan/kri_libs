from uuid import UUID

from .connection import database
from .exceptions import UserNotFoundError


def get_user(query: dict) -> dict:
    user = database.user.find_one(query)  # type: dict
    if not user:
        raise UserNotFoundError(f"Cannot find user with: {query}")
    return user


def get_user_by_uuid(uuid: UUID) -> dict:
    return get_user(
        query={'user_uuid': uuid}
    )