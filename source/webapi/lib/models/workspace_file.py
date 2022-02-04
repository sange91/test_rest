from webapi.lib import models
from webapi.lib.models.user import User
from webapi.lib.models.lock import Lock
from webapi.lib.models.location import Location
from webapi.lib.models.project import Project


class WorkspaceFile(models.BaseEntityModel):
    name: str
    context: dict
    project: Project
    app: str
    location: Location
    lock: Lock
    owner: User
    step: dict
    task: dict
    transactions: list
    workspace: dict
