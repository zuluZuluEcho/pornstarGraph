

def is_nutted(filename: str) -> str:
    """
    Receive a filename, and return a nutted has been busted on it.
    """
    if ("qw49" in filename.lower()) or ("al gebost" in filename.lower()):
        return "Yes"
    elif "xw49" in filename.lower():
        return "Maybe"
    else:
        return "No"
