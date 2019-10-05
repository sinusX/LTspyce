import logging


def default_log(lvl):
    logger = logging.getLogger('LTspyce')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('LTspyceLog.log')
    fh.setLevel(lvl)
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(format)
    logger.addHandler(fh)
