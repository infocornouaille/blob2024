a = {
    "F": ["B", "G"],
    "B": ["A", "D"],
    "A": ["", ""],
    "D": ["C", "E"],
    "C": ["", ""],
    "E": ["", ""],
    "G": ["", "I"],
    "I": ["", "H"],
    "H": ["", ""],
}


def taille(arbre, lettre):
    """Retourne la taille de l'arbre"""
    # Vérification des types
    assert type(arbre) == dict, "L'arbre doit être un dictionnaire"
    assert type(lettre) == str, "La lettre doit être une chaîne de caractères"
    # Si la lettre est vide, on retourne 0
    if lettre == "":
        return 0
    # Sinon, on retourne 1 + la taille de la branche de gauche + la taille de la branche de droite
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])


# Tests sur les exemples de l'énoncé
assert taille(a, "F") == 7
assert taille(a, "B") == 5
assert taille(a, "A") == 1
assert taille(a, "D") == 3
