from typing import Any, Dict

from sac_configurations.input.yaml import YamlConfig


def read_yaml(filename: str) -> Dict[str, Any]:
    """Read Yaml configurations

    :param filename: Yaml configurations file path
    :type filename: str
    :return: Yaml configurations converted to dictionary
    :rtype: Dict
    """
    yaml_config = YamlConfig()
    yaml_config.read([filename])
    return yaml_config.to_dict()
