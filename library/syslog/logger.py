import logging
import socket
from logging import Formatter, Logger
from logging.handlers import SysLogHandler
from typing import Any, Dict
from library.constants.general import (
   ADDRESS,
    FACILITY,
    HOST,
    IS_FILE,
    PORT,
    SOCK_TYPE,
    TCP,
    TIME_FORMAT, 
)

from library.utils.processor import get_key_from_value
from sac_log.constants import LOG_FORMATTER, LOG_LEVEL  # type: ignore


def get_sys_logger(name: str, config: Dict[str, Any]) -> Logger:
    """Get logger object to enable logging

    :param name: Log file path
    :type name: str
    :param config: configurations dictionary containing
    :type config: Dict
    :return: Logger object
    :rtype: Logger
    """
    # Create a logger object
    logger: Logger = logging.getLogger(name)
    logger.setLevel(config[LOG_LEVEL])

    # Set socket type
    socket_type: socket.SocketKind = None
    if config[SOCK_TYPE] == TCP:
        socket_type = socket.SOCK_STREAM
    else:
        socket_type = socket.SOCK_DGRAM

    # Set address
    address = None
    if not config[IS_FILE]:
        # if logging is not enabled from file, address is remote ip and port
        address = (config[HOST], config[PORT])
    else:
        # It is address value configured
        address = config[ADDRESS]

    # Set facility for syslog handler
    facility = getattr(SysLogHandler, str(config[FACILITY]).upper())
    facilty_name = get_key_from_value(facility, SysLogHandler.facility_names)

    # Get formatter for sys log handler
    format_str: str = str(config[LOG_FORMATTER]).format(
        name=name, facility=facilty_name
    )
    formatter: Formatter = Formatter(format_str, config[TIME_FORMAT])
    # Create Syslog handler
    handler = SysLogHandler(
        address=address,
        facility=facility,
        socktype=socket_type
    )
    # Set formatter for the syslog handler
    handler.setFormatter(formatter)

    # add handler to the log
    logger.addHandler(handler)

    return logger
