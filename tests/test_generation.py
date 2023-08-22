from wanorde import format, name, util

example_names = 'examples/names.txt'
example_config = 'examples/config.json'

def test_example_config():
    names = name.read_names(example_names)
    configs = util.parse_json_config([example_config])
    format.process_configs(configs, names)
    name.print_usernames(names, '@test.nl', False)

def test_all_configs():
    names = name.read_names(example_names)
    configs = util.generate_configs()
    format.process_configs(configs, names)
