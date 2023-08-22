# from util import (ensure_list, generate_configs, parse_json_config,
#                   print_usernames, process_configs, read_input_file,
#                   read_names)

from wanorde import name, util


def test_read_names():
    filename = 'examples/names.txt'
    names = name.read_names(filename)
    assert len(names) == 8


def test_generate_configs():
    """ 
    When adding new config options, please update the assertion below to match
    the number of newly generated configs.
    """
    configs = util.generate_configs()

    assert len(configs) == 1024

def test_parse_json_config():
    filename1 = 'examples/config.json'
    filename2 = 'examples/config.json'
    configs = util.parse_json_config([filename1,filename2])
