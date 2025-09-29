from datetime import datetime
import re

class Validator:
    def is_positive(self, value):
        """Check if the value is positive"""
        return value > 0

    def is_valid_date(self, date_str):
        """Check if the string is a valid date (YYYY-MM-DD)"""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def is_valid_email(self, email):
        """Check if the email is valid"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def is_not_empty(self, value):
        """Check if the string is not empty"""
        return bool(value and value.strip())
