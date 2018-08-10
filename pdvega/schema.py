from pkgutil import get_data
from json import loads

VEGALITE_FILE = 'v2.4.3.json'
VEGALITE_SCHEMA = loads(get_data('pdvega', VEGALITE_FILE).decode('utf-8'))