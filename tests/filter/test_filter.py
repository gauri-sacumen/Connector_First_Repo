from library.filter.notifications import NotificationFilter
from library.init import configs
import pdb
nf = NotificationFilter()


def test_dome_notification_filter():

    notifications = [
        {
            "id": 123456,
            "category": "DNC_PARTICIPANT_ADDED",
            "created": "2021-05-26T07:41:35Z",
            "dome_tags": ["foo", "bar", "baz"],
            "alert_ids": ["12345000-0000-0000-0000-000000000000"],
        },
        {
            "id": 123457,
            "category": "OTHER",
            "created": "2021-05-26T07:41:35Z",
            "dome_tags": ["foo", "bar", "baz"],
            "alert_ids": ["12345000-0000-0000-0000-000000000000"],
        },
    ]

    res = nf.dome_notification_filter(notifications, configs)
    assert isinstance(res, list)

#test_event_notification_filter
def test_event_notification_filter():
    notifications = [
        {
            "event_action": "ACTION-1",
            "event": {
                "id": "1d59f474-f2a7-4ef0-9e4e-3da61c1fbcc1",
                "alert_id": "",
                "category": "CAT-1",
                "sub_category": "SUB-CAT-1",
                "severity": 1000,
                "confidence": 1,
                "is_whitelisted": False,
                "is_blacklisted": True,
            },
        },
        {
            "event_action": "ENA_EVENT_ADDED_TO_ALERT",
            "event": {
                "id": "1d59f474-f2a7-4ef0-9e4e-3da61c1fbcc1",
                "alert_id": "",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 1000,
                "confidence": 1,
                "is_whitelisted": False,
                "is_blacklisted": True,
            },
        },
    ]

    configs["event_notifications"]["severity"] = 500
    res = nf.event_notification_filter(notifications, configs)

    assert isinstance(res, list)


def test_alert_notification_filter():
    notifications = [
        {
            "alert_action": "ANA_ALERT_CREATED",
            "alert": {
                "id": "12345000-0000-0000-0000-000000000000",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
        {
            "alert_action": "ANA_ALERT_CREATED",
            "alert": {
                "id": "12545000-0000-0000-0000-000000000000",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
    ]
    configs["alert_notifications"]["severity"] = 500

    res = nf.alert_notification_filter(notifications, configs)

    assert isinstance(res, list)


def test_filter_notifications():
    notifications = [
        {
            "alert_action": "ANA_ALERT_CREATED",
            "alert": {
                "id": "12345000-0000-0000-0000-00000000123",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
        {
            "alert_action": "ANA_ALERT_CREATED",
            "alert": {
                "id": "12545000-0000-0000-0000-000000000000",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
    ]
    notification_type = "alert_notifications"

    res = nf.filter_notfications(notifications, notification_type, configs)

    assert isinstance(res, list)


def test_filtered_out_notifications():

    notifications_received = [
        {
            "alert_action": "ANA_WORKFLOW_CREATED",
            "alert": {
                "id": "12345000-0000-0000-0000-000000000000",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
        {
            "alert_action": "ANA_ALERT_CREATED",
            "alert": {
                "id": "12545000-0000-0000-0000-00000000123",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
    ]

    notifications_filterpassed = [
        {
            "alert_action": "ANA_WORKFLOW_CREATED",
            "alert": {
                "id": "12345000-0000-0000-0000-000000000000",
                "category": "OTHER",
                "sub_category": "OBSERVED_BAD_ACTIVITY",
                "severity": 600,
                "status": "STATUS-1",
            },
        },
    ]
    res = nf.filtered_out_notifications(notifications_received, notifications_filterpassed)
    pdb.set_trace()

    assert res[0].get('alert_action') == 'ANA_ALERT_CREATED'
    assert isinstance(res, list)
