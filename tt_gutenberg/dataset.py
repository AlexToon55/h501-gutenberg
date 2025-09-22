# reference: https://github.com/rfordatascience/tidytuesday/blob/main/data/2025/2025-06-03/readme.md

import pandas as pd

# Option 2: Read directly from GitHub and assign to an object

gutenberg_authors = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
gutenberg_languages = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')



# Return the dataframes as a dictionary
def load_gutenberg_data():
    return {
        'authors': gutenberg_authors,
        'languages': gutenberg_languages,
        'metadata': gutenberg_metadata,
        'subjects': gutenberg_subjects
    } 