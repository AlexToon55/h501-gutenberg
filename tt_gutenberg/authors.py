# Imports
import pandas as pd
from .dataset import load_authors, load_languages, load_metadata


def _languages_per_author():
    """Build a small dataframe of author_id and number of languages."""
authors = load.authors()