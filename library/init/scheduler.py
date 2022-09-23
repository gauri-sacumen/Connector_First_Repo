import os
from typing import Any, Dict
from library.constants.general import(SCHEDULER,
    SCHEDULER_CONFIG_DIR,
    SCHEDULER_CONFIG_FILE,)
from library.init.utils import read_yaml
from sac_scheduler.schedule import Schedule


def get_configurations() -> Dict[str, Any]:
    """Get configurations for scheduler

    :return: Scheduler configurations
    :rtype: Dict
    """
    from library.init import configs

    filename = os.path.join(
        configs[SCHEDULER][SCHEDULER_CONFIG_DIR],
        configs[SCHEDULER][SCHEDULER_CONFIG_FILE],
    )
    return read_yaml(filename)


def init_scheduler() -> Schedule:
    """Initialise scheduler

    :return: Scheduler object
    :rtype: Schedule
    """
    configurations = get_configurations()
    schedule = Schedule()
    schedule.add_jobs(configurations)
    return schedule
