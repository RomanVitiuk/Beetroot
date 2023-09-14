from os import getcwd
from os.path import join, isfile

import pandas as pd

from extractor_functions import create_dict
from files_handlers import(
    create_csv_file,
    create_text_file_from_pdf,
    topics_list,
    write_rows_to_csv,
)
from time_speed_execution import time_speed


@time_speed
def main():
    if not isfile(join(getcwd(), "psoriasis_topics.txt")):
        create_text_file_from_pdf(
            file_name="Abstract Book from the 5th World Psoriasis and Psoriatic Arthritis Conference 2018.pdf"
        )
    lst = topics_list()
    if not isfile(join(getcwd(), "topics_info.csv")):
        create_csv_file()
    [write_rows_to_csv(dct=create_dict(text=text)) for text in lst]


if __name__ == "__main__":
    print("[+] Start parse pdf document!")
    main()
    print("[+] Successful created csv file --> topics_info.csv")
    df = pd.read_csv("topics_info.csv")
    rows, columns = df.shape
    print(f"[+] File topics_info.csv include: {rows} rows and {columns} columns")
    f_rows, f_columns = df.dropna().shape
    print(f"[+] File topics_info.csv without empty records include: {f_rows} rows and {f_columns} columns")
    df.to_excel("psoriasis_topics_info.xlsx", index=False)
    print("[+] Successful created ecxel file --> psoriasis_topics_info.xlsx")
    print("Ok")
