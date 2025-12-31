from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()
client = httpx.AsyncClient(base_url="https://vm3k82gg09.execute-api.ap-southeast-1.amazonaws.com")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    # Forward the request to the target gateway
    url = f"/{path}"
    headers = dict(request.headers)
    # Remove 'host' header to let httpx set the correct one for the target
    headers.pop("host", None)
    
    content = await request.body()
    
    response = await client.request(
        method=request.method,
        url=url,
        headers=headers,
        params=request.query_params,
        content=content
    )
    
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
