import logging


# logging.basicConfig(filename='app.log', filemode='w',
#                     format='%(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s', level=logging.INFO)


# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s')
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
