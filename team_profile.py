import pandas as pd
import matplotlib.pyplot as plt


def load_data(team_stats_path, player_stats_path):
    df_team = pd.read_csv(team_stats_path, parse_dates=["gameDate"])
    df_player = pd.read_csv(player_stats_path, parse_dates=["gameDate"], low_memory=False)
    return df_team, df_player


def filter_team_season(df_team, df_player, team_name, season):
    start_year = int(season)
    end_year = start_year + 1
    start_date = f"{start_year}-10-01"
    end_date = f"{end_year}-07-01"

    df_team_season = df_team[
        (df_team["teamName"] == team_name) &
        (df_team["gameDate"] >= start_date) &
        (df_team["gameDate"] < end_date)
    ]

    df_player_season = df_player[
        (df_player["playerteamName"] == team_name) &
        (df_player["gameDate"] >= start_date) &
        (df_player["gameDate"] < end_date)
    ]

    return df_team_season, df_player_season


def show_team_summary(df_team, team_name):
    print(f"\n Résumé de l’équipe : {team_name}")
    games = len(df_team)
    wins = df_team["win"].sum()
    print(f"• Matchs joués : {games}")
    print(f"• Victoires : {int(wins)}")

    stats = df_team.select_dtypes(include="number").mean()
    
    desired = [
        "teamScore", "assists", "reboundsTotal", "turnovers", "foulsPersonal",
        "pointsFastBreak", "pointsFromTurnovers"
    ]
    present = [col for col in desired if col in stats.index]

    if present:
        print("\n Statistiques moyennes disponibles :")
        print(stats[present].round(2))
    else:
        print(" Aucune statistique moyenne disponible (vérifie les colonnes du fichier CSV).")

def show_team_players(df_player_season):
    """
    Affiche tous les joueurs de l’équipe avec leur moyenne de points,
    triés par ordre décroissant.
    """
    df_points = (df_player_season
                 .groupby("fullName")["points"]
                 .mean()
                 .sort_values(ascending=False)
                 .reset_index())

    print("\n Tous les joueurs de l’équipe par moyenne de points :\n")
    print(df_points.to_string(index=False))



def plot_wins_by_month(df_team, team_name):
    df_team = df_team.copy()
    df_team["month"] = df_team["gameDate"].dt.to_period("M").astype(str)
    monthly_wins = df_team.groupby("month")["win"].sum()

    plt.figure(figsize=(10, 4))
    plt.bar(monthly_wins.index, monthly_wins.values, color="mediumseagreen")
    plt.title(f" Victoires par mois — {team_name}")
    plt.xlabel("Mois")
    plt.ylabel("Nombre de victoires")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_team_score_progression(df_team, team_name):
    if "teamScore" not in df_team.columns:
        print("Aucune donnée 'teamScore' pour tracer l'évolution.")
        return

    df_sorted = df_team.sort_values("gameDate")
    plt.figure(figsize=(10, 4))
    plt.plot(df_sorted["gameDate"], df_sorted["teamScore"], marker='o', color="royalblue")
    plt.title(f" Évolution des scores — {team_name}")
    plt.xlabel("Date")
    plt.ylabel("Score d’équipe")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
