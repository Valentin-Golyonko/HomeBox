import logging
from random import randint

from celery import shared_task

from config.celery import app

logger = logging.getLogger(__name__)


@app.task
def morning_alarm(**kwargs) -> None:
    logger.debug(f"time to wake up! {kwargs.get('hello')}")
    return None


@shared_task
def task_celery_test_run() -> int:
    some_int = randint(0, 10)
    logger.debug(f"task_celery_test_run(): some_int: {some_int}.")
    return some_int
