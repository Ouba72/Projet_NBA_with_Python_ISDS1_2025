"""Module utils contenant des fonctions utiles pour l'analyse des statistiques NBA."""
import pandas as pd

def load_player_stats(filepath):
    """Charge un fichier CSV et retourne un DataFrame pandas."""
    return pd.read_csv(filepath, parse_dates=["gameDate"])

def filter_data(df, season=None, game_type=None):
    if season:
        start, end = int(season), int(season) + 1
        df = df[(df["gameDate"] >= f"{start}-10-01") & (df["gameDate"] < f"{end}-07-01")]
    if game_type:
        df = df[df["gameType"] == game_type]
    return df

def compute_leaderboard(df, category="points", top_n=10):
    return (df.groupby("fullName")[category]
              .mean()
              .sort_values(ascending=False)
              .head(top_n)
              .reset_index())

def display_leaderboard(df, category="points", top_n=10):
    leaderboard = compute_leaderboard(df, category, top_n)
    print(f"\n Leaderboard — {category.capitalize()} (Top {top_n})")
    print(leaderboard.to_string(index=False))
