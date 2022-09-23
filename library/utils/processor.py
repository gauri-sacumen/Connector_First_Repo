from typing import Dict, Any

from library.constants.chars import EMPTY_STRING

def get_key_from_value(value: str, dct: Dict[str, Any]) -> str:
    """Get key from value in the dictinory

    :param value: value for which key to be searched
    :type value: str
    :param dct: Dictionary in which to look for value
    :type dct: Dict
    :return: Key corresponding to the value in dct
    :rtype: str
    """
    key_list = list(dct.keys())
    value_list = list(dct.values())

    index = value_list.index(value) if value in value_list else -1
    return key_list[index] if index >= 0 else EMPTY_STRING
