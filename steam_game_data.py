import kaggle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
df = pd.read_csv(file_path, header=0)

# --- Clean Data ---
df = df.dropna(subset=['Positive', 'Negative'])

# Filter free and paid games
free_games = df[df['Required age'] == 0]
paid_games = df[df['Required age'] > 0]

# --- FOREVER PLAYTIME ---
free_forever_hours = free_games['Average playtime forever'].mean() / 60
paid_forever_hours = paid_games['Average playtime forever'].mean() / 60
total_forever = free_forever_hours + paid_forever_hours
free_forever_percent = (free_forever_hours / total_forever) * 100 if total_forever > 0 else 0
paid_forever_percent = (paid_forever_hours / total_forever) * 100 if total_forever > 0 else 0

# --- 2 WEEKS PLAYTIME ---
free_2w_hours = free_games['Average playtime two weeks'].mean() / 60
paid_2w_hours = paid_games['Average playtime two weeks'].mean() / 60
total_2w = free_2w_hours + paid_2w_hours
free_2w_percent = (free_2w_hours / total_2w) * 100 if total_2w > 0 else 0
paid_2w_percent = (paid_2w_hours / total_2w) * 100 if total_2w > 0 else 0

# --- SCORES ---
free_score = free_games['Positive'] / (free_games['Positive'] + free_games['Negative'])
paid_score = paid_games['Positive'] / (paid_games['Positive'] + paid_games['Negative'])
free_avg_score = free_score.mean()
paid_avg_score = paid_score.mean()

# --- Plot all charts in a 2x2 grid ---
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
labels = ['Free Games', 'Paid Games']
colors = ['skyblue', 'lightcoral']
explode = (0.05, 0.05)

# Top left: Forever playtime pie
axs[0, 0].pie([free_forever_percent, paid_forever_percent],
              labels=labels, autopct='%1.1f%%', colors=colors,
              explode=explode, startangle=90)
axs[0, 0].set_title('Total Average Playtime (Forever)')

# Top right: 2 weeks playtime pie
axs[0, 1].pie([free_2w_percent, paid_2w_percent],
              labels=labels, autopct='%1.1f%%', colors=colors,
              explode=explode, startangle=90)
axs[0, 1].set_title('Average Playtime (Last 2 Weeks)')

# Bottom center (spanning both columns): Score comparison bar chart
axs[1, 0].bar(labels, [free_avg_score, paid_avg_score], color=colors)
axs[1, 0].set_ylim(0, 1)
axs[1, 0].set_ylabel('Average Score (Positive / Total Reviews)')
axs[1, 0].set_title('Average Review Score: Free vs Paid Games')
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

# Hide the unused subplot space on bottom right
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
