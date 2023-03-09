import logging

# LOGGING

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', # da formato a como se muestran los logs
    datefmt='%d-%m-%Y %H:%M:%S', # format time in log
    level=logging.DEBUG, # define el grado de alerta minimo a mostrar
    filename='logs_test1.txt' # indica el archivo donde guardara los logs
)

logger = logging.getLogger(__name__)

logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message')
logger.critical('This is Critical')



"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""



