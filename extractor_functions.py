import re
from typing import Dict, Generator, List

from numpy import nan

from utils_regexp.regexp_patterns import (
    country_loc_pattern,
    desc_pattern,
    location_pattern,
    names_pattern,
    session_topic_pattern,
    split_location_pattern,
    topic_pattern,
)


def create_dict(text: str) -> Dict[str, str]:
    """
    Function forms dictionary from input text and return
    this dictionary.
    Args: text
    Type args: str
    Return: dict -> {str: str}
    """
    result = session_topic_pattern.search(string=text).groupdict()
    result.update(desc_pattern.search(string=text).groupdict())
    _, desc_names_loc = text.split(result["session"] + result["topic"])
    names_location, _ = desc_names_loc.split(result["desc"])
    if location_pattern.search(string=names_location):
        result.update(
            location_pattern.search(string=names_location).groupdict()
        )
        names, _ = names_location.split(result["affiliation_name"])
        result.update({"names": names.replace("\n", "")})
        result["affiliation_name"] = result.get("affiliation_name").replace("\n", "")
    else:
        result.update({"affiliation_name": ""})
        result.update({"names": names_location.replace("\n", "")})
    return result


def is_start_of_topic(line: str) -> bool:
    """
    Function check if string match with pattern: < P000\\n >
    and return bool (True or False).
    Where P is on start of line and 000 any three digits.
    Args: line
    Type args: str
    Return: bool
    """
    if re.search(pattern=topic_pattern, string=line):
        return True
    return False


def get_country(line: str) -> Dict[str, str]:
    """
    Function create and return dictionary from input line
    if match with pattern.
    Args: line
    Type args: str
    Return: dict -> {'str': 'str'}
    """
    if country_loc_pattern.search(line):
        return country_loc_pattern.search(line).groupdict()
    return {"location": ""}


def split_names(line: str) -> List[str]:
    """
    Function replace newline symbol on '' (empty string)
    and create list of names from line. If names match
    with pattern than this list sorted by last digit.
    Args: line
    Type args: string
    Return: list[str]
    """
    lst = line.replace("\n", '').split(', ')
    if lst[0][-1] in "1234567890":
        lst.sort(key=lambda x: x[-1])
    return lst


def split_location(line: str) -> List[str]:
    """
    Function create list of location from line. If
    location match with pattern than this list
    sorted by last digit.
    Args: line
    Type args: str
    Return: list[str]
    """
    if line == "" or line is nan:
        return [""]
    if line[-1] == ",":
        line = line[:-1]
    lst = split_location_pattern.split(line)
    lst = list(filter(lambda x: x != '', lst))
    if lst[0][0] in "1234567890":
        lst.sort(key=lambda x: x[0])
    return lst


def union_names_location(
    lst_name: list, lst_location: list
) -> Generator[tuple, None, None]:
    """
    Function take two list on input and forms
    a generator of (name, location) pairs.
    Args: lst_name, lst_location
    Type args: list[str], list[str]
    Return: generator -> tuple(str, str)
    """
    if len(lst_location) == 1:
        return ((name, lst_location[0]) for name in lst_name)
    else:
        return (
            (name, loc) if name[-1] == loc[0] else (name, loc)
            for loc in lst_location
            for name in lst_name
        )
