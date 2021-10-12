def finalLog():
    import logging
    from logging.handlers import RotatingFileHandler

    logging.basicConfig(
    handlers=[RotatingFileHandler('./my_log.log',maxBytes=200000)],
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s  %(message)s",
    datefmt='%Y-%m-%dT%H:%M:%S')