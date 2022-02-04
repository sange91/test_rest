from webapi.lib import models
from webapi.lib.models.user import User
from webapi.lib.models.location import Location


class Transaction(models.BaseEntityModel):
    type: str
    comment: str
    timestamp: str
    machine: str
    location: Location
    user: User
    # wsf: WorkspaceFile
