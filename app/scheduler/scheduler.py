from apscheduler.schedulers.asyncio import AsyncIOScheduler

schedule = AsyncIOScheduler(job_defaults={
    'max_instances': 1,
    'coalesce': True,
    'misfire_grace_time': 3600
})


async def start_scheduler():
    schedule.start()