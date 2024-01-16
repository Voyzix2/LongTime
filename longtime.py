import time


def sleep(duration, unit='seconds'):
    if unit == 'seconds':
        time.sleep(duration)
    elif unit == 'minutes':
        time.sleep(duration * 60)
    elif unit == 'hours':
        time.sleep(duration * 60 * 60)
    elif unit == 'days':
        time.sleep(duration * 24 * 60 * 60)
    elif unit == 'months':
        time.sleep(duration * 30 * 24 * 60 * 60)
    elif unit == 'years':
        time.sleep(duration * 365 * 24 * 60 * 60)
    else:
        raise ValueError("Invalid time unit. Supported units: seconds, minutes, hours, days, months, years")


def repeat(repetitions, duration, unit='seconds'):
    for _ in range(repetitions):
        sleep(duration, unit)
