import logging
from dataclasses import dataclass

@dataclass
class LoggerConfig:
    level: int = logging.ERROR
    format: str = ""

@dataclass
class DiscordConfig:
    token: str
    guid: str


@dataclass
class BotConfig:
    command_prefix: str
    discord: DiscordConfig
