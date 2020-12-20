def isnumber(string):
    try:
        float(string)
        return True
    except: # pylint: disable=bare-except
        return False


def valeur_liste(liste):
    liste_with_values = [x[:-1] if x[-1] == '$' else x + 'not a value' for x in liste]
    return sum(float(x) if isnumber(x) else 0 for x in liste_with_values)


def test_valeur_liste():
    liste = ['10$', 'chaussette', '12.55$', 'pizza', '0.57$', 'Rien', '7$', 'condom', '2$', '123a']
    assert valeur_liste(liste) == 32.120000000000005
