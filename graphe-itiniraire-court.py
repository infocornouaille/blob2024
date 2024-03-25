graphe = {"A": ["B","C","H"],
          "B": ["A", "I"],
          "C": ["A", "D", "E"],
          "D": ["C", "E"],
          "E": ["C", "D", "G"],
          "F": ["G", "I"],
          "G": ["E", "F", "H"],
          "H": ["A", "G", "I"],
          "I": ["B", "F", "H"]}

def recherche_chemin_court(graphe:dict,sommet_depart:str,sommet_arrivee:str):
    """Recherche les chemins les plus court entre 
    deux sommets d'un graphe"""
    if sommet_depart not in graphe:
        return []
    if sommet_arrivee not in graphe:
        return []
    
