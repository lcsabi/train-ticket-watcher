import logging


def setup_logger():
    # Configure the root logger
    logging.basicConfig(level=logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)

    # Create a console handler
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(message)s')
    file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)

    # Attach the handlers to the logger
    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logging.getLogger(__name__)
