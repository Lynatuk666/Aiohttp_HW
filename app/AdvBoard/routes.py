"""
Module for creating and setting up routes.
"""

from aiohttp import web
from app.AdvBoard.views import AdvView, UserView, AdvRedactView


def setup_routes(app: web.Application):
    """Function for setting up routes."""
    app.router.add_get('/api/user/{user_id:[0-9]+}', UserView)
    app.router.add_post('/api/user/', UserView)
    app.router.add_patch('/api/user/{user_id:[0-9]+}', UserView)
    app.router.add_delete('/api/user/{user_id:[0-9]+}', UserView)
# ############################################################
    app.router.add_get('/api/adv/', AdvView)
    app.router.add_get('/api/adv/{adv_id:[0-9]+}', AdvRedactView)
# ####################################################################
    app.router.add_post('/api/user/{user_id:[0-9]+}/adv', AdvRedactView)
    app.router.add_delete('/api/user/{user_id:[0-9]+}/adv/{adv_id:[0-9]+}', AdvRedactView)
    app.router.add_patch('/api/user/{user_id:[0-9]+}/adv/{adv_id:[0-9]+}', AdvRedactView)
