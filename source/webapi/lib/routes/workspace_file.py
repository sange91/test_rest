import json
from typing import List
from fastapi import APIRouter
from fastapi import Depends, Query
from fastapi import status, HTTPException
from webapi.lib.models.workspace_file import WorkspaceFile
from webapi.lib.routes import get_root_route
from webapi.db_client import get_db_client


wsf_route = '{}/workspace_file'.format(get_root_route())
router = APIRouter(prefix=wsf_route)


async def get_filters(query_filters: list[str] = Query(...)):
    filters = list()

    print(">>>> filters", filters)
    return list(map(json.loads, filters))


# @router.get('', response_model=WorkspaceFile, status_code=status.HTTP_200_OK)
# async def get_workspace_file(filters: list[str] | None = Query(None), operator=None,
#                              db_client: str = Depends(get_db_client)):
#     workspace = None
#     print("?????? filter", filters, operator)
#     if not workspace:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Workspace not found.')
#
#     result = db_client.find()
#     return result


@router.get('', response_model=WorkspaceFile, status_code=status.HTTP_200_OK)
async def get_workspace_file(filters: List = Depends(get_filters), operator=None,
                             db_client: str = Depends(get_db_client)):
    workspace = None
    print("?????? filter", filters, operator)
    if not workspace:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Workspace not found.')

    result = db_client.find()
    return result


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_workspace_file(wsf: WorkspaceFile):
    return {'data': 'created workspace file with {}'.format(wsf)}


@router.post('/clone', status_code=status.HTTP_201_CREATED)
async def clone_workspace_file(wsf: WorkspaceFile):
    return {'data': 'created workspace file with {}'.format(wsf)}


@router.post('/upshift', status_code=status.HTTP_201_CREATED)
async def upshift_workspace_file(wsf: WorkspaceFile):
    return {'data': 'created workspace file with {}'.format(wsf)}
