from datatypes import BasicConfig, InfixesConfig, NameType


class Name:
    """
    Assumes names are supplied with chunks delimited by spaces.
    E.g. 'First van der Last'
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
        self.first = self.chunks[0]
        self.middle = self.chunks[1:-1]
        self.last = self.chunks[-1]

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
