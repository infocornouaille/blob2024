graphe = {"A": ["B","C","H"],
          "B": ["A", "I"],
          "C": ["A", "D", "E"],
          "D": ["C", "E"],
          "E": ["C", "D", "G"],
          "F": ["G", "I"],
          "G": ["E", "F", "H"],
          "H": ["A", "G", "I"],
          "I": ["B", "F", "H"]}


tab_itineraires=[]
def cherche_itineraires(G, start, end, chaine=[]):
    chaine = chaine + [start]
    if start == end:
        return chaine
    for u in G[start]:
        if u not in chaine:
            nchemin = cherche_itineraires(G, u, end, chaine)
            if len(nchemin) != 0:
                tab_itineraires.append(nchemin)
    return []

def itineraires_court(G,dep,arr):
    cherche_itineraires(G, dep, arr)
    # tab_court = ...
    # Initialisation
    tab_court = []
    # Initialisation de la variable mini à l'infini
    mini = float('inf')
    # Parcours de la liste des itinéraires
    for v in tab_itineraires:
        # if len(v) <= ... :
        if len(v) <= mini :
            # mini = ...
            mini = len(v)
    for v in tab_itineraires:
        if len(v) == mini:
            # tab_court.append(...)
            tab_court.append(v)
    return tab_court
