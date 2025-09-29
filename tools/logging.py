import datetime

class Logger:
    @staticmethod
    def info(message):
        """Log an info message with timestamp"""
        print(f"[INFO] {datetime.datetime.now()} - {message}")

    @staticmethod
    def error(message):
        """Log an error message with timestamp"""
        print(f"[ERROR] {datetime.datetime.now()} - {message}")

    @staticmethod
    def warning(message):
        """Log a warning message with timestamp"""
        print(f"[WARNING] {datetime.datetime.now()} - {message}")
