import logging
from logging.handlers import RotatingFileHandler
import time
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('my_log.log', maxBytes=30, backupCount=10)
logger.addHandler(handler)

for _ in range(10000):
    logger.debug('Hello, world!')
    time.sleep(3)