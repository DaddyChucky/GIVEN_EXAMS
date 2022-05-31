__version__ = "TP5 - Exercice #1"
__author__ = "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"

import string

"""
 * <PARTIE 1.1 DU MANDAT>
 * Retourne le contenu d'un fichier.
 * @param chemin_fichier    (str) Le chemin vers le fichier.
 * @return                  (str) Le contenu du fichier.
"""


def charger_contenu(chemin_fichier: str) -> str:
    with open(chemin_fichier, 'r') as fichier_brumeux:
        return fichier_brumeux.read()


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
    # Créer mon dictionnaire
    mon_dictionnaire: dict = dict()

    # Ajouter les symboles à mon dictionnaire
    for letter in string.ascii_letters + string.digits + '()." /=:;<>_-\\+,\'{}#*[]':
        mon_dictionnaire['//[' + hex(ord(letter)) + ']'] = letter

    # Ajouter le code mort à mon dictionnaire
    cles_code_mort: list = ['//[0x7F]', '//[0x00]', '//[0x07]', '//[0x1E]']
    for cle in cles_code_mort:
        mon_dictionnaire[cle] = ''

    # Ajouter les fonctions à mon dictionnaire
    valeurs_fonctions_assembleur: list = ['if', 'else', 'while', 'for', 'range', 'try']
    for valeur in valeurs_fonctions_assembleur:
        mon_dictionnaire['_ZN4crtl1' + valeur[0] + 'C1Ev'] = valeur

    # Ajouter les autres symboles à mon dictionnaire
    dictionnaire_autres_symboles: dict = {
        '_ZN4crtl2exC1Ev': 'except',
        '_ZN4util3impC1Ev': 'import',
        '//[0x09]': '\n'
    }
    mon_dictionnaire.update(dictionnaire_autres_symboles)
    return mon_dictionnaire


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
    # Initialisation du contenu du programme brumeux et de mon dictionnaire
    programme_brumeux: str = charger_contenu(chemin_fichier_brumeux)
    mon_dictionnaire: dict = creer_dictionnaire()
    possibilites_longueur: list = []
    programme_decouvert: str = ''

    # Calculer les longueurs possibles
    for cle in mon_dictionnaire.keys():
        longueur_cle: int = len(cle)
        if longueur_cle not in possibilites_longueur:
            possibilites_longueur.append(longueur_cle)

    # Transpiler le programme brumeux au sein du programme decouvert
    i = 0
    while i < len(programme_brumeux):
        for longueur in sorted(possibilites_longueur, reverse=True):
            mot_asm: str = programme_brumeux[i:i+longueur]
            if mot_asm in mon_dictionnaire.keys():
                i += longueur
                programme_decouvert += mon_dictionnaire[mot_asm]
                break

    # Ecrire le tout dans programme_decouvert.txt
    with open(chemin_fichier_transpile, 'w') as fichier_transpile:
        fichier_transpile.write(programme_decouvert)

    if __name__ == "__main__":
        print(f'Transpilation terminee avec succes du fichier {chemin_fichier_brumeux} au sein du fichier'
              f' {chemin_fichier_transpile}')


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
    # Obtenir le contenu du fichier à obfusquer
    contenu_a_obfusquer: str = charger_contenu(chemin_fichier_a_obfusquer)
    mon_dictionnaire: dict = creer_dictionnaire()
    dictionnaire_inverse = {valeur: cle for (cle, valeur) in mon_dictionnaire.items()}
    contenu_obfusque: str = ''

    # Obfusquer le contenu et l'insérer dans contenu_obfusque
    for lettre in contenu_a_obfusquer:
        contenu_obfusque += dictionnaire_inverse[lettre]

    with open(chemin_fichier_obfusque, 'w') as fichier_obfusque:
        fichier_obfusque.write(contenu_obfusque)

    if __name__ == "__main__":
        print(f'Obfuscation terminee avec succes du fichier {chemin_fichier_a_obfusquer} au sein du fichier'
              f' {chemin_fichier_obfusque}')
