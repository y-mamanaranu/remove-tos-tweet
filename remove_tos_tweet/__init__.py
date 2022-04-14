"""Remove @tos tweet."""

__version__ = '0.1.0'

import glob
import os
from pathlib import Path

from traitlets.config import Config
from traitlets.config.configurable import Configurable
from traitlets.config.loader import PyFileConfigLoader

__all__ = [
    os.path.split(os.path.splitext(file)[0])[1]
    for file in glob.glob(os.path.join(
        os.path.dirname(__file__), '[a-zA-Z0-9]*.py'))
]

lib_name = "Remove_tos_tweet"
rep_name = lib_name.lower()


def get_configdir(create: bool = False) -> Path:
    """Return path of the the configuration directory: CONFIGDIR.

    The directory is chosen as follows:
    1. ``$HOME/.config/{rep_name}``
    2. ``$HOME/.{rep_name}``
    """

    def gen_candidates():
        yield Path.home() / ".config" / rep_name
        yield Path.home() / f".{rep_name}"

    for path in gen_candidates():
        if path.exists() and path.is_dir():
            return path

    for path in gen_candidates():
        if path.parent.exists() and path.parent.is_dir():
            if create:
                path.mkdir(parents=True, exist_ok=True)
            return path


def fname(create: bool = False):
    """Return path of the the config file.

    The file location is chosen as follows
    1. ``$(pwd)/{rep_name}rc.py``
    2. ``$CONFIGDIR/config.py``
        ``$CONFIGDIR`` is determined by ``get_configdir``
    3. ``$HOME/.{rep_name}rc.py``
    4. ``$HOME/.config/{rep_name}rc.py``
    """

    def gen_candidates():
        yield Path.cwd() / f"{rep_name}rc.py"
        yield get_configdir() / "config.py"
        yield Path.home() / f".{rep_name}rc.py"
        yield Path.home() / ".config" / f"{rep_name}rc.py"

    for cand in gen_candidates():
        if cand.exists() and not cand.is_dir():
            return cand

    if create:
        message = "\n".join([
            "\n",
            "No config file is found. "
            "Copy default config file to the path below.",
            "Default config file path:",
            f"\t{fname_default()}",
            "Config file path:",
            *[f"\t{p}" for p in gen_candidates()],
        ])
        raise FileNotFoundError(message)


def fname_default():
    """Return path of the the default config file."""
    return Path(__file__).with_name("config.py")


def load_config(create: bool = False):
    """Load config."""
    p = fname_default()
    PyFileConfigLoader(str(p)).load_config()

    p = fname(create=create)
    if p:
        PyFileConfigLoader(str(p)).load_config()


# define c before load_config()
c = Configurable.config = Config()
load_config(create=True)
