from variabele import constants
import polars as pl


def read_pornstars() -> set[str]:
    """
    Reads the name of each pornstar — line for line.
    """
    pornstars: set[str] = set()

    with open(constants.PATH_PORNSTAR_FILE, 'r', encoding="utf-8") as file:
        content_pornstar_file: str = file.read()

        for pornstar in content_pornstar_file.splitlines():
            pornstars.add(pornstar.lower())

    return pornstars


def prepare_for_cpp(filenames: pl.Series) -> None:
    """
    Prepares the data for the C++ programme.
    """
    with (open(constants.PATH_FILENAME_FOR_CPP, 'w', encoding="utf-8") as file):
        for filename in filenames:
            if not (("onbekend" in filename.lower()) and not ('&' in filename)):
                adjusted_filename: str = filename.replace('+', ' ').replace('-', ' ').replace('.', ' ').replace("  ", ' ').lower()
                file.write(f"{adjusted_filename}\n")


def read_frequency_per_pornstar() -> dict[str, int]:
    """
    Reads the result of the C++ programme — to fetch the frequency of each pornstar.
    """
    with open(constants.PATH_FILE_FREQUENCY_PER_PORNSTAR, 'r', encoding="utf-8") as bestand:
        frequency_per_pornstar: list[str] = bestand.read().splitlines()

    frequency_per_pornstar_: dict[str, int] = {}

    for frequency_and_pornstar_ in frequency_per_pornstar:
        values: list[str] = frequency_and_pornstar_.split(',')
        pornstar: str = values[0]
        frequency_pornstar: int = int(values[1])

        frequency_per_pornstar_[pornstar] = frequency_pornstar

    return frequency_per_pornstar_


def read_frequency_per_pornstar_pair() -> dict[tuple[str, str], int]:
    """
    Reads the result of the C++ programme — to fetch the frequency of each pornstar pair.
    """
    with open(constants.PATH_FILE_FREQUENCY_PER_PORNSTAR_PAIR, 'r', encoding="utf-8") as file:
        frequenties_per_pornstar_pair: list[str] = file.read().splitlines()

    frequenties_per_pornstar_pair_: dict[tuple[str, str], int] = {}

    for frequency_pair in frequenties_per_pornstar_pair:
        values: list[str] = frequency_pair.split(',')
        pornstar1: str = values[0]
        pornstar2: str = values[1]
        frequency_per_pair: int = int(values[2])

        frequenties_per_pornstar_pair_[(pornstar1, pornstar2)] = frequency_per_pair

    return frequenties_per_pornstar_pair_
