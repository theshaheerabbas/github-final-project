import pandas as pd

# Assuming you have a dataframe named 'df'
df = pd.DataFrame({
    'column1': [1, 2, 3, 4, 5],
    'column2': ['a', 'b', 'c', 'd', 'e'],
    'column3': [10.5, 20.3, 15.8, 7.2, 12.9]
})

# Selecting multiple columns
selected_columns = df[['column1', 'column3']]

print(selected_columns)
