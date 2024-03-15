graphe = {0: [1, 2], 1: [2], 2: [0], 3: [0]}


def voisins(graphe, sommet):
    """renvoie la liste des voisins du sommet dans le graphe"""
    assert sommet in graphe, "le sommet n'est pas dans le graphe"
    # Les successeurs du sommet sont des voisins du sommet
    resultat = graphe[sommet]
    for cle in graphe:
        if cle != sommet and cle not in resultat and sommet in graphe[cle]:
            resultat.append(cle)
    return resultat

print(voisins(graphe, 0))
assert voisins(graphe, 0) == [1, 2, 3]
assert voisins(graphe, 1) == [2, 0]
assert voisins(graphe, 2) == [0, 1]
assert voisins(graphe, 3) == [0]
