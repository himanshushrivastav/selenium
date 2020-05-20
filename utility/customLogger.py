import logging
import inspect

def loggers(logLevel = logging.DEBUG):
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandle = logging.FileHandler("automation.log", mode='a')
    fileHandle.setLevel(logLevel)

    logFormat = logging.Formatter('%(asctime)s - %(name)s-(levelname)s: %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S:%p')
    fileHandle.setFormatter(logFormat)
    logger.addHandler(fileHandle)


    return logger

