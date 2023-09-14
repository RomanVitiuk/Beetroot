from csv import DictWriter
from typing import List

from PyPDF2 import PdfReader

from extractor_functions import (
    get_country,
    is_start_of_topic,
    split_names,
    split_location,
    union_names_location,
)


def create_csv_file() -> None:
    """
    Function create csv file if not exists.
    Return: None
    """
    fieldnames = [
            "names",
            "affiliation_name",
            "location",
            "session",
            "topic",
            "desc",
            # 'session',
            # 'topic',
            # 'desc',
            # 'location',
            # 'names',
            # "country",
        ]
    with open('topics_info.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def create_text_file_from_pdf(file_name: str) -> None:
    """
    Function create text file with topics from
    pdf file.
    Args: file_name
    Type args: str
    Return: None
    """
    data = PdfReader(file_name)
    with open("psoriasis_topics.txt", "w") as f:
        for x in data.pages[6:64]:
            f.write(x.extract_text())


def topics_list() -> List[str]:
    """
    Function create a list of topics from file.
    Return: list[str]
    """
    lst = []
    with open("psoriasis_topics.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            if i > 2:
                if is_start_of_topic(line):
                    lst.append("")
                    lst[-1] += line
                else:
                    lst[-1] += line
    return lst


def write_rows_to_csv(dct: dict) -> None:
    """
    Function append row to csv file.
    Return: None
    """
    fieldnames = [
            "names",
            "affiliation_name",
            "location",
            "session",
            "topic",
            "desc",
            # 'session',
            # 'topic',
            # 'desc',
            # 'location',
            # 'names',
            # "country",
        ]
    names_list = split_names(dct["names"])
    location_list = split_location(dct["affiliation_name"])
    name_loc_list = union_names_location(
        lst_name=names_list,
        lst_location=location_list
    )
    del dct["names"]
    del dct["affiliation_name"]
    with open("topics_info.csv", mode="a", encoding="utf-8", newline="") as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        for name, location in name_loc_list:
            country = get_country(location)
            dct["names"] = name
            dct["affiliation_name"] = location
            dct.update(country)
            writer.writerow(dct)
