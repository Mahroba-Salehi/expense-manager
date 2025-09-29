from datetime import datetime

class Utils:
    def format_currency(self, amount):
        """Format amount as 1,000.00"""
        return "{:,.2f}".format(amount)

    def str_to_date(self, date_str):
        """Convert a string to datetime"""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def calculate_total(self, records):
        """Calculate total from a list of records with 'amount' attribute"""
        return sum(r.amount for r in records)

    def sort_records_by_date(self, records):
        """Sort a list of records by date"""
        return sorted(records, key=lambda r: self.str_to_date(r.date))

    def filter_records_by_month(self, records, month, year):
        """Filter records by month and year"""
        filtered = []
        for r in records:
            date = self.str_to_date(r.date)
            if date.year == year and date.month == month:
                filtered.append(r)
        return filtered
