from configparser import ConfigParser, SectionProxy
from xkcdpass import xkcd_password


class Config:
    pass

class ConfigSection:
    def __init__(self, section: SectionProxy, items_type: str):
        for key in section:
            if items_type == "string":
                self.__setattr__(key, section[key])
            elif items_type == "int":
                try:
                    self.__setattr__(key, section.getint(key))
                except ValueError:
                    print(f'Could not convert option [{section.name}] -> "{key}" to int')
                    raise


# Global config object
config = Config()


def check_config_file(filename: str) -> bool:
    required_structure = {
        "general": ["token", "db_file", "words_file"],
        "pwd_words": ["min", "max"]
    }

    global config
    parser = ConfigParser()
    parser.read(filename)

    # Check required sections and options in them
    if len(parser.sections()) == 0:
        print("Config file missing or empty")
        return False
    for section in required_structure.keys():
        if section not in parser.sections():
            print(f'Missing section "{section}" in config file')
            return False
        for option in required_structure[section]:
            if option not in parser[section]:
                print(f'Missing option "{option}" in section "{section}" of config file')
                return False

    # Read again, now create Config
    objects_type = {"general": "string", "pwd_words": "int"}
    for section in parser.sections():
        try:
            config.__setattr__(section, ConfigSection(parser[section], items_type=objects_type[section]))
        except ValueError:
            return False

    # Load words database into config
    config.__setattr__("wordlist", xkcd_password.generate_wordlist(wordfile=parser["general"]["words_file"],
                                                                   min_length=4, max_length=10, valid_chars="[a-z]"))

    return True
