import polars as pl
from file import is_nutted
from collections import Counter
from pornstar import capitalize_name


def give_top_n(values_per_entity: dict[str, int | float], n: int = 10) -> dict[str, int | float]:
    """
    Returns the top N entities from big to small.
    """
    counter: Counter = Counter(values_per_entity)

    top_n_entities: dict[str, int | float] = {}

    for entity, value in counter.most_common():
        if len(top_n_entities) < n:
            top_n_entities[entity] = value
        elif value == list(top_n_entities.values())[-1]:
            top_n_entities[entity] = value
        else:
            break

    return top_n_entities


def give_nut_count_pornstar(pornstars: set[str], filenames: pl.Series, certain_nuts: bool) -> dict[str, int]:
    """
    Returns the amount of times there was nutted on a certain pornstar — for every pornstar — as a dictionary.
    """
    filenames_lower_case: list[str] = [filename.lower() for filename in filenames]
    nut_count_per_pornstar: dict[str, int] = {pornstar: 0 for pornstar in pornstars}

    if certain_nuts:
        for filename in filenames_lower_case:
            for pornstar in pornstars:
                if (pornstar in filename) and (is_nutted(filename) == "Yes"):
                    nut_count_per_pornstar[pornstar] += 1
    else:
        for filename in filenames_lower_case:
            for pornstar in pornstars:
                if (pornstar in filename) and ((is_nutted(filename) == "Yes") or (is_nutted(filename) == "Maybe")):
                    nut_count_per_pornstar[pornstar] += 1

    return {capitalize_name(pornstar): nut_count for pornstar, nut_count in nut_count_per_pornstar.items()}
