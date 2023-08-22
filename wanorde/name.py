from wanorde.datatypes import NameType
from wanorde.util import ensure_list, ensure_string, read_input_file


class Name:
    """
    Assumes names are supplied with chunks delimited by spaces.
    E.g. 'Jan van der Jansen'
    """

    lowercase = True
    strip_characters = ["'"]
    usernames: set[str]

    def __init__(self, name: str):
        self.original = name

        self.reset()

        self.type: NameType = self._get_type()

        self.usernames: set[str] = set()

    def reset(self):
        """Resets modifications to chunks."""
        self.name = self.original
        self._preprocess()

        self.chunks = self.name.split(" ")
        self.first = ensure_list(self.chunks[0])
        self.middle = ensure_list(self.chunks[1:-1])
        self.last = ensure_list(self.chunks[-1])

    def _get_type(self):
        if len(self.chunks) == 1:
            return NameType.Invalid
            #  raise ValueError('Name has no first or last name: %s' % self.name)
        elif len(self.chunks) == 2:
            return NameType.Basic
        return NameType.Infixes

    def _preprocess(self):
        self._strip()
        self._tolower()

    def _strip(self):
        for character in self.strip_characters:
            self.name = self.name.strip(character)

    def _tolower(self):
        if self.lowercase:
            self.name = self.name.lower()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    @property
    def info(self) -> str:
        return f"{self.original}, {self.name}, {self.type}"



def print_usernames(names: list[Name], suffix: str, csv = False) -> None:
    all_usernames = []
    if csv:
        print('username,first name,infix,last name')

    for name in names:
        usernames = [f"{username}{suffix}" for username in name.usernames]
        all_usernames += usernames
        
        if csv:
            for username in usernames:
                print(f'{username},{ensure_string(name.first)},{ensure_string(name.middle)},{ensure_string(name.last)}')


    if not csv:
        print("\n".join(sorted(set(all_usernames))))

def read_names(input_file: str) -> list[Name]:
    """Read names into sorted list of Name objects."""
    names = read_input_file(input_file)
    names = [Name(name) for name in names]

    return sorted(names, key=str)
 