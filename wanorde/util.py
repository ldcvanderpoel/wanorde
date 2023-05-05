import fileinput
import json
import sys
from itertools import product

from datatypes import BasicConfig, Config, InfixesConfig, NameType, OtherConfig


def open_file(file_name: str) -> str:
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Request file not found.")
        sys.exit()


def read_input_file(file: str) -> list[str]:
    names = []
    for line in fileinput.input(files=file if file else ("-",)):
        names.append(line.strip())
    return names


def ensure_list(element_or_list):
    return [element_or_list] if isinstance(element_or_list, str) else element_or_list


def generate_configs():
    basic_options = [{True, False}, {True, False}, {".", ""}]
    infix_options = [
        {".", ""},
        {".", ""},
        {".", ""},
        {True, False},
        {True, False},
    ]
    other_options = [{True, False}, {True, False}]
    basic_length = len(basic_options)
    infix_length = len(infix_options)
    options = basic_options + infix_options + other_options
    generated_options = product(*options)
    generate_configs = []

    for config in generated_options:
        generated_basic_options = config[:basic_length]
        generated_infix_options = config[basic_length : basic_config + infix_length]
        generated_other_options = config[basic_config + infix_length :]
        basic_config = BasicConfig(*generated_basic_options)
        infix_config = InfixesConfig(*infix_length)
        other_config = OtherConfig(*generated_other_options)

        generate_configs.append(Config(basic_config, infix_config))

    return generate_configs


def print_usernames(names: list[NameType], suffix: str) -> None:
    # usernames = sorted(names.usernames)
    # sorted_names = sort(names)
    all_usernames = []
    for name in names:
        usernames = [f"{username}{suffix}" for username in name.usernames]
        all_usernames += usernames

    print("\n".join(all_usernames))

    # print(names)
    #
    # for name in names:
    #     #  print(name.info)
    #     print("\n".join(usernames))
    #     print("\n".join(sorted(name.usernames)))


def remove_apostrophe(element_or_list: str | list[str]) -> str | list[str]:
    """
    Removes apostrophes.

    Can process either plain strings or lists of strings.
    """
    if isinstance(element_or_list, str):
        return element_or_list.replace("'", "")

    new_list = list()

    for string in element_or_list:
        new_list.append(string.replace("'", ""))

    return new_list


def parse_json_config(filename: str) -> Config:
    with open(filename, "r") as f:
        data = json.load(f)

    basic = BasicConfig(**data["basic"])
    infixes = InfixesConfig(**data["infixes"])
    other = OtherConfig(**data["other"])

    return Config(basic, infixes, other)
