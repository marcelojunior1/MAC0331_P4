from geocomp.common import control
from geocomp.common.point import Point


def Ray_Crossing(l):
    print("\n")
    ponto = l[0]
    del l[0]

    ponto.hilight("yellow")

    c = 0
    d = 0

    control.sleep()

    linha = control.plot_horiz_line(ponto.y, "blue", 1)

    control.sleep()
    for i in range(len(l)):
        segm_l = l[i]

        segm_l.hilight("blue")

        p1 = Point(segm_l.init.x, segm_l.init.y)
        p2 = Point(segm_l.to.x, segm_l.to.y)

        p1.x -= ponto.x
        p1.y -= ponto.y
        p2.x -= ponto.x
        p2.y -= ponto.y

        if p1.x == 0 and p1.y == 0:
            print("Dentro")
            ponto.hilight("green")
            control.plot_delete(linha)
            return True

        teste_c = (p1.y > 0) is not (p2.y > 0)
        teste_d = (p1.y < 0) is not (p2.y < 0)

        if teste_c or teste_d:
            if teste_c and intersecao_eixo_x(p1, p2) > 0:
                c += 1
            if teste_d and intersecao_eixo_x(p1, p2) < 0:
                d += 1

        control.sleep()
        segm_l.unhilight()

    if not ((c % 2 == 0 and d % 2 == 0) or (c % 2 != 0 and d % 2 != 0)):
        print("Dentro")
        ponto.hilight("green")
        control.plot_delete(linha)
        return True

    if c % 2 != 0:
        print("Dentro")
        ponto.hilight("green")
        control.plot_delete(linha)
        return True
    else:
        print("Fora")
        ponto.hilight("red")
        control.plot_delete(linha)
        return False

def intersecao_eixo_x(p1, p2):
    x = (p1.x * p2.y - p2.x * p1.y) / (p2.y - p1.y)
    return x
