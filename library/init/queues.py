from library.init.notification_queue import NotificationQueue
from sac_queue.dataqueue import DataQueue  # type: ignore
from sac_queue.metricsqueue import MetricsQueue  # type: ignore


def init_metrics_queue() -> MetricsQueue:
    """Initialise metrics queue to be used as common resource to put metrics data

    :return: metrics queue object
    :rtype: MetricsQueue
    """
    return MetricsQueue.instance()


def init_data_queue() -> DataQueue:
    """Initialise data queue to be used as common resource to put metrics data

    :return: metrics queue object
    :rtype: DataQueue
    """
    return DataQueue.instance()


def init_notification_queue() -> DataQueue:
    """Initialise notification queue to be used to store filtered notifications

    :return: metrics queue object
    :rtype: NotificationQueue
    """
    return NotificationQueue.instance()
