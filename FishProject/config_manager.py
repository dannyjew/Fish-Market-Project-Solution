from definitions import PROJECT_ROOT_DIR
import configparser
import os

_config = configparser.ConfigParser()

_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

BUCKETNAME = _config['default']['bucketname']
TARTARE = _config['default']['fishsource']  # Tartare cause it's the fish sauce

