"""This module contains config for tic-tac-toe"""
from pathlib import Path
from dataclasses import dataclass
import logging.config

import yaml

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / 'logs'
CONFIG_LOGER_FILE = BASE_DIR / 'config.yaml'


def config_logger():
    """This function open config.yaml for describe the configuration logging"""
    with open(CONFIG_LOGER_FILE, 'r', encoding="utf-8") as conf_file:
        config = yaml.safe_load(conf_file.read())
        logging.config.dictConfig(config)


@dataclass
class WindowResolution:
    """Class for keeping track of the size of the terminal window."""
    height: int
    width: int
