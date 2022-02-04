import motor.motor_asyncio
from beanie import init_beanie
from fastapi import FastAPI
from dbapi.lib.models import workspace_file

app = FastAPI()


@app.on_event('startup')
async def initialize_beanie(db_name='test_db'):
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    await init_beanie(database=client[db_name], document_models=workspace_file.models)
