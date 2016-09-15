from simpleai.search import breadth_first, SearchProblem, astar, greedy, depth_first
from simpleai.search.viewers import BaseViewer



INICIAL = (
    (1, 0, 1, 0, 1, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
    (0, 1, 0, 0, 1, 0, 1, 1, 0, 0)
)

visor = BaseViewer()


def colocar_rey(Estado_Inicial, posicion):
    Estado_Inicial = t2l(Estado_Inicial)
    Estado_Inicial[posicion[0]][posicion[1]] = 2
    Estado_Inicial = l2t(Estado_Inicial)
    return Estado_Inicial


def resolver(metodo_busqueda, posicion_rey, controlar_estados_repetidos):

    #poner al rey y ese va a ser INICIAL
    EstadoDeInicio = colocar_rey(INICIAL,posicion_rey)
    metodos_busqueda = {'astar':astar,
                        'breadth_first':breadth_first,
                        'greedy':greedy,
                        'depth_first':depth_first}
    result = metodos_busqueda[metodo_busqueda](HnefataflProblem(EstadoDeInicio),controlar_estados_repetidos, viewer=visor)
    #result = metodos_busqueda[metodo_busqueda](HnefataflProblem(EstadoDeInicio),controlar_estados_repetidos)
    return result

def donde_esta(state, numero):
    for indice_fila, fila in enumerate(state):
        for indice_columna, numero_actual in enumerate(fila):
            if numero_actual == numero:
                return indice_fila, indice_columna


#quiero ver si podria ser meta viendo las posiciones cercanas donde llego..
#def fila_si_llego_a_un_lado(fila, col):



def t2l(t):
    return list(list(r) for r in t)


def l2t(l):
    return tuple(tuple(r) for r in l)


class HnefataflProblem(SearchProblem):

    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        meta = False
        fila_rey, col_rey = donde_esta(state, 2)
        if fila_rey == 0 or col_rey == 0 or fila_rey == 9 or col_rey == 9:
            meta = True
        return meta


    def actions(self, state):
        acciones = []
        fila_rey, col_rey = donde_esta(state, 2)

        if (fila_rey > 0) and (fila_rey < 9) and (col_rey > 0) and (col_rey < 9):
            cerca = 0
            if state[fila_rey - 1][col_rey] == 0: #si el lugar esta vacio, y podria moverme
                if fila_rey - 1 != 0:           #si no esta en un borde
                    if state[fila_rey -2][col_rey] == 1:
                        cerca += 1
                if state[fila_rey - 1][col_rey + 1] == 1:
                    cerca += 1
                if state[fila_rey - 1][col_rey - 1] == 1:
                    cerca += 1
                if cerca <= 1:
                    acciones.append((fila_rey - 1, col_rey))
            cerca = 0
            if state[fila_rey + 1][col_rey] == 0:  # si el lugar esta vacio, y podria moverme
                if fila_rey + 1 != 9:  # si no esta en un borde
                    if state[fila_rey + 2][col_rey] == 1:
                        cerca += 1
                if state[fila_rey + 1][col_rey + 1] == 1:
                    cerca += 1
                if state[fila_rey + 1][col_rey - 1] == 1:
                    cerca += 1
                if cerca <= 1:
                    acciones.append((fila_rey + 1, col_rey))
            #----------------------------ahora voy a ver si puedo moverme a derecha o a izquierda----------------------------
            cerca = 0
            if state[fila_rey][col_rey - 1] == 0:  # si el lugar esta vacio, y podria moverme
                if col_rey - 1 != 0:  # si no esta en un borde
                    if state[fila_rey][col_rey - 2] == 1:
                        cerca += 1
                if state[fila_rey + 1][col_rey - 1] == 1:
                    cerca += 1
                if state[fila_rey - 1][col_rey - 1] == 1:
                    cerca += 1
                if cerca <= 1:
                    acciones.append((fila_rey, col_rey - 1))
            cerca = 0
            if state[fila_rey][col_rey + 1] == 0:  # si el lugar esta vacio, y podria moverme
                if col_rey + 1 != 9:  # si no esta en un borde
                    if state[fila_rey][col_rey + 2] == 1:
                        cerca += 1
                if state[fila_rey + 1][col_rey + 1] == 1:
                    cerca += 1
                if state[fila_rey - 1][col_rey + 1] == 1:
                    cerca += 1
                if cerca <= 1:
                    acciones.append((fila_rey, col_rey + 1))

        return acciones

    def result(self, state, action):
        fila_rey, col_rey = donde_esta(state, 2)
        fila_otro, col_otro = action[0], action[1]

        state = t2l(state)
        state[fila_rey][col_rey] = 0
        state[fila_otro][col_otro] = 2
        state = l2t(state)

        return state

    def heuristic(self, state):
        rey_fila, rey_columna = donde_esta(state, 2)
        rey_fila_otroLado = 9 - rey_fila
        rey_columna_otroLado = 9 - rey_columna
        Menor = rey_fila
        if rey_fila > rey_columna:
            Menor = rey_columna
        if Menor > rey_columna_otroLado:
            Menor = rey_columna_otroLado
        if Menor > rey_fila_otroLado:
            Menor = rey_fila_otroLado
        return Menor


if __name__ == '__main__': #para que cunado lo importo no se mejecute.

    # # Caso 1
    #resultado = resolver('breadth_first', (5, 3), False) #No funciona con el BaseViewer
    # # Caso 2
    #resultado = resolver('breadth_first', (5, 3), True)
    # # Caso 3
    #resultado = resolver('depth_first', (5, 3), False)  #No funciona con el BaseViewer
    # # Caso 4
    #resultado = resolver('depth_first', (5, 3), True)
    # # Caso 5
    #resultado = resolver('greedy', (5, 3), False)   #No funciona con el BaseViewer
    # # Caso 6
    #resultado = resolver('greedy', (5, 3), True)
    # # Caso 7
    resultado = resolver('astar', (5, 3), False) #No funciona con el BaseViewer
    # # Caso 8
    #resultado = resolver('astar', (5, 3), True)

    # print 'Camino:'
    # for accion, estado in resultado.path():
    #     print 'Movi', accion
    #     print 'Llegue a', estado

    print 'Cantidad de nodos visitados:', visor.stats['visited_nodes']
    print 'Profundidad: ', resultado.depth
    print 'Costo: ', resultado.cost
    print 'Longitud maxima frontera:', visor.stats['max_fringe_size']



