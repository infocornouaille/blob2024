class Graphe:

    def __init__(self, liste_sommets):
        self.liste_sommets = liste_sommets
        # Dictionnaire en compréhension
        self.adjacence = {sommets: [] for sommets in liste_sommets}

    def ajoute_arete(self, sommet1, sommet2):
        # Si le sommet2 n'est pas dans la liste des sommets du sommet1
        # On ajoute le sommet2 à la liste des sommets du sommet1
        if sommet2 not in self.liste_sommets[sommet1]:
            self.adjacence[sommet1].append(sommet2)
        # Si le sommet1 n'est pas dans la liste des sommets du sommet2
        # On ajoute le sommet1 à la liste des sommets du sommet2
        if sommet1 not in self.liste_sommets[sommet2]:
            self.adjacence[sommet2].append(sommet1)
    
    def sont_voisins(self, sommet1, sommet2):
        return sommet2 in self.adjacence[sommet1]
    
    def voisins(self, sommet):
        return self.adjacence[sommet]
        


graphe = Graphe(["A", "B", "C", "D", "E"])
graphe.ajoute_arete("A", "B")
graphe.ajoute_arete("A", "C")
graphe.ajoute_arete("A", "D")
graphe.ajoute_arete("A", "E")
graphe.ajoute_arete("B", "C")
print(graphe)
print(graphe.liste_sommets)
print(graphe.adjacence)

def BFS(g, depart):
    '''
    Effectue un parcours en largeur du graphe g en partant du sommet depart,
    et renvoie la liste des sommets visités dans l'ordre du parcours.
    '''
    traites = []
    decouverts = [depart]
    en_attente = [depart]
    while en_attente != [] :
        sommet = en_attente.pop(0)
        voisins = g.voisins(sommet)
        for voisin in voisins:
            if voisin not in decouverts:
                decouverts.append(voisin)
                en_attente.append(voisin)
        traites.append(sommet)
    return traites

print(BFS(graphe, "A"))