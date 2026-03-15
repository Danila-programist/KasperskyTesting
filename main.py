import uvicorn
from fastapi import FastAPI

from app.api.export import router_file

app = FastAPI(title="API for Upload Files")

app.include_router(router_file)

if __name__ == "__main__":
    uvicorn.run(app, host="main:app", port=8000, reload=True)
