import datetime

class Logger:
    def info(self, message):
        """Log an info message with timestamp"""
        print(f"[INFO] {datetime.datetime.now()} - {message}")

    def error(self, message):
        """Log an error message with timestamp"""
        print(f"[ERROR] {datetime.datetime.now()} - {message}")

    def warning(self, message):
        """Log a warning message with timestamp"""
        print(f"[WARNING] {datetime.datetime.now()} - {message}")
