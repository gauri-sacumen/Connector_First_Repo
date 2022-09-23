from queue import Queue
from typing import Any

from sac_queue.base import BaseQueue  # type: ignore


class NotificationQueue(BaseQueue): # type: ignore
    """NotificationQueue class to store filtered notifications.

    This is FIFO queue and follows thread safety.
    Queue follows the Singleton design pattern hence object
    is not allowed to create with __init__ method,
    instead instance() method needs to be called which creates
    an object only if no object is created
    or else it will return the existing object

    :param BaseQueue: Inherits base Queue class
    :type BaseQueue: class
    :raises RuntimeError: raises exception is an object
    is created without instance() method
    :return: Notification Queue Object
    :rtype: NotificationQueue
    """

    _instance: Any = None
    queue: Any = None

    def __init__(self) -> None:
        """Initialize the NotificationQueue Object

        :raises RuntimeError: This follows Singleton design pattern,
        hence creation of the instance should not be allowed
        via instance directly
        """
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls) -> BaseQueue:
        """Instance method to create the instance of NotificationQueue class.

        This follows Singleton design pattern

        :return: NotificationQueue instance
        :rtype: BaseQueue
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.queue = Queue()
        return cls._instance
