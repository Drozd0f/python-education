"""This module stores configuration information"""
from pathlib import Path
from dataclasses import dataclass


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = Path('src/template').resolve()


@dataclass
class WindowResolution:
    """Class for keeping track of the size of the terminal window."""
    height: int
    width: int
