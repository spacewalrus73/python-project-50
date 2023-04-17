import json
import yaml
from yaml.loader import SafeLoader


def get_content(path: str) -> dict:
    with open(path, 'r') as f:
        file = f.read()

    file_format = get_format(path)

    if file_format == 'json':
        return json.loads(file)
    elif file_format == 'yml':
        return yaml.load(file, Loader=SafeLoader)
    else:
        print("Programme stopped")


def get_format(filepath: str) -> str:

    if filepath.endswith('.json'):
        return 'json'
    elif filepath.endswith(('.yml', '.yaml')):
        return 'yml'
    else:
        print("Incorrect input file format. Use json or yml.")
