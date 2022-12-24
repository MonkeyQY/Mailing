from app.db.mailing import mailings
from app.models.mailing import MailingDelete, MailingUpdate, MailingAdd, Mailing
from app.repositories.base_repository import BaseRepository


class MailingRepository(BaseRepository):

    async def get_by_id(self, mailing_id: int) -> Mailing:
        query = mailings.select().where(mailings.c.id == mailing_id)
        mailing = await self.database.fetch_one(query=query)
        return Mailing.parse_obj(mailing)

    async def create(self, mailing: MailingAdd):
        query = mailings.insert().values(mailing.filter,
                                         mailing.text_message)
        return await self.database.execute(query=query)

    async def update(self, mailing: MailingUpdate):
        query = mailings.update().where(mailings.c.id == mailing.id).values(
            mailing.filter,
            mailing.text_message)
        return await self.database.execute(query=query)

    async def delete(self, mailing: MailingDelete):
        query = mailings.delete().where(mailings.c.id == mailing.id)
        return await self.database.execute(query=query)
