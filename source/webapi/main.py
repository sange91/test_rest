import uvicorn
from webapi.app import app
from webapi.lib.routes.workspace_file import router as wsf_router
from webapi.lib.routes.transactions import router as transaction_router

app.include_router(wsf_router)
app.include_router(transaction_router)


if __name__ == '__main__':
    uvicorn.run(app)