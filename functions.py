import re
from typing import Iterable, Optional, Iterator, Any, Callable


def read_file(filename: str) -> Iterator[str]:
    with open(filename) as file:
        for line in file:
            yield line


def filter_query(value: str, data: Iterator[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterator[str]) -> Iterator[str]:
    return map(lambda x: x.split()[int(value)], data)


def unique_query(data: Iterator[str], *args: Any, **kwargs: Any) -> set[str]:
    return set(data)


def sort_query(value: str, data: Iterator[str]) -> list[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterator[str]) -> list[str]:
    limit = int(value)
    return list(data)[:limit]


def regex_query(value: str, data: Iterator[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)


CMDS: dict[str, Callable] = {
    "filter": filter_query,
    "unique": unique_query,
    "map": map_query,
    "limit": limit_query,
    "sort": sort_query,
    "regex": regex_query,
}


def execute(value: str, cmd: str, filename: str,
            data: Optional[Iterator[str]]) -> list[str]:
    if data is None:
        prepared_data: Iterator[str] = read_file(filename)
    else:
        prepared_data = data

    return list(CMDS[cmd](value=value, data=prepared_data))
