import datetime

from app.db.mailing import mailings
from app.models.mailing import MailingDelete, MailingUpdate, MailingAdd, Mailing
from app.repositories.base_repository import BaseRepository


class MailingRepository(BaseRepository):

    async def get_by_id(self, mailing_id: int) -> Mailing:
        query = mailings.select().where(mailings.c.id == mailing_id)
        mailing = await self.database.fetch_one(query=query)
        return Mailing.parse_obj(mailing)

    async def create(self, mailing: MailingAdd):
        query = mailings.insert().values(
            filter=mailing.filter,
            text_message=mailing.text_message,
            time_sending=mailing.time_sending,
            start_time=mailing.start_time,
            end_time=mailing.end_time
        )
        return await self.database.execute(query=query)

    async def update(self, mailing: MailingUpdate):
        query = mailings.update().where(mailings.c.id == mailing.id).values(
            filter=mailing.filter,
            text_message=mailing.text_message,
            time_sending=mailing.time_sending,
            start_time=mailing.start_time,
            end_time=mailing.end_time
        )
        await self.database.execute(query=query)

    async def delete(self, mailing: MailingDelete):
        query = mailings.delete().where(mailings.c.id == mailing.id)
        return await self.database.execute(query=query)

    async def get_all(self) -> list[Mailing]:
        query = mailings.select()
        mailings_list = await self.database.fetch_all(query=query)
        return [Mailing.parse_obj(mailing) for mailing in mailings_list]

    async def end_time_mailing(self, mailing_id: int):
        query = mailings.update().where(mailings.c.id == mailing_id).values(
            end_time=datetime.datetime.utcnow()
        )
        return await self.database.execute(query=query)
