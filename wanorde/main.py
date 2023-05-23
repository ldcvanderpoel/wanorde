#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import operator
import sys

from datatypes import BasicConfig, Config, InfixesConfig, OtherConfig
from format import format_names
from name import Name, NameType
from util import (ensure_list, generate_configs, parse_json_config,
                  print_usernames, read_input_file)


def custom_config():
    # Change configuration to the desired output
    basic = BasicConfig(
        firstname_abbreviated=True, first_name_last=False, concatonate_character="."
    )

    infixes = InfixesConfig(
        concatonate_character="",
        concatonate_first_character=".",
        concatonate_last_character="",
        abbreviate=False,
        omit=False,
    )

    other = OtherConfig(strip_apostrophe=True, remove_marriage_name=True)

    return Config(basic, infixes, other)


def process_configs(configs: list[Config], names: list[Name]):
    for config in configs:
        format_names(names, config)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        metavar="FILE",
        nargs="?",
        help="Newline delimited list of names. If empty, stdin is used.",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        help="A suffix, such as @domain.nl",
        required=False,
        default="",
    )
    config_parser_group = parser.add_mutually_exclusive_group(required=True)

    config_parser_group.add_argument(
        "-c",
        "--config",
        help="Config file.",
        required=False,
        default="",
    )
    # Need to test
    # config_parser_group.add_argument(
    #     "-a",
    #     "--all",
    #     help="All possible configurations."
    # )
    # config_parser_group.add_argument(
    #     "-b",
    #     "--brute",
    #     help="Brute forces initials. Expects a list of shortened names, e.g. `b.alpha`.",
    #     required=False,
    #     default=""
    # )

    parser.add_argument(
        "--csv",
        help="CSV output containing, mapping username with original name.",
        required=False,
        action='store_true'
    )

    args = parser.parse_args()
    # args.config
    names = read_input_file(args.input)
    names = [Name(name) for name in names]

    sorted_names = sorted(names, key=operator.attrgetter("type"))

    configs = list()
    if args.config:
        configs = [parse_json_config(args.config)]
    else:
        configs = generate_configs()

    process_configs(configs, sorted_names)
    print_usernames(sorted_names, args.suffix, args.csv)


if __name__ == "__main__":
    main()
