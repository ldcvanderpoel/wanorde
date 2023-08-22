# Wanorde

Different languages have different rules for constructing names, and therefore
require different tactics for constructing possible usernames from people names.

Username generators often rely on submitting specific username formats. However, this
often does not have sufficient expression power for dealing with more complex
name structures.

For example, these are some names one might encounter:
- Bob Jansen
- Bob van Jansen
- Bob van der Jansen
- Bob van 't Jansen
- Bob Jansen-Vries
- Jan-Willem Jansen

Supplying one format that covers each situation is difficult. Instead, we should define
consistent naming rules, and apply those to a list of names.

# Usage
```
usage: main.py [-h] [-i [FILE]] [-s SUFFIX] -c CONFIG

options:
  -h, --help            show this help message and exit
  -i [FILE], --input [FILE]
                        Newline delimited list of names. If empty, stdin is used.
  -s SUFFIX, --suffix SUFFIX
                        A suffix, such as @domain.nl
  -c CONFIG, --config CONFIG
                        Config file. See `examples/config.json`.
```


# Acknowledgments
Inspired by https://github.com/urbanadventurer/username-anarchy