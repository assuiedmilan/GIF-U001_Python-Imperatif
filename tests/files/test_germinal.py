import os

import pytest


@pytest.fixture()
def germinal():
    germinal = """Dans la plaine rase, sous la nuit sans étoiles,
    d’une obscurité et d’une épaisseur d’encre, un
    homme suivait seul la grand-route de
    Marchiennes à Montsou, dix kilomètres de pavé,
    coupant tout droit, à travers les champs de
    betteraves. Devant lui, il ne voyait même pas le
    sol noir, et il n’avait la sensation de l’immense
    horizon plat que par les souffles du vent de mars,
    des rafales larges comme sur une mer, glacées
    d’avoir balayé des lieues de marais et de terres
    nues. Aucune ombre d’arbre ne tachait le ciel, le
    pavé se déroulait avec la rectitude d’une jetée, au
    milieu de l’embrun aveuglant des ténèbres.
    """

    with open('germinal.txt', mode='wb') as fich:
        fich.write(germinal.encode('utf-16'))


def test_germinal(germinal):
    with open('germinal.txt', 'rb') as fich:
        zola = fich.read().decode('utf-16')
        print(zola.strip())