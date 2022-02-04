import asyncio
import pymongo
from beanie import Document
from beanie import Indexed
from typing import Optional


class BaseDocument(Document):
    # _type =
    retired: bool = True
    tags: list


class Location(BaseDocument):
    code: str
    region: str
    timezone: str

    class Collection:
        name = 'location'


class Lock(BaseDocument):
    user: Optional[str]
    machine: Optional[str]
    location: Optional[Location]


class Transaction(BaseDocument):
    type: str
    comment: str
    timestamp: str
    machine: str
    location: Location
    user: dict
    # wsf: WorkspaceFile


class WorkspaceFile(BaseDocument):
    name: str
    context: dict
    project: dict
    location: Location
    lock: Lock
    owner: Indexed(str)
    step: dict
    task: dict
    transactions: list
    workspace: dict

    class Collection:
        name = 'workspace_file'


models = BaseDocument.__subclasses__()

