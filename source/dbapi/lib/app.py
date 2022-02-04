import asyncio
import motor.motor_asyncio
from beanie import init_beanie
from dbapi.lib.models import workspace_file


async def initialize_beanie(db_name):
    if not client:
        client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

    await init_beanie(database=client[db_name], document_models=workspace_file.models)


async def main():
    await initialize_beanie('test_db')

    # files = workspace_file.WorkspaceFile.find(
    #     workspace_file.WorkspaceFile.owner == 'sange.lama')

    # wsf = workspace_file.WorkspaceFile(name='test_db1', owner='sange.lama')
    # await wsf.insert()
    #
    # await switch_db('test_db2')
    # wsf = workspace_file.WorkspaceFile(name='test_db2', owner='sange.lama')
    #
    # await wsf.insert()
    files = workspace_file.WorkspaceFile.find(workspace_file.WorkspaceFile.owner == 'sange.lama')

    print(await files.to_list())

if __name__ == '__main__':
    asyncio.run(main())
