from app.db.client import clients
from app.models.client import Client, ClientAdd, ClientUpdate, ClientDelete, ClientAddResponse
from app.repositories.base_repository import BaseRepository


class ClientRepository(BaseRepository):

    async def get_by_id(self, client_id: int) -> Client:
        query = clients.select().where(clients.c.id == client_id)
        client = await self.database.fetch_one(query=query)
        return Client.parse_obj(client)

    async def get_client_where_mobile_code(self, mobile_code: str) -> Client:
        query = clients.select().where(clients.c.mobile_operator_code == mobile_code)
        client = await self.database.fetch_one(query=query)
        return Client.parse_obj(client)

    async def get_client_where_tag(self, tag: str) -> Client:
        query = clients.select().where(clients.c.tag == tag)
        client = await self.database.fetch_one(query=query)
        return Client.parse_obj(client)

    async def create(self, client: ClientAdd):
        query = clients.insert().values(client.mobile_number,
                                        client.mobile_operator_code,
                                        client.tag,
                                        client.utc)
        return await self.database.execute(query=query)

    async def update(self, client: ClientUpdate):
        query = clients.update().where(clients.c.id == client.id).values(
            client.mobile_number,
            client.mobile_operator_code,
            client.tag,
            client.utc)
        return await self.database.execute(query=query)

    async def delete(self, client: ClientDelete):
        query = clients.delete().where(clients.c.id == client.id)
        return await self.database.execute(query=query)
