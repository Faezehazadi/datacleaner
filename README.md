# DataCleaner
A simple Python package for cleaning CSV data.

## Features
- Remove NaN values
- Drop unnecessary columns
- Rename columns
- Save cleaned data to a new file

## Usage
```python
from datacleaner import clean_data

df = clean_data("data.csv", dropna=True, drop_columns=["col1"], rename_columns={"old":"new"}, output="cleaned.csv")
print(df.head())
