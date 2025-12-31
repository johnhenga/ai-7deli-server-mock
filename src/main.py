from fastapi import FastAPI
import os
from route_proxy import router as proxy_router

app = FastAPI()
app.include_router(proxy_router)

API_KEY = os.getenv("API_KEY")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
