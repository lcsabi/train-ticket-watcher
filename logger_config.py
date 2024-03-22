import logging


def setup_logger(name: str):
    logging.basicConfig(level=logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler('app.log')

    # Console handler
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)

    # Formatter, set handlers
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)

    # Logger, add handlers
    logger = logging.Logger(name)
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logger
