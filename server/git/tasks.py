from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .dataInterface import updateAPIData

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/60')),
    name="taskUpdateAPIData",
    ignore_result=True
)
def taskUpdateAPIData():
    """
    Update the database with data from the repository
    """
    updateAPIData()
    logger.info("Updated database")
