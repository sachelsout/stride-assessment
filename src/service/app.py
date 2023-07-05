import os
import logging
from merger import MergerService

# OS code (code working on different OS machines)
if os.name == 'nt':
    FULL_PATH = '/'.join((os.path.abspath(__file__).replace('\\',
                         '/')).split('/')[:-1])
elif os.name == 'posix':
    FULL_PATH = '/'.join(os.path.abspath(__file__).split('/')[:-1])
else:
    raise OSError('untested OS')

# creating log file folder/directory, if it doesn't exists
LOG_FILE_PATH = FULL_PATH + '/logFile'
os.makedirs(LOG_FILE_PATH, exist_ok=True)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)-3d:%(filename)s:%(funcName)s:%(levelname)s:%(lineno)d:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename=LOG_FILE_PATH +'/logger.log',
                    force=True)

# run the app/service 
if __name__ == "__main__":
    
    try:
        service = MergerService()
        service.merge()
    
    except Exception as service_ERR:
        logging.error('service error', exc_info=service_ERR)
else:
    logging.critical('service error')