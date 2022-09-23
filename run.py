"""
this is the start point of the collector module
"""
#from distutils.command import config
import time
from sac_configurations.context.certify import CertifyConfigurations
from library.init import configs, get_schema_definition, logger , filter_logger
from library.constants.messages import (LOGGER_INITIALISED,CONFIG_VERIFICATION_SUCCESS)
from library.init.scheduler import init_scheduler
from sac_requests.context.request import HttpRequest
from sac_requests.context.config import HttpConfig
from sac_requests.context.headers import HttpHeaders
from sac_requests.context.url import HttpURL



if __name__ == "__main__":
    try:
        logger.info(LOGGER_INITIALISED)
        schema = get_schema_definition()
        certify = CertifyConfigurations(schema)
        certify.verify_n_assign_default(configs)
        logger.info(CONFIG_VERIFICATION_SUCCESS)
        try:
            scheduler = init_scheduler()
            scheduler.scheduler.start()
            while True:
            # Sleep is added to make the scheduler available
            # for other jobs.
                time.sleep(10)
        except Exception as exp:
            print(exp)
            scheduler.shutdown()

    except Exception as exp:
        print(exp)