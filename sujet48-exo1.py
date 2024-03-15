graphe = [[1, 2], [2], [0], [0]]


def voisins(graphe, sommet):
    """renvoie la liste des voisins du sommet dans le graphe"""
    assert sommet < len(graphe), "le sommet n'est pas dans le graphe"
    # Les successeurs du sommet sont des voisins du sommet
    resultat = graphe[sommet]
    for i in range(len(graphe)):
        if i != sommet and i not in resultat and sommet in graphe[i]:
            resultat.append(i)
    return resultat

assert voisins(graphe, 0) == [1, 2, 3]
assert voisins(graphe, 1) == [2, 0]
assert voisins(graphe, 2) == [0, 1]
assert voisins(graphe, 3) == [0]