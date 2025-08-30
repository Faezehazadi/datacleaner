import pandas as pd

def clean_data(file_path, dropna=False, drop_columns=None, rename_columns=None, output=None):
    """
    Clean the CSV data based on user options.
    
    :param file_path: Path to input CSV file
    :param dropna: Remove rows with NaN values (bool)
    :param drop_columns: List of columns to drop
    :param rename_columns: Dictionary of columns to rename
    :param output: Path to save cleaned file (optional)
    :return: Cleaned pandas DataFrame
    """
    df = pd.read_csv(file_path)

    if dropna:
        df = df.dropna()

    if drop_columns:
        df = df.drop(columns=drop_columns)

    if rename_columns:
        df = df.rename(columns=rename_columns)

    if output:
        df.to_csv(output, index=False)

    return df
