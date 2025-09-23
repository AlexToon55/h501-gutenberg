# Imports
import pandas as pd
from .dataset import load_authors, load_metadata # Don't need languages here as metadata has language info required. 

# Function to list authors by number of languages their works have been translated into.
def list_authors(by_languages=True, alias=True):
    #Build a small dataframe of author_id and number of languages.
    meta = load_metadata()
    authors = load_authors()[['gutenberg_author_id', 'author', 'alias' ]]


    # keep only the columns we need
    pairs = meta[['gutenberg_author_id', 'language']].drop_duplicates()


    # count how many languages per author
    counts = ( 
        pairs.groupby('gutenberg_author_id')
                .size()
                .reset_index(name='language_count')
        )


    # attach author + alias
    df = counts.merge(authors, on='gutenberg_author_id', how='left')
    df = df.sort_values('language_count', ascending=False, kind='mergesort')

    # pick the columns to return
    name_col = 'alias' if alias else 'author'
    col = df[name_col]
    mask = col.notna() & (col.str.strip() != '') & (col.str.upper() != 'NA')
    return col[mask].tolist()

