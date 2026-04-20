# Projet Rattrapage NBA - ISUP 2025

Analyse de données NBA avec prédiction de salaire par régression linéaire.

**Contexte** : Projet de rattrapage pour le cours de Python ISUP 2025. L'objectif est d'implémenter une régression linéaire sans utiliser sklearn/statsmodels et de créer 3 fonctionnalités d'analyse NBA.

## Installation

```bash
pip install -e .
```

## Utilisation

### Classement des joueurs
```bash
nba-leaderboard --stat points --season 2024 --top 10
nba-leaderboard --stat assists --season 2024 --type "Regular Season"
```

### Analyse d'équipe
```bash
nba-team-summary --team "Lakers" --season 2024
nba-team-summary --team "Warriors" --season 2023
```

### Prédiction de salaire
```bash
nba-predict-salary
```

## Données

Le projet utilise 4 fichiers CSV dans le dossier `data/` :
- `Players.csv` - Informations des joueurs (6,532 joueurs)
- `PlayerStatistics.csv` - Stats par match (504,985 entrées, 1946-2025)
- `TeamStatistics.csv` - Stats d'équipes par saison
- `Salaries.csv` - Salaires des joueurs (1,128 entrées)

**Note importante** : La saison NBA va d'octobre à juillet de l'année suivante. Le code extrait automatiquement la saison à partir de la date des matchs (ex: un match en novembre 2023 = saison 2023).

## Implémentation OLS

J'ai implémenté la régression linéaire à la main dans `src/rattrapage/ols.py` :
- **Formule mathématique** : β̂ = (X^T X)^(-1) X^T y
- **Pas d'utilisation** de sklearn ou statsmodels (contrainte du projet)
- **Méthodes requises** : fit(), predict(), get_coeffs(), determination_coefficient()

**Variables utilisées pour prédire le salaire** :
- Points par match (moyenne)
- Passes par match (moyenne) 
- Rebonds totaux par match (moyenne)


## Fonctionnalités détaillées

### 1. Leaderboard
- Calcule la moyenne des stats par joueur sur une saison
- Trie par ordre décroissant
- Gère les saisons et types de jeux (Regular Season/Playoffs)

### 2. Résumé d'équipe
- Statistiques offensives et défensives
- Bilan victoires/défaites
- Moyennes sur toute la saison

### 3. Prédiction de salaire
- Normalise les données (moyenne=0, écart-type=1)
- Entraîne le modèle OLS sur les données historiques
- Prédit le salaire pour un profil donné

## Tests

```bash
pytest tests/
```

23 tests au total qui couvrent :
- **Classe OLS** (14 tests) : formule mathématique, cas limites
- **Résumé d'équipe** (3 tests) : calculs de stats, gestion erreurs
- **Leaderboard** (3 tests) : tri, filtrage, affichage
- **Intégration** (3 tests) : fonctionnement avec vraies données

## Structure

```
├── data/                    # Fichiers CSV NBA
├── src/rattrapage/          # Code source
│   ├── ols.py              # Régression linéaire (classe principale)
│   ├── leaderboard.py      # Classements joueurs
│   ├── team_summary.py     # Résumés d'équipe
│   ├── predict_salary.py   # Prédiction salaire
│   └── utils.py            # Fonctions utilitaires (chargement CSV, etc.)
├── tests/                   # Tests unitaires
└── setup.py                # Configuration package
```

## Problèmes rencontrés et solutions

1. **Noms d'équipes** : Au début j'utilisais "Los Angeles Lakers" mais dans les données c'est juste "Lakers"
2. **Types de jeux** : Les données utilisent "Regular Season" et "Playoffs" (pas "Regular")
3. **Extraction de saison** : Il faut calculer la saison NBA à partir de la date (octobre = début de saison)
4. **Données manquantes** : Certains joueurs n'ont pas de salaire, j'ai filtré ces cas
5. **Performance** : R² de 0.32 c'est pas génial mais avec seulement 3 variables c'est correct

## Exemples de résultats

**Leaderboard points 2024** :
1. Shai Gilgeous-Alexander (32.1 pts/match)
2. Giannis Antetokounmpo (29.5 pts/match)
3. Nikola Jokic (29.2 pts/match)

**Résumé Lakers 2024** :
- 6,867 matchs joués
- 58.5% de victoires
- 106.7 points moyens

**Prédiction salaire** :
- Joueur avec 15 pts, 5 pds, 8 reb → ~15.4M$ prédit
- Erreur absolue moyenne : ~9M$ (les salaires NBA varient énormément)

## Notes techniques

- Gestion des erreurs pour équipes/stats inexistantes
- Les 3 commandes CLI sont installées automatiquement avec le package

---

