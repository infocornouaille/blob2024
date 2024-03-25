```python linenums='1' hl_lines='27 29 31 33 34'
class Pile:
    """Classe définissant une structure de pile."""

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n'est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()


def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch est bien parenthésée"""
    # Vérification du type de ch
    assert type(ch) == str, "ch doit être une chaîne de caractères"
    # Initialisation de la pile
    p = Pile()
    # Parcours des caractères de ch
    for c in ch:
        # Si c est une parenthèse ouvrante, on l'empile
        if c == "(":
            p.empiler(c)
        # Si c est une parenthèse fermante
        elif c == ")":
            # Si la pile est vide, la chaîne n'est pas bien parenthésée
            if p.est_vide():
                return False
            # Sinon, on dépile
            else:
                p.depiler()
    # Si la pile est vide, la chaîne est bien parenthésée
    return p.est_vide()


# Tests
assert bon_parenthesage("((()())(()))") == True
assert bon_parenthesage("())(()") == False
assert bon_parenthesage("(())(()") == False

```