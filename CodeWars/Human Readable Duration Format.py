def format_duration(seconds):
    """dirty solution .ignore"""
    readable_str = ""
    years = 0
    days = 0
    hours = 0
    minutes = 0
    secs = 0
    while True:
        if seconds >= 31536000:
            seconds -= 31536000
            years += 1
        elif seconds >= 86400:
            seconds -= 86400
            days += 1
        elif seconds >= 3600:
            seconds -= 3600
            hours += 1
        elif seconds >= 60:
            seconds -= 60
            minutes += 1
        else:
            secs = seconds
            break
    if years == 1:
        readable_str += f"{years} year"
    elif years > 1:
        readable_str += f"{years} years"
    if days == 1:
        readable_str += f"{days} day"
    elif days > 1:
        readable_str += f"{days} days"
    if days > 1:
        if hours >= 1:
            readable_str += ", "
        elif minutes >= 1:
            readable_str += " and "
    if hours == 1:
        readable_str += f"{hours} hour"
    elif hours > 1:
        readable_str += f"{hours} hours"
    if hours > 1:
        if seconds >= 1:
            readable_str += ", "
        elif minutes >= 1:
            readable_str += " and "
    if minutes == 1:
        readable_str += f"{minutes} minute"
    elif minutes > 1:
        readable_str += f"{minutes} minutes"
    if secs == 1:
        readable_str += f"{secs} second"
    elif secs > 1:
        if minutes >= 1:
            readable_str += " and "
        elif hours >= 1:
            readable_str += " and "
        elif days >= 1:
            readable_str += " and "
        readable_str += f"{secs} seconds"
    print(readable_str)


for i in range(10):
    format_duration(i*3000)
