import re

def detect_date_format(date_str):
    patterns = {
        'YYYY-MM-DD': r'\d{4}-\d{2}-\d{2}',
        'DD-MM-YYYY': r'\d{2}-\d{2}-\d{4}',
        # Add more patterns as needed
    }

    for format_name, pattern in patterns.items():
        if re.match(pattern, date_str):
            return format_name

    return "Unknown format"
