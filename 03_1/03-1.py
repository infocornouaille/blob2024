def maximum_tableau(tab):
    """Renvoie le maximum d'un tableau tab non vide."""
    # Vérification du type de tab
    assert type(tab) == list, "tab doit être une liste"
    # Vérification que le tableau n'est pas vide
    assert tab != [], "tab ne doit pas être vide"
    # Initialisation du maximum
    maximum = tab[0]
    # On parcourt les éléments du tableau
    for element in tab:
        # Si on trouve un élément plus grand que maximum
        if element > maximum:
            # On met à jour maximum
            maximum = element
    return maximum


# Tests
assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131
assert maximum_tableau([-27, 24, -3, 15]) == 24
