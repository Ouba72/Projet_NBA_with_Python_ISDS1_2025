"""Ce module permet d’afficher un classement de joueurs NBA selon une statistique choisie."""

from rattrapage.utils import (load_player_stats, filter_data, display_leaderboard)

def main():

    """Affiche une fiche descriptive d’équipe NBA en fonction de la saison et du nom."""
    print(" Bienvenue dans l’outil Leaderboard NBA !")

    category = category = input(
      ">> Quelle statistique veux-tu analyser ? (ex: points, assists, reboundsTotal, etc.) : "
    ).strip()

    season = input(">> Quelle saison t'intéresse ? (ex: 2023 pour la saison 2023-2024) :").strip()
    game_type = input(">> Quel type de match ? (Regular Season ou Playoffs): ").strip()
    top_n_input = input(">> Combien de joueurs veux-tu afficher ? (ex: 10): ").strip()
    try:
        top_n = int(top_n_input)
    except ValueError:
        print("Nombre invalide. Par défaut, on affichera les 10 meilleurs.")
        top_n = 10

    df = load_player_stats("PlayerStatistics.csv")
    df = filter_data(df, season=season, game_type=game_type)
    display_leaderboard(df, category=category, top_n=top_n)

if __name__ == "__main__":
    main()
