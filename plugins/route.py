from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({
        "server_status": "running",
        "bot": "@Spk_File_Store_Bot",
        "made_by": "@spk_links"
    })
