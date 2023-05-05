from dataclasses import dataclass
from enum import IntEnum, auto


class NameType(IntEnum):
    Basic = auto()
    Infixes = auto()
    Invalid = auto()


@dataclass
class BasicConfig:
    """First name abbreviated to a single letter, or full?"""

    # Basic options, for basic 'First Last' names.
    firstname_abbreviated: bool

    # Character to concatonate with. Can be empty.
    first_name_last: bool

    # First name first?
    concatonate_character: str
    #  def __init__(self, firstname_abbreviated: bool, first_name_first: bool, concatonate_character: str):
    #      self.first


@dataclass
class InfixesConfig:
    """Configuration options for 'infixes'."""

    """
    How to concatonate multiple chunks of infixes.
    E.g. van.der vs vander
    """
    concatonate_character: str

    # How to concatonate first name to infixes.
    # E.g. f.vander vd fvander
    concatonate_first_character: str

    # How to concatonate last name to infixes.
    # E.g. vander.last vs vanderlast
    concatonate_last_character: str

    # Whether to abbreviate the infixes.
    # E.g. v.d or vd
    abbreviate: bool

    # Whether to omit the infixes.
    # E.g. First van der Last becomes firstlast
    omit: bool


@dataclass
class OtherConfig:
    # Remove apostrophe.
    # laurens.van.'t.poel -> laurens.van.t.poel
    strip_apostrophe: bool

    # Remove the extra name received after marriage, e.g.
    # laurens.van.der.poel-slim -> laurens.van.der.poel
    remove_marriage_name: bool


@dataclass
class Config:
    basic: BasicConfig
    infixes: InfixesConfig
    other: OtherConfig
