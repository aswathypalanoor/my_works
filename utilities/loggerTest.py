import logging
import os

class Log_Maker:
    @staticmethod
    def log_gen():
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "nopcommerce.log")

        logger = logging.getLogger("nopcommerceLogger")
        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
