# Get the data from the gutenberg project
import pandas as pd


def load_authors():
   # bring the data in as a dataframe
   url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
   return pd.read_csv(url)


def load_languages():
   url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
   return pd.read_csv(url)


def load_metadata():
   url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
   return pd.read_csv(url)