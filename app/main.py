"""
This is the main entry point for the application.
"""

from aiohttp import web
from app.AdvBoard.routes import setup_routes
from app.AdvBoard.views import session_middleware
from app.AdvBoard.db_funcs import init_db, close_db


app = web.Application()


def setup_app(application):
    """Set up some middlewares."""
    setup_routes(application)
    # setup_DB(application)


async def db_context(app: web.Application):
    """Open database connection and close it after requests."""
    await  init_db()
    yield
    await close_db()



app.cleanup_ctx.append(db_context)
app.middlewares.append(session_middleware)


if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, port=8080)
