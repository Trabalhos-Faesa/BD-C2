from enum import Enum
from typing import (
    Any,
    Mapping,
    Optional,
    TypedDict,
)

from pydantic import BaseModel


class SQLResultStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class SQLResultDictBase(TypedDict):
    """Campos obrigatórios"""
    rows: list[Mapping[str, Any]]
    # https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.CursorResult.rowcount
    rowcount: int


class SQLResultDict(SQLResultDictBase, total=False):
    """Campos opcionais (`total=False`)"""
    status: Optional[SQLResultStatus]
    msg: Optional[str]


class SQLResult(BaseModel):
    # __annotations__ = typing.get_type_hints(SQLResultDict)
    rowcount: int
    rows: list[dict]
    status: Optional[SQLResultStatus] = None
    msg: Optional[str] = None
