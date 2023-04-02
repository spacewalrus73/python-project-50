from json import dumps


def json(diff):
    return dumps(diff, indent=4)
