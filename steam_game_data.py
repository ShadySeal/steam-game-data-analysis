import kaggle
import pandas as pd  # pandas is used for handling tabular datasets (dataframes) and performing operations such as reading CSV files
import numpy as np  # numpy is used for numerical computations such as working with arrays and applying mathematical operations
import os

# Only download if file doesn't already exist
if not os.path.exists("games.csv"):
    print("File doesn't exist.")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files("fronkongames/steam-games-dataset", path='.', unzip=True)
else:
    print("File exists.")

file_path = "games.csv"

# Read the dataset into a pandas dataframe
df = pd.read_csv(file_path, header=0)  # header=0 means the first row in the CSV is used as column names

# Display the first few rows of the dataframe to confirm the data has been loaded correctly
print("Dataset Preview:")  # Print a label for context
print(df.head(5))  # Display the first 5 rows of the dataset