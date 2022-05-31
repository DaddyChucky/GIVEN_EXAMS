__version__ = "TP5 - Exercice #1"
__author__ = "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


# Soit la seule librairie pouvant être utilisée et importée au sein de ce fichier, faites-en bon usage !
import string

"""
 * <PARTIE 1.1 DU MANDAT>
 * Retourne le contenu d'un fichier.
 * @param chemin_fichier    (str) Le chemin vers le fichier.
 * @return                  (str) Le contenu du fichier.
"""


def charger_contenu(chemin_fichier: str) -> str:
    # Écrivez ici, enlevez le 'pass'
    pass


"""
 * <PARTIE 1.2 DU MANDAT>
 * Crée un dictionnaire qui devrait lier le code obfusqué lu en tant que clé au code équivalent en Python (valeur).
 * Attention! Cette fonction devrait faire usage des fonctions hex(), ord() et chr() et non bêtement copier la table
 * présentée au Tableau 1. La moitié des points sera justement accordée pour la brièveté et l'ingéniosité de votre
 * implémentation (pensez à user des imports et à regarder dans la documentation pour des fontions simples qui font
 * une partie du travail à votre place!).
 * @return (dict) Un tel dictionnaire.
"""


def creer_dictionnaire() -> dict:
    # Écrivez ici, enlevez le 'pass'
    pass


"""
 * <PARTIE 1.3 DU MANDAT>
 * À partir du contenu du programme brumeux et de votre dictionnaire nouvellement créé, transpilez au sein 
 * du fichier programme-decouvert.txt. Si ce fichier n'existe pas déjà, il doit être créé. Pareillement, 
 * s'il existe déjà, son contenu doit être écrasé à chaque fois que ce script est exécuté.
 * Attention, cette fonction ne prend rien en paramètres. Vous devez vous servir des fonctions réalisées
 * précédemment pour parvenir à vos fins.
 * @param chemin_fichier_brumeux    (str) Le chemin vers le fichier brumeux.
 * @param chemin_fichier_transpile  (str) Le chemin vers le fichier transpilé.
"""


def transpilation(chemin_fichier_brumeux: str = 'programme-obfusque.txt',
                  chemin_fichier_transpile: str = 'programme-decouvert.txt') -> None:
    # Écrivez ici, enlevez le 'pass'
    pass


"""
 * <PARTIE 2 DU MANDAT>
 * À partir du contenu du programme à découvert du fichier programme-a-obfusquer.txt,veuillez obfusquer son contenu 
 * dans un second fichier, nommé programme-obfusque.txt. Si ce fichier n'existe pas déjà, il doit être créé. 
 * Pareillement, s'il existe déjà, son contenu doit être écrasé à chaque fois que ce script est exécuté.
 * Attention, cette fonction ne prend rien en paramètres. Vous devez vous servir des fonctions réalisées
 * précédemment pour parvenir à vos fins. Ici, vous avez deux façons de procéder. 1) En obfuscant caractère par
 * caractère (méthode la plus facile utilisée dans les tests), ou 2) vérifier si la partie lue correspond à 
 * une structure de contrôle et vérifier dans votre dictionnaire sa concordance en assembleur. Bien que les tests
 * ne soient pas fournis pour la 2e méthode, nous allons en tenir compte dans la correction de votre ingéniosité.
 * @param chemin_fichier_a_obfusquer    (str) Le chemin vers le fichier a obfusquer.
 * @param chemin_fichier_obfusque       (str) Le chemin vers le fichier obfusqué.
"""


def obfuscation(chemin_fichier_a_obfusquer: str = 'programme-a-obfusquer.txt',
                chemin_fichier_obfusque: str = 'programme-obfusque.txt') -> None:
    # Écrivez ici, enlevez le 'pass'
    pass
