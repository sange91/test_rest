from typing import Optional
from webapi.lib import models
from webapi.lib.models.project import Project


class Location(models.BaseEntityModel):
    code: str
    region: str
    timezone: str
    projects: Optional[Project]