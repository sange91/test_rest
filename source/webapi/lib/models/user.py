from webapi.lib import models


class User(models.BaseEntityModel):
    id: int
    code: str

