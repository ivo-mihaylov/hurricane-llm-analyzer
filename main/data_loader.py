import pandas as pd
from main.data import data

"""
Provides a utility function to convert the raw data into a pandas DataFrame.
"""


def load_dataset() -> pd.DataFrame:

    """
    Converts the dictionary from data.py into a pandas DataFrame.

    Returns:
        pd.DataFrame: The structured dataset.
    """

    df = pd.DataFrame(data)
    return df