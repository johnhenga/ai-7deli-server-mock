from fastapi import APIRouter, Request, Response
import httpx
import os

router = APIRouter()
API_KEY = os.getenv("API_KEY")

client = httpx.AsyncClient(base_url="https://vm3k82gg09.execute-api.ap-southeast-1.amazonaws.com")

@router.api_route(
    "/chatbot", 
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def chatbot(
    request: Request,
):
    headers = {
        "apikey": API_KEY
    }
    # Forward the request to the target gateway
    url = f"/dev/ip"
    response = await client.request(
        method=request.method,
        url=url,
        headers=headers,
        params=request.query_params,
        content=await request.body()
    )
    
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )
