from pydantic import BaseModel
from typing import Optional


class BaseEntityModel(BaseModel):
    # _type =
    retired: Optional[bool] = False
    tags: Optional[list]

