# Save this as logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import graypy

def setup_logging(console_level=logging.DEBUG, 
                  file_level=logging.INFO, 
                  graylog_level=logging.WARNING, 
                  log_file="app.log", 
                  graylog_host="localhost", 
                  graylog_port=12201):
    """
    Set up modular logging with console, file, and Graylog handlers.

    Args:
        console_level (int): Logging level for console output.
        file_level (int): Logging level for file output.
        graylog_level (int): Logging level for Graylog output.
        log_file (str): Path to the log file.
        graylog_host (str): Hostname for the Graylog server.
        graylog_port (int): Port for the Graylog server.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger("modular_logger")
    logger.setLevel(logging.DEBUG)  # Set the base level to the lowest to catch all messages

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(file_level)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Graylog handler
    graylog_handler = graypy.GELFUDPHandler(graylog_host, graylog_port)
    graylog_handler.setLevel(graylog_level)
    logger.addHandler(graylog_handler)

    return logger


# Example usage
if __name__ == "__main__":
    logger = setup_logging(
        console_level=logging.DEBUG,
        file_level=logging.INFO,
        graylog_level=logging.WARNING,
        log_file="app.log",
        graylog_host="localhost",
        graylog_port=12201
    )

    logger.debug("This is a debug message (console only).")
    logger.info("This is an info message (console and file).")
    logger.warning("This is a warning message (console, file, and Graylog).")
    logger.error("This is an error message (console, file, and Graylog).")
    logger.critical("This is a critical message (console, file, and Graylog).")
