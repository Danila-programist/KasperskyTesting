import uvicorn
from fastapi import FastAPI

app = FastAPI(title="API for Upload Files")

if __name__ == "__main__":
    uvicorn.run(app, host="main:app", port=8000, reload=True)
