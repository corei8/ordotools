import logging


logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s', level=logging.INFO)
