from webapi.lib import models


class Lock(models.BaseEntityModel):
    machine: str
    status: bool
