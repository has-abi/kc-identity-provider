import logging
from logging.config import fileConfig

from pkg_resources import resource_filename

fileConfig(
    fname=resource_filename("src", "logger.cfg"),
    disable_existing_loggers=False,
    defaults={
        "kc-identity-provider-level": "DEBUG",
        "kc-identity-provider-formatter": "classic",
    },
)

logger = logging.getLogger("kc-identity-provider")
