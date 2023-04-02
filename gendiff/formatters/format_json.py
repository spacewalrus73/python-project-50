from json import dumps


def json(diff):
    result = ''
    for item in diff:
        result = result + dumps(item, indent=4) + '\n'
    return result[:-1]
