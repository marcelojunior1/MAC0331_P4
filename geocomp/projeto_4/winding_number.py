from geocomp.common import prim
from geocomp.common import segment
from geocomp.common import control
from geocomp import config

# Tolerancia
TOL = 10 ^ (-6)


def Winding_Number(l):
    # Registra o ponto
    origem = l[0]
    del l[0]

    print(l)
