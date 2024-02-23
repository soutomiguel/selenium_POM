import configparser


def read_configurations(category, key):
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    return config.get(category, key)
