def echange(tab, i, j):
    """Echange les éléments d'indice i et j dans le tableau tab."""
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_selection(tab):
    """Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection."""
    # Vérification du type de tab
    assert type(tab) == list, "tab doit être une liste"
    N = len(tab)
    for k in range(N):
        # Recherche de l'indice du minimum
        imin = k
        # On parcourt les éléments de k+1 à N-1
        for i in range(k + 1, N):
            # Si on trouve un élément plus petit que tab[imin]
            if tab[i] < tab[imin]:
                # On met à jour l'indice du minimum
                imin = i
        # On échange tab[k] et tab[imin]
        echange(tab, k, imin)


# Tests
liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
assert liste == [6, 12, 18, 21, 25, 41, 55]
