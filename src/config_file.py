import toml
import os


class ConfigFile:

    CONFIG_FILE_PATH = f'{os.environ["HOME"]}/.chpwd_cmd'

    def __init__(self):
        try:
            self.config = toml.load(open(self.CONFIG_FILE_PATH))
        except toml.decoder.TomlDecodeError as e:
            raise ConfigFileError(e) from None
        except FileNotFoundError as e:
            raise ConfigFileError(
                f'configuration file ({self.CONFIG_FILE_PATH})\
                    does not exist {e}') from None


class ConfigFileError(Exception):
    pass
