from app.db.client import clients
from app.models.client import Client, ClientAdd, ClientUpdate, ClientDelete
from app.repositories.base_repository import BaseRepository


class ClientRepository(BaseRepository):
    async def get_by_id(self, client_id: int) -> Client:
        query = clients.select().where(clients.c.id == client_id)
        client = await self.database.fetch_one(query=query)
        return Client.parse_obj(client)

    async def get_clients_where_pattern(self, pattern: str) -> list[Client]:
        query = clients.select().where(
            clients.c.mobile_operator_code == pattern or clients.c.tag == pattern
        )
        list_client = await self.database.fetch_all(query=query)
        return [Client.parse_obj(client) for client in list_client]

    async def create(self, client: ClientAdd) -> int:
        query = clients.insert().values(
            mobile_number=client.mobile_number,
            mobile_operator_code=client.mobile_operator_code,
            tag=client.tag,
            utc=client.utc,
        )
        return await self.database.execute(query=query)

    async def update(self, client: ClientUpdate) -> None:
        query = (
            clients.update()
            .where(clients.c.id == client.id)
            .values(
                mobile_number=client.mobile_number,
                mobile_operator_code=client.mobile_operator_code,
                tag=client.tag,
                utc=client.utc,
            )
        )
        await self.database.execute(query=query)

    async def delete(self, client: ClientDelete) -> None:
        query = clients.delete().where(clients.c.id == client.id)
        return await self.database.execute(query=query)
