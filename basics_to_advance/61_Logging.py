from logging import *

# debug('This is debug')
# warning('This is warning')
# error('This is error')
# critical('This is critical')

# *** {name} *** also we can use this , style = '{

LOG_FORMAT = '%(lineno)s , %(name)s , %(asctime)s // %(message)s // %(lineno)d'
basicConfig (filename='logfile.log' , level=DEBUG , filemode='w' , format=LOG_FORMAT)

logger = getLogger('Geek')

logger.debug('This is debug')
info('This is info')
warning('This is warning')
error('This is error')
critical('This is critical')

