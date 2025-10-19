from aiohttp import web
import re
from bot import Bot
from config import CHANNEL_ID

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({
        "server_status": "running", 
        "bot": "SPK FileStore Bot",
        "made_by": "@spk_links"
    })

@routes.get(r"/watch/{id:\d+}", allow_head=True)
async def stream_handler(request):
    try:
        message_id = int(request.match_info['id'])
        return web.Response(text=f"Stream page for message {message_id}")
    except Exception as e:
        return web.Response(text=f"Error: {str(e)}")

@routes.get(r"/{id:\d+}", allow_head=True)
async def media_handler(request):
    try:
        message_id = int(request.match_info['id'])
        return web.Response(text=f"Media download for {message_id}")
    except Exception as e:
        return web.Response(text=f"Error: {str(e)}")
