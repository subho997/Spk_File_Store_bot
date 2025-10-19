from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"status": "running", "message": "Bot is alive!"})

@routes.get("/health")
async def health_check_handler(request):
    return web.json_response({"status": "healthy"})

# Add more routes as needed for your application
