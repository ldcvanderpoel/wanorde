#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from wanorde.format import process_configs
from wanorde.name import print_usernames, read_names
from wanorde.util import generate_configs, parse_json_config


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
    # config_parser_group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument(
        "-c",
        "--config",
        help="Config file(s). If no config file(s) are supplied, all possible configurations are generated.",
        required=False,
        nargs='*',
        default="",
    )

    parser.add_argument(
        "--csv",
        help="CSV output containing, mapping username with original name.",
        required=False,
        action='store_true'
    )

    args = parser.parse_args()

    names = read_names(args.input)
    
    configs = list()
    if args.config:
        configs = parse_json_config(args.config)
    else:
        configs = generate_configs()

    process_configs(configs, names)
    print_usernames(names, args.suffix, args.csv)

if __name__ == "__main__":
    main()
