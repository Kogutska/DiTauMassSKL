
## loging
import logging
logging.basicConfig()

## a local module for color coding logging
from . import colorer
## to create a log file
#logging.basicConfig(filename='prepare-data-set.log',level=logging.DEBUG)
# create logger
logger = logging.getLogger('ROOT to H5')
logger.setLevel(logging.INFO)
