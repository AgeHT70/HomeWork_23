from typing import Iterable, Optional


def read_file(filename: str):
    with open(filename) as file:
        for line in file:
            yield line


def filter_query(value, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def map_query(value, data):
    return map(lambda x: x.split()[int(value)], data)


def unique_query(data, *args, **kwargs):
    return set(data)


def sort_query(value, data):
    reverse = value == 'asc'
    return sorted(data, reverse=reverse)


def limit_query(value, data):
    limit = int(value)
    return list(data)[:limit]


CMDS = {
    "filter": filter_query,
    "unique": unique_query,
    "map": map_query,
    "limit": limit_query,
    "sort": sort_query,
}


def execute(value: str, cmd: str, filename: str, data: Optional[str]):
    if data is None:
        prepared_data = read_file(filename)
    else:
        prepared_data = data

    return list(CMDS[cmd](value=value, data=prepared_data))

