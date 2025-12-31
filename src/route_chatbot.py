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
    """
    Initialize a chat session with the chatbot.

    Args:
        user_id (str): The ID of the user.

    Returns:
        Response: A response containing stream_token, channel_id, and getstream_api_key.
    """
    user_id = None
    
    # Extract user_id based on method
    if request.method == "POST":
        try:
            data = await request.json()
            user_id = data.get("user_id")
        except:
            pass
    else:
        user_id = request.query_params.get("user_id")

    # In a real chatbot, you'd use user_id here. 
    # For now, we're just forwarding to /dev/ip which ONLY supports GET.
    
    headers = {
        "apikey": API_KEY
    }
    
    # We force "GET" here because the target /dev/ip doesn't allow POST
    response = await client.request(
        # method="POST",
        method="GET",
        url=f"/dev/api/identity-service/v1/token/{user_id}",
        headers=headers,
        params=request.query_params
    )
    
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )
