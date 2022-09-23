import functools
import time
from typing import Any, Dict, List, Tuple
from library.constants.chars import  (
    COMMA_STRING,
    EMPTY_STRING,
    SPACE_STRING
)
from library.init import logger
from library.constants.messages import (INSIDE_FUNCTION)

def log_function_name(function: Any) -> Any:
    """Wrapper to log the function name
    :param function: function to be wrapped
    :type function: object
    :return: Function wrapper
    :rtype: object
    """
    # this is a decorator function where in it will log the function name
    def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        logger.debug(INSIDE_FUNCTION.format(function_name=function.__name__))

        return function(*args, **kwargs)

    return wrapper
def filter_option(filter_params: str) -> List[str]:
    """Create filter options

    :param filter_params: Filter parameter
    :type filter_params: str
    :return: List of filter options generated from filter parameters
    :rtype: List
    """
    result = []
    if filter_params:
        filter_params = filter_params.replace(COMMA_STRING, EMPTY_STRING)
        result = list(filter_params.split(SPACE_STRING))
    return result