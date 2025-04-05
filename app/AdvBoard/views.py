"""
This module with views, which will be used in routes.
"""

import app.AdvBoard.db_funcs as db
from aiohttp import web
from app.AdvBoard.models import Advertisement, User


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with db.Session() as session:
        request.session = session
        response = await handler(request)
    return response


class AdvView(web.View):
    """Class to return all advertisements from database."""
    async def get(self):
        adv_list = await db.get_adv_list(self.request.session)
        return web.json_response([adv.dict for adv in adv_list])


class UserView(web.View):
    """Class for work with users."""
    async def get(self):
        user = self.request.match_info["user_id"]
        return web.json_response(await db.get_user_by_id(int(user), self.request.session))

    async def post(self):
        json_data = await self.request.json()
        user = User(**json_data)
        await db.create_user(user, self.request.session)
        return web.json_response(user.dict)

    async def patch(self):
        json_data = await self.request.json()
        user_id = int(self.request.match_info["user_id"])
        user = await db.update_user(user_id, json_data, self.request.session)
        return web.json_response(user.dict)

    async def delete(self):
        user_id = self.request.match_info["user_id"]
        try:
            await db.delete_user(int(user_id), self.request.session)
        except Exception as e:
            return web.json_response({"Result":"User not found"},status=404)
        return web.json_response({"Result":"User deleted"}, status=204)


class AdvRedactView(web.View):
    """Class for work with advertisements."""
    @property
    def adv_id(self):
        return int(self.request.match_info["adv_id"])

    async def get(self):
        adv = await db.get_adv_by_id(self.adv_id, self.request.session)
        return web.json_response(adv.dict)

    async def post(self):
        json_data = await self.request.json()
        owner_id = int(self.request.match_info["user_id"])
        adv = Advertisement(**json_data, user_id=owner_id)
        await db.create_adv(adv, self.request.session)
        return web.json_response(adv.dict)

    async def patch(self):
        json_data = await self.request.json()
        upd_adv = await db.update_adv(self.adv_id, json_data, self.request.session)
        print("вроде должно")
        return web.json_response(upd_adv.dict)

    async def delete(self):
        adv_id = self.request.match_info["adv_id"]
        try:
            await db.delete_adv(int(adv_id), self.request.session)
        except Exception as e:
            return web.json_response({"Result":"Advertisement not found"},status=404)
        return web.json_response({"Result":"Advertisement deleted"}, status=204)