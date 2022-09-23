from typing import Any, Callable, Dict, List
from library.constants.general import(
    ACTION,
    ALERT,
    ALERT_ACTION,
    ALERT_NOTIFICATIONS,
    CATEGORY,
    DOME_NOTIFICATIONS,
    EVENT,
    EVENT_ACTION,
    EVENT_NOTIFICATIONS,
    IS_BLACKLISTED,
    IS_WHITELISTED,
    SEVERITY,
    STATUS,
    SUB_CATEGORY, 
)

from library.utils.general import filter_option
# from api_notifications.init import metrics_queue
# from api_notifications.metrics.filter import FilterMetrics


class NotificationFilter(object):
    """Notifications filters class

    :param object: Inherits basic object
    :type object: class
    """

    def _get_filter_function(
        self, notification: str
    ) -> Callable[[List[Any], Dict[Any, Any]], List[Any]]:
        """Get filter function for the notification

        :param notification: Notification for which filter function is required
        :type notification: str
        :return: Filter function as object
        :rtype: Callable[[List, Dict], List]
        """
        filters = {
            ALERT_NOTIFICATIONS: self.alert_notification_filter,
            EVENT_NOTIFICATIONS: self.event_notification_filter,
            DOME_NOTIFICATIONS: self.dome_notification_filter,
        }
        return filters.get(notification)

    def filter_notfications(
        self,
        notifications: List[Dict[str, Any]],
        notification_type: str,
        configs: Dict[Any, Any],
    ) -> List[Dict[str, Any]]:
        """Returns the filter pass notifications

        :param notifications: Notification List
        :type notifications: List
        :param notification_type: Type of Notification to filter
        :type notification_type: str
        :param configs: Configurations
        :type configs: Dict
        :return: Collection of filtered notifications
        :rtype: List
        """
        # Get notifications received count
        received_count = len(notifications)

        filtered_notification = []
        # Get filter function
        func = self._get_filter_function(notification_type)
        # Filter notifications
        filtered_notification = func(notifications, configs)

        # Get notifications processed count
        processed_count = len(filtered_notification)

        # Calculate notifications filtered count
        #filtered_count = received_count - processed_count

        # Generate Notification Metrics
        # metrics = FilterMetrics(
        #     notification_type, received_count, filtered_count, processed_count
        # )
        # metrics_queue.add_to_queue(metrics)
        return filtered_notification

    def event_notification_filter(
        self, notifications: List[Any], configs: Dict[Any, Any]
    ) -> List[Any]:
        """Filter out the event_notifactions

        :param notifications: Notifications to be filtered
        :type notifications: Dict
        :param configs: Configurations containing filter options
        :type configs: Dict
        :return: Filtered notificaitons
        :rtype: List
        """
        results = []
        if notifications:
            for event in notifications:
                if (
                    event[EVENT_ACTION]
                    not in filter_option(configs[EVENT_NOTIFICATIONS][ACTION])
                    and event[EVENT][CATEGORY]
                    not in filter_option(
                        configs[EVENT_NOTIFICATIONS][CATEGORY])
                    and event[EVENT][SUB_CATEGORY]
                    not in filter_option(
                        configs[EVENT_NOTIFICATIONS][SUB_CATEGORY])
                    and event[EVENT][SEVERITY]
                    >= (configs[EVENT_NOTIFICATIONS][SEVERITY])
                    and event[EVENT][IS_WHITELISTED]
                    != (configs[EVENT_NOTIFICATIONS][IS_WHITELISTED])
                    and event[EVENT][IS_BLACKLISTED]
                    != (configs[EVENT_NOTIFICATIONS][IS_BLACKLISTED])
                ):
                    results.append(event)

        return results

    def alert_notification_filter(
        self, notifications: List[Any], configs: Dict[Any, Any]
    ) -> List[Any]:
        """Filter out the alert_notifactions

        :param notifications: Alert notifications
        :type notifications: List
        :param configs: Configurations
        :type configs: Dict
        :return: List of filtered allert notifications
        :rtype: List
        """
        results = []
        if notifications:
            for alert in notifications:
                if (
                    alert[ALERT_ACTION]
                    not in filter_option(configs[ALERT_NOTIFICATIONS][ACTION])
                    and alert[ALERT][CATEGORY]
                    not in filter_option(
                        configs[ALERT_NOTIFICATIONS][CATEGORY])
                    and alert[ALERT][SUB_CATEGORY]
                    not in filter_option(
                        configs[ALERT_NOTIFICATIONS][SUB_CATEGORY])
                    and alert[ALERT][STATUS]
                    not in filter_option(configs[ALERT_NOTIFICATIONS][STATUS])
                    and alert[ALERT][SEVERITY]
                    >= (configs[ALERT_NOTIFICATIONS][SEVERITY])
                ):
                    results.append(alert)
        return results

    def dome_notification_filter(
        self, notifications: List[Any], configs: Dict[Any, Any]
    ) -> List[Any]:
        """Filter out the dome_notifactions

        :param notifications: Dome notifications
        :type notifications: List
        :param configs: Configurations
        :type configs: Dict
        :return: Filtered dome notifications
        :rtype: List
        """
        results = []
        if notifications:
            for dome in notifications:
                if dome[CATEGORY] not in filter_option(
                    configs[DOME_NOTIFICATIONS][CATEGORY]
                ):
                    results.append(dome)
        return results

    def filtered_out_notifications(
        self, received: List[Any], filterpass: List[Any]
    ) -> List[Any]:
        """get filtered out notifications

        :param received: Notifications recieved
        :type received: List
        :param filterpass: Notifications passed via filter
        :type filterpass: List
        :return: Filter out notifications
        :rtype: List
        """
        filter_out = []
        for notification in received:
            if notification not in filterpass:
                filter_out.append(notification)

        return filter_out
