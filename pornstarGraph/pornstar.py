

def capitalize_name(name: str) -> str:
    """
    Correctly capitalizes a name.

    >>> capitalize_name("jan bootjongen")
    'Jan Bootjongen'
    >>> capitalize_name("samuel")
    'Samuel'
    >>> capitalize_name("marty mcfly")
    'Marty Mcfly'
    """
    name_capitalized: list[str] = [name.capitalize() for name in name.split(' ')]
    name_capitalized_: str = ' '.join(name_capitalized)

    return name_capitalized_
