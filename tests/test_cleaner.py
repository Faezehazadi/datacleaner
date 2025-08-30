import pandas as pd
from datacleaner.cleaner import clean_data

def test_clean_data(tmp_path):
    data = {"A": [1, 2, None], "B": [4, 5, 6]}
    df = pd.DataFrame(data)
    file_path = tmp_path / "test.csv"
    df.to_csv(file_path, index=False)

    result = clean_data(file_path, dropna=True)
    assert result.shape[0] == 2
