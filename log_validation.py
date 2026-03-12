def normalize_level(level: str) -> str:
    level = level.strip()
    level = level.upper()
    return level


def validate_and_normalize(parsed):

    timestamp, level, service, message = parsed

    level = normalize_level(level)

    allowed = {"INFO", "WARN", "ERROR"}

    service = service.strip()
    message = message.strip()

    if level not in allowed:
        return None

    if service == "" or message == "":
        return None

    return (timestamp, level, service, message)
