import logging


def setup_logger(name: str):
    # Configure the root logger
    logging.basicConfig(level=logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler('app.log')

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)

    # Get the root logger
    logger = logging.Logger(name)
    logger.addHandler(file_handler)

    return logger
