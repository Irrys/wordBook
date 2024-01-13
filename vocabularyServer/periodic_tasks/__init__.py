from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from periodic_tasks.filter_review_words import filter_review_words
from periodic_tasks.send_words_to_notion import create_words_toggle_block
import datetime


class Task:

    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def _find_tasks(self):
        pass

    def _registry_tasks(self):
        self.scheduler.add_job(filter_review_words, CronTrigger(hour=16, minute=47))
        self.scheduler.add_job(filter_review_words, DateTrigger(run_date=datetime.datetime.now()))
        self.scheduler.add_job(create_words_toggle_block, DateTrigger(run_date=datetime.datetime.now()))

    def start(self):
        self._registry_tasks()
        self.scheduler.start()
