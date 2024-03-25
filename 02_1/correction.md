```python linenums='1'
def correspond(mot, mot_a_trous):
    """Vérifie si le mot correspond au mot à trous."""
    # Vérification des types
    assert type(mot) == str, "mot doit être une chaîne de caractères"
    assert type(mot_a_trous) == str, "mot_a_trous doit être une chaîne de caractères"
    # Si les longueurs des mots sont différentes, on retourne False
    if len(mot) != len(mot_a_trous):
        return False
    # On parcourt les lettres des deux mots
    for i in range(len(mot)):
        # Si les lettres sont différentes et que la lettre du mot à trous n'est pas une étoile, on retourne False
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != "*":
            return False
    # Si on n'a pas trouvé de différence, on retourne True
    return True


# Tests
assert correspond("INFORMATIQUE", "INFO*MA*IQUE") == True
assert correspond("AUTOMATIQUE", "INFO*MA*IQUE") == False
assert correspond("STOP", "S*") == False
assert correspond("AUTO", "*UT*") == True

```