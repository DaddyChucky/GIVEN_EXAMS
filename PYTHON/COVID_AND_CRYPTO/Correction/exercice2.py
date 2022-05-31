__version__ = "TP5 - Exercice #2"
__author__ = "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"

import csv
import json

chemin_fichier_csv: str = 'vaccinations.csv'
delimiteur_csv: str = ','
chemin_fichier_rapport_json: str = 'rapport.json'
indentation_json: int = 4

"""
 * <PARTIE 1.1 DU MANDAT>
 * Retourne le contenu d'un fichier CSV sous forme de liste.
 * @param   chemin_fichier  (str)   Le chemin vers le fichier CSV.
 * @param   delimiteur      (str)   Le délimiteur utilisé pour séparer les données au sein du fichier CSV.
 * @return                  (list)  Le contenu du fichier csv sous forme de liste.
"""


def charger_donnees(chemin_fichier: str, delimiteur: str) -> list:
    liste_fichier_csv: list = []
    with open(chemin_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier, delimiter=delimiteur)
        for ligne in lecteur_csv:
            liste_fichier_csv.append(ligne)
    return liste_fichier_csv


"""
 * <PARTIE 1.2 DU MANDAT>
 * Retourne une liste de données uniquement valides pour un pays donné.
 * @param   nom_pays    (str)   Le nom d'un pays donné.
 * @return              (list)  La liste de données pour un pays donné.
"""


def donnees_pays(nom_pays: str) -> list:
    index_nom_pays: int = 0
    donnees: list = charger_donnees(chemin_fichier_csv, delimiteur_csv)
    donnees_pays_concerne: list = []
    for ligne in donnees:
        if ligne[index_nom_pays] == nom_pays:
            donnees_pays_concerne.append(ligne)
    return donnees_pays_concerne


"""
 * <PARTIE 1.3 DU MANDAT>
 * Trouver le nombre d'habitants maximal d'un pays. Vous devez utiliser la fonction construite à l'étape
 * précédente pour parcourir le lot de données, en plus de faire une manipulation sur cette liste pour obtenir que
 * les données du pays concerné. Indice: utilisez les colonnes des personnes vaccinées quotidiennement (brut et par
 * million) et appliquez la règle de trois pour trouver une estimation du nombre d'habitants. Vous devriez obtenir
 * une estimation par ligne de données. Parcourez toutes les lignes et retourner votre estimation maximale. À noter que,
 * pour certains pays, votre estimation peut être complètement fausse ou irréaliste. Ce n'est pas grave!
 * @param   nom_pays  (str) Le nom du pays concerné.
 * @return            (int) Le nombre d'habitants maximal.
"""


def nombre_habitants_maximal(nom_pays: str) -> int:
    index_personnes_vaccinees_quotidiennement_par_million: int = 13
    index_personnes_vaccinees_quotidiennement: int = 14
    n_lignes: int = 0
    facteur_million: int = 1000000
    estimations_nombre_habitants: list = []
    donnees_pays_concerne: list = donnees_pays(nom_pays)
    for ligne in donnees_pays_concerne:
        n_lignes += 1
        try:
            estimations_nombre_habitants.append(int(ligne[index_personnes_vaccinees_quotidiennement]) /
                                                float(ligne[index_personnes_vaccinees_quotidiennement_par_million]) *
                                                facteur_million)
        except ZeroDivisionError:
            continue
        except ValueError:
            continue
    return int(max(estimations_nombre_habitants))


"""
 * <PARTIE 1.4 DU MANDAT>
 * À partir de votre fonction construite à la partie 1.3, vous avez maintenant une estimation du nombre d'habitants
 * pour un pays concerné. Établissez maintenant le pourcentage de la population vaccinée (rapport entre le nombre total
 * de personnes vaccinées et le nombre d'habitants).
 * @param   nom_pays  (str)     Le nom du pays concerné.
 * @return            (float)   Le pourcentage de la population vaccinée (AB.CD) à 2 chiffres significatifs 
 *                              après la virgule.
"""


def pourcentage_population_vaccinee(nom_pays: str) -> float:
    idx_total_pers_vaccinees: int = 5
    idx_max: int = 0
    facteur_pourcentage: int = 100
    nombre_habitants: int = nombre_habitants_maximal(nom_pays)
    donnees_pays_concerne: list = donnees_pays(nom_pays)
    try:
        return round(
            int(sorted(donnees_pays_concerne, key=lambda x: x[2], reverse=True)[idx_max][idx_total_pers_vaccinees]) /
            nombre_habitants * facteur_pourcentage, 2)
    except ZeroDivisionError:
        return 0.


"""
 * <PARTIE 1.5 DU MANDAT>
 * Vous devez à présent proposez au docteur toutes les destinations probables comme destination-retraite. Pour ce faire,
 * utilisez votre fonction de la partie 1.4 en itérant sur chaque pays et, si le pays possède un seuil de personnes
 * vaccinées supérieur ou égal à 75 %, vous devez l'inclure au sein de votre rapport.json. Bien entendu, vous devez
 * créer un tel rapport si ce fichier n'est pas déjà créé. S'il l'est déjà, vous devez l'écraser. Le format du rapport
 * attendu est indiqué au sein de l'énoncé. À noter que vous devez traiter certaines données aberrantes si vous
 * constatez que le pourcentage de la population vaccinée surpasse 100 % (dû à l'estimation du nombre d'habitants).
 * Note: le docteur souhaite sortir du pays!
"""


def destinations_retraite() -> None:
    donnees_csv: list = charger_donnees(chemin_fichier_csv, delimiteur_csv)
    idx_pays: int = 0
    destinations_invalides: list = ['location', 'Canada']
    seuil_min: float = 75.00
    seuil_max: float = 100.00
    nom_pays: list = []
    destinations_retraite_possibles: dict = dict()
    for ligne in donnees_csv:
        if ligne[idx_pays] not in nom_pays and ligne[idx_pays] not in destinations_invalides:
            nom_pays.append(ligne[idx_pays])
    for pays in list(nom_pays)[::-1]:
        try:
            pourcentage_pop_vaccinee: float = pourcentage_population_vaccinee(pays)
            nombre_habitants: int = nombre_habitants_maximal(pays)
            if seuil_max >= pourcentage_pop_vaccinee >= seuil_min:
                destinations_retraite_possibles[pays] = {
                    'pourcentage_population_vaccinee': pourcentage_pop_vaccinee,
                    'nombre_habitants': nombre_habitants,
                    'nombre_personnes_vaccinees': int(nombre_habitants * pourcentage_pop_vaccinee / seuil_max)
                }
        except ValueError or ZeroDivisionError:
            continue

    with open(chemin_fichier_rapport_json, 'w') as rapport:
        json.dump(destinations_retraite_possibles, rapport, ensure_ascii=False, indent=indentation_json)
