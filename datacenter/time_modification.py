import time


def format_duration(duration, time_format):
    return time.strftime(time_format, time.gmtime(duration))
