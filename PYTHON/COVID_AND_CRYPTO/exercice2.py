__version__ = "TP5 - Exercice #2"
__author__ = "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"

# Soient les seules librairies pouvant être utilisées et importées au sein de ce fichier, faites-en bons usages !
import csv
import json

"""
 * <PARTIE 1.1 DU MANDAT>
 * Retourne le contenu d'un fichier CSV sous forme de liste.
 * @param   chemin_fichier  (str)   Le chemin vers le fichier CSV.
 * @param   delimiteur      (str)   Le délimiteur utilisé pour séparer les données au sein du fichier CSV.
 * @return                  (list)  Le contenu du fichier csv sous forme de liste.
"""


def charger_donnees(chemin_fichier: str, delimiteur: str) -> list:
    # Écrivez ici, enlevez le 'pass'
    pass


"""
 * <PARTIE 1.2 DU MANDAT>
 * Retourne une liste de données uniquement valides pour un pays donné.
 * @param   nom_pays    (str)   Le nom d'un pays donné.
 * @return              (list)  La liste de données pour un pays donné.
"""


def donnees_pays(nom_pays: str) -> list:
    # Écrivez ici, enlevez le 'pass'
    pass


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
    # Écrivez ici, enlevez le 'pass'
    pass


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
    # Écrivez ici, enlevez le 'pass'
    pass


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
    # Écrivez ici, enlevez le 'pass'
    pass
