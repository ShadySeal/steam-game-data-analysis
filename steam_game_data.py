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

# Games that are free
free_games = df[df['Required age'] == 0]

# Games that are not free
paid_games = df[df['Required age'] > 0]

# Display how many free and paid games there are
print("Number of free games:", len(free_games))
print("Number of paid games:", len(paid_games))

# Filter games with non-zero average playtime
played_games = df[df['Average playtime forever'] > 0]

# Display the number of such games
print("Number of games with playtime > 0:", len(played_games))

# Show the top 10 of them
print("Games with non-zero average playtime:")
print(played_games[['AppID', 'Average playtime forever']].head(10))