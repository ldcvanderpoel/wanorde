import re

from datatypes import Config, NameType
from name import Name
from util import ensure_list, remove_apostrophe


def format_names(names: list[Name], config: Config):
    formatter = Format(config)

    for name in names:
        username = formatter.format(name)
        name.usernames.add(username)
        name.reset()


class Format:
    def __init__(self, config):
        self.config = config

    def format(self, name: NameType):
        self._preprocess(name)

        if name.type == NameType.Basic:
            return self._basic(name)
        elif name.type == NameType.Infixes:
            return self._infix(name)
        elif name.type == NameType.Invalid:
            return "INVALID"
        else:
            raise ValueError("Unknown nametype in formatter.")

    def _basic(self, name: Name):
        config = self.config

        fullname = ensure_list(ensure_list(name.first) + ensure_list(name.last))

        return f"{config.basic.concatonate_character}".join(fullname)

    def _infix(self, name: Name):
        config = self.config

        if config.infixes.omit:
            name.middle = []

        if config.infixes.abbreviate:
            for element in name.middle:
                element = element[0]

        if name.middle:
            fullname_part = f"{config.infixes.concatonate_character}".join(
                ensure_list(name.middle)
            )

            fullname_part = f"{config.infixes.concatonate_first_character}".join(
                ensure_list(ensure_list(name.first) + ensure_list(fullname_part))
            )
        else:
            fullname_part = name.first

        fullname = f"{config.infixes.concatonate_last_character}".join(
            ensure_list(ensure_list(fullname_part) + ensure_list(name.last))
        )
        return fullname

    def _preprocess(self, name: Name):
        config = self.config

        if config.other.strip_apostrophe:
            name.first = remove_apostrophe(name.first)
            name.middle = remove_apostrophe(name.middle)
            name.last = remove_apostrophe(name.last)

        if config.basic.firstname_abbreviated:
            name.first = name.first[0]

        if config.other.remove_marriage_name:
            cutoff = " ".join(ensure_list(name.middle) + ensure_list(name.last))
            cutoff = re.sub(r"-.*", "", cutoff)
            cutoff = cutoff.split(" ")
            name.middle = cutoff[:-1]
            name.last = cutoff[-1]

        # laurens.van.der.poel -> van.der.poel.laurens
        if config.basic.first_name_last:
            name.first, name.middle, name.last = name.middle, name.last, name.first
