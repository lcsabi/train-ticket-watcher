import logging


def setup_logger(name: str):
    # Set logger level
    logging.basicConfig(level=logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler('app.log')

    # Create a console handler
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)

    # Create logger and add handlers
    logger = logging.Logger(name)
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logger
