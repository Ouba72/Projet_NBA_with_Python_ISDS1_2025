"""Module principal pour afficher la fiche descriptive d’une équipe NBA par saison."""
import pandas as pd

from rattrapage.team_profile import (
    load_data, filter_team_season, show_team_summary,
    show_team_players, plot_wins_by_month, plot_team_score_progression
)

df = pd.read_csv('TeamStatistics.csv')

def main():
    """Affiche une fiche descriptive d’une équipe NBA pour une saison donnée."""
    print(" Fiche descriptive d’une équipe NBA")
    teams = sorted(df["teamName"].unique())
    print("\n Équipes disponibles :")
    for team in teams:
        print(f"• {team}")

    team = input("Nom de l’équipe (ex: Nuggets) : ").strip()
    season = input("Saison (ex: 2024 pour la saison 2024–25) : ").strip()

    df_team, df_player = load_data("TeamStatistics.csv", "PlayerStatistics.csv")

    df_team_season, df_player_season = filter_team_season(df_team, df_player, team, season)

    if df_team_season.empty:
        print("\n Aucune donnée trouvée pour cette équipe et cette saison.")
        return

    show_team_summary(df_team_season, team)
    show_team_players(df_player_season)
    plot_wins_by_month(df_team_season, team)
    plot_team_score_progression(df_team_season, team)

if __name__ == "__main__":
    main()
