from library.constants.messages import(NOTIFICATIONS_COLLECTOR_JOB_STARTED,NOTIFICATIONS_COLLECTOR_JOB_ENDED,NOTIFICATIONS_FILTER_JOB_STARTED ,
NOTIFICATIONS_FILTER_JOB_ENDED 
)
from library.init import logger , filter_logger
from library.init import configs
from library.collector.api import collect_notification , apply_filter
# from library.init.scheduler import get_configurations

def notifications_collector_job() -> None:
    
    """Job to collect notifications from IronAPI
    """
    #logger.info(NOTIFICATIONS_COLLECTOR_JOB_STARTED)
    collect_notification()
    #logger.info(NOTIFICATIONS_COLLECTOR_JOB_ENDED) 

def notifications_filter_job() -> None:
    """Job to read notifications from Data queue, filter it and write to Notifications queue.
    """
    filter_logger.info(NOTIFICATIONS_FILTER_JOB_STARTED)
    apply_filter()
    filter_logger.info(NOTIFICATIONS_FILTER_JOB_ENDED)