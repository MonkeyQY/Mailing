from app.db.message import messages
from app.models.message import Message
from app.repositories.base_repository import BaseRepository


class MessageRepository(BaseRepository):
    async def get_all_messages_for_mailing(self, mailing_id: int) -> list[Message]:
        query = messages.select().where(messages.c.mailing_id == mailing_id)
        list_messages = await self.database.fetch_all(query=query)
        return [Message.parse_obj(message) for message in list_messages]

    async def create(self, client_id, mailing_id, status_sending: bool = False) -> Message:
        query = messages.insert().values(
            client_id=client_id,
            mailing_id=mailing_id,
            status_sending=status_sending
        )
        return await self.database.execute(query=query)
