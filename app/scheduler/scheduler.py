from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app import config
from app.send_statistic_for_mail.send_statistic_for_users import send_statistic_for_users

schedule = AsyncIOScheduler(job_defaults={
    'max_instances': 1,
    'coalesce': True,
    'misfire_grace_time': 3600
})


async def start_scheduler():
    schedule.add_job(send_statistic_for_users, 'cron', hour=config.hour_send_statistic)
    schedule.start()