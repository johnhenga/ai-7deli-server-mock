from fastapi import FastAPI
import os
# from route_proxy import router as proxy_router
from route_chatbot import router as chatbot_router

app = FastAPI()
app.include_router(chatbot_router)
# app.include_router(proxy_router)


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        dict: A simple status response indicating the server is running.
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
