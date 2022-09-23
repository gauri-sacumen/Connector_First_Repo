from library.init import configs, logger, filter_logger
from sac_requests.context.request import HttpRequest
from sac_requests.context.config import HttpConfig
from sac_requests.context.headers import HttpHeaders
from sac_requests.context.url import HttpURL
from library.constants.general import(
     EVENT_NOTIFICATIONS,
    ALERT_NOTIFICATIONS,
    DOME_NOTIFICATIONS,
    IRON_API,
    FILTERED_OUT_NOTIFICATIONS,
)
from library.constants.messages import(
    NOTIFICATIONS_NOT_AVAILABLE,
    GENERIC_ERROR ,
    

)
from library.filter.notifications import NotificationFilter
from library.init import (
    configs,
    data_queue,
    filter_logger,
    logger,
    notification_queue,
    metrics_queue
)
from library.constants.messages import(
    UNRECOGNISED_NOTIFICATION_TYPE,
)
from library.utils.general import log_function_name

def collect_notification() -> None:
    try:
        config = HttpConfig()
        endpoint = configs['iron_api']['event_endpoint']
        http_url = HttpURL(host='127.0.0.1',port=5000)
        headers = HttpHeaders({})
        data = {}
        notification_list = [
        EVENT_NOTIFICATIONS,
        ALERT_NOTIFICATIONS,
        DOME_NOTIFICATIONS
    ]
        http_request = HttpRequest(headers=headers,url=http_url, config=config)
        json_response = http_request.post(endpoint,data = data)
        content = json_response.json()
        if content and list(content.keys())[0] in notification_list:
                data_queue.add_to_queue(content)
        else:
            logger.error(
                UNRECOGNISED_NOTIFICATION_TYPE.format(
                    type=list(content.keys())[0], content=content
                )
            )
        #filter_logger.info(content)
    except Exception as e:
        filter_logger.info(e)

@log_function_name
def apply_filter() -> None:
    """Apply filter job

    It will read all the notifications from the notifications queue,
    apply filter on it and the send it to filter queue
    """
    try:
        nf = NotificationFilter()
        notifications = data_queue.read_from_queue()
        if notifications:
            for notification in notifications:
                notification_type = list(notification.keys())[0]
                result = nf.filter_notfications(
                    notification.get(notification_type, []),
                    notification_type,
                    configs,
                )
                notification_queue.add_to_queue({notification_type: result})
                if configs[IRON_API][FILTERED_OUT_NOTIFICATIONS]:
                    notification_filtered_out = nf.filtered_out_notifications(
                        notification.get(notification_type, []), result
                    )
                    filter_logger.info(
                        {notification_type: notification_filtered_out}
                    )
        
        else:
            logger.info(NOTIFICATIONS_NOT_AVAILABLE)
    except Exception as err:
        logger.exception(GENERIC_ERROR.format(exception=str(err)))
