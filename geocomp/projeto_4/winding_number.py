import math

from geocomp.common import prim
from geocomp.common import segment
from geocomp.common import control
from geocomp import config

# Tolerancia
from geocomp.common.point import Point
from geocomp.common.segment import Segment

TOL = 10 ^ (-6)


def Winding_Number(l):
    print("\n")
    origem = l[0]
    del l[0]

    soma = 0.0
    somaAngulos = 0.0

    control.sleep()
    for i in range(len(l)):
        segm = l[i]
        segm1 = Segment(origem, segm.init)
        segm2 = Segment(origem, segm.to)

        segm1.hilight()
        segm2.hilight()
        origem.hilight("yellow")

        # Define os pontos
        p1 = Point(l[i].init.x, l[i].init.y)
        p2 = Point(l[i].to.x, l[i].to.y)
        xc = origem.x
        yc = origem.y

        # Torna o ponto como origem do sistema
        x1 = p1.x - xc
        y1 = p1.y - yc
        x2 = p2.x - xc
        y2 = p2.y - yc

        # Calcula o angulo
        theta_1 = math.atan2(y1, x1)
        theta_2 = math.atan2(y2, x2)

        if theta_1 < 0:
            theta_1 += 2*math.pi
        if theta_2 < 0:
            theta_2 += 2*math.pi

        angulo = abs(theta_1 - theta_2)
        if abs(theta_1 - theta_2) > math.pi:
            angulo = 2*math.pi - angulo

        # Define o sinal do angulo
        if prim.left(p1, p2, origem):
            angulo *= -1

        # Soma o valor
        soma += angulo
        somaAngulos += theta_1

        control.sleep()
        segm1.hide()
        segm2.hide()

    print(soma)
    if abs(soma) < TOL:
        origem.hilight("red")
    else:
        origem.hilight("green")
