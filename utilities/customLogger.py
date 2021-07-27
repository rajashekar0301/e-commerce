import logging
import os
log_dir = os.path.join(os.path.normpath(os.getcwd()), 'Logs')
print(log_dir)
log_fname = os.path.join(log_dir, 'log_file_name.log')
print(log_fname)

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create a file handler
        handler_warn = logging.FileHandler('..\\Logs\\warning_log.txt')
        handler_warn.setLevel(logging.WARNING)

        handler_info = logging.FileHandler('..\\Logs\\info_log.txt')
        handler_info.setLevel(logging.INFO)

        handler_err = logging.FileHandler('..\\Logs\\error_log.txt')
        handler_err.setLevel(logging.ERROR)

        # create a logging format

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler_warn.setFormatter(formatter)
        handler_info.setFormatter(formatter)
        handler_err.setFormatter(formatter)

        # add the handler to the logger

        logger.addHandler(handler_warn)
        logger.addHandler(handler_info)
        logger.addHandler(handler_err)

        logger.info('Information')
        logger.warning('warning')
        logger.error('Error')

        return logger
