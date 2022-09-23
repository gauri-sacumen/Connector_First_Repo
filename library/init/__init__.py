from typing import Any, Dict, List, Tuple
import os
from sac_configurations.context.schema import Schema
from sac_configurations.input.cfg import CFGConfig
# from sac_log.logger import get_logger  # type: ignore
from library.init.scheduler import init_scheduler
from sac_log.logger import get_logger
from library.syslog.logger import get_sys_logger
from library.init.queues import (
    init_data_queue,
    init_metrics_queue,
    init_notification_queue,
)
from library.constants.general import(
    CLASS_ID_CFG,
    CONFIG,
    CONFIGURATION_CFG,
    FILTER_OUT,
    LOG_CONFIG_CFG,
    SCHEMA_CONFIG_YAML,
    LOGGING,
    INN_COLLECTOR,
    FILTER_OUT_LOG,
    INN_SYSLOG_COLLECTOR,
    SYSLOG,
)
def get_schema_definition() -> Schema:
    """Generate schema definition

    :return: Schema definition
    :rtype: Schema
    """
    filename = os.path.join(CONFIG, SCHEMA_CONFIG_YAML)
    return Schema(filename)

def get_config_file_list() -> List[Any]:
    """Get list of configurations files

    :return: List of configurations files
    :rtype: List
    """
    file_list = []
    for item in [CONFIGURATION_CFG, LOG_CONFIG_CFG, CLASS_ID_CFG]:
        filename = os.path.join(CONFIG, item)
        file_list.append(filename)
    return file_list

def read_configurations(filenames: List[str]) -> Dict[str, Any]:
    """Read configurations from the configuraiton files

    :param filenames: List of configurations files
    :type filenames: List
    :return: Configurations read from the list of configurations files
    :rtype: Dict
    """
    config = CFGConfig()
    config.read(filenames)
    return config.to_dict()


def get_configurations() -> Dict[str, Any]:
    """Get configurations privided in configurations files

    :return: Configuraitons read from configurations files
    :rtype: Dict
    """
    file_list = get_config_file_list()
    return read_configurations(file_list)

def init_queues() -> Any:
    """Initialise queues like metrics queue, data queue, and notifications queue

    :return: [description]
    :rtype: [type]
    """
    # Get metrics queue
    metrics_queue = init_metrics_queue()
    # Get data queue
    data_queue = init_data_queue()
    # Get notification queue
    notification_queue = init_notification_queue()

    return metrics_queue, data_queue, notification_queue


# Get configurations
configs = get_configurations()
# Get logger instance
logger = get_logger(INN_COLLECTOR, configs[LOGGING])
metrics_queue, data_queue, notification_queue = init_queues()


filter_logger = get_logger(INN_COLLECTOR, configs[FILTER_OUT])


