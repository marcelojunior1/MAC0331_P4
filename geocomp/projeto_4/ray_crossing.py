from math import inf

from geocomp.common import prim
from geocomp.common import segment
from geocomp.common import control
from geocomp import config
from geocomp.common.point import Point
from geocomp.common.prim import intersect
from geocomp.common.segment import Segment


def Ray_Crossing(l):
    print("\n")
    ponto = l[0]
    del l[0]

    print(ponto)

    c = 0
    d = 0

    for i in range(len(l)):
        segm_l = l[i]
        p1 = segm_l.init
        p2 = segm_l.to

        p1.x -= ponto.x
        p1.y -= ponto.y
        p2.x -= ponto.x
        p2.y -= ponto.y

        if p1.x == 0 and p1.y == 0:
            print("Dentro")
            return True

        teste_c = (p1.y > 0) is not (p2.y > 0)
        teste_d = (p1.y < 0) is not (p2.y < 0)

        if teste_c or teste_d:
            if teste_c and intersecao_eixo_x(p1, p2) > 0:
                c += 1
            if teste_d and intersecao_eixo_x(p1, p2) < 0:
                d += 1

    if not ((c % 2 == 0 and d % 2 == 0) or (c % 2 != 0 and d % 2 != 0)):
        print("Dentro")
        return True

    if c % 2 != 0:
        print("Dentro")
        return True
    else:
        print("Fora")
        return False


def intersecao_eixo_x(p1, p2):
    x = (p1.x * p2.y - p2.x * p1.y) / (p2.y - p1.y)
    return x
