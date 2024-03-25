def est_cyclique(plan):
    """Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon."""
    # Vérification du type de plan
    assert type(plan) == dict, "plan doit être un dictionnaire"
    # Initialisation
    expediteur = "A"
    destinataire = plan[expediteur]
    nb_destinaires = 1
    # Tant que le destinataire n'est pas l'expéditeur
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)


# Affichages
print(est_cyclique({"A": "E", "F": "A", "C": "D", "E": "B", "B": "F", "D": "C"}))
print(est_cyclique({"A": "E", "F": "C", "C": "D", "E": "B", "B": "F", "D": "A"}))
print(est_cyclique({"A": "B", "F": "C", "C": "D", "E": "A", "B": "F", "D": "E"}))
print(est_cyclique({"A": "B", "F": "A", "C": "D", "E": "C", "B": "F", "D": "E"}))

# Tests
assert (
    est_cyclique({"A": "E", "F": "A", "C": "D", "E": "B", "B": "F", "D": "C"}) == True
)
assert (
    est_cyclique({"A": "E", "F": "C", "C": "D", "E": "B", "B": "F", "D": "A"}) == False
)
assert (
    est_cyclique({"A": "B", "F": "C", "C": "D", "E": "A", "B": "F", "D": "E"}) == False
)
assert (
    est_cyclique({"A": "B", "F": "A", "C": "D", "E": "C", "B": "F", "D": "E"}) == False
)
