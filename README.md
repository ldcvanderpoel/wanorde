# Wanorde

Different languages have different rules for constructing names, and therefore require different tactics for constructing possible usernames from people names.

Username generators often rely on submitting specific username formats. However, this often does not have sufficient expression power for dealing with more complex name structures.

For example, these are some names one might encounter:
- Jan Jansen
- Jan van Jansen
- Jan van der Jansen
- Jan van 't Jansen
- Jan Jansen-Visser
- Jan-Willem Jansen

Supplying one format that covers each situation is difficult. Instead, we should define consistent naming rules, and apply those to a list of names.

## Known issues

- It's not always clear what part of a name is an first name, an infix, or a last name. Currently, it is assumed that last names consists of single words, which is not always true. However, it will do for now.
- It is sometimes not possible to distinguish married names from complex infixes or last names.

# Usage
For an example of a config file, please see `examples/config.json`.

```
usage: main.py [-h] [-i [FILE]] [-s SUFFIX] -c [CONFIG ...] [--csv]

options:
  -h, --help            show this help message and exit
  -i [FILE], --input [FILE]
                        Newline delimited list of names. If empty, stdin is used.
  -s SUFFIX, --suffix SUFFIX
                        A suffix, such as @domain.nl
  -c [CONFIG ...], --config [CONFIG ...]
                        Config file(s). If no config file(s) are supplied, all possible configurations are generated.
  --csv                 CSV output containing, mapping username with original name.

```


# Acknowledgments
Inspired by https://github.com/urbanadventurer/username-anarchy