from simpleai.search import breadth_first, SearchProblem, astar, greedy
from simpleai.search.viewers import WebViewer


INICIAL = (
    (1, 0, 1, 0, 1, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 1, 1, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    (0, 0, 0, 2, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
    (0, 1, 0, 0, 1, 0, 1, 1, 0, 0)
)



def resolver(metodo_busqueda, posicion_rey, controlar_estador_repetidos):
    return

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
        '''cerca = 0
        fila_rey, col_rey = donde_esta(state, 2)
        if fila_rey == 0 or col_rey == 0 or fila_rey == 9 or col_rey == 9:
            #posible_meta = fila_si_llego_a_un_lado(fila_rey, col_rey)
            if col_rey == 0 or col_rey == 9: #si esta en las columnas laterales
                if fila_rey != 0:
                    if state[fila_rey - 1][col_rey] == 1:
                        cerca += 1
                if fila_rey != 9:
                    if state[fila_rey + 1][col_rey] == 1:
                        cerca += 1
            if fila_rey == 0 or fila_rey == 9: #si esta en la primer o ultima fila
                if col_rey != 0:
                    if state[fila_rey][col_rey - 1] == 1:
                        cerca += 1
                if col_rey != 9:
                    if state[fila_rey][col_rey + 1] == 1:
                        cerca += 1
        if cerca == 2:
            meta = True
        else:
            meta = False
        return meta'''

    def actions(self, state):
        acciones = []
        fila_rey, col_rey = donde_esta(state, 2)

        if fila_rey > 0 and fila_rey < 9 and col_rey > 0 and col_rey < 9:
            cerca = 0
            if state[fila_rey - 1][col_rey] != 0: #si el lugar esta vacio, y podria moverme
                if fila_rey - 1 != 0:           #si no esta en un borde
                    if state[fila_rey -2, col_rey] == 1:
                        cerca += 1
                if state[fila_rey - 1, col_rey + 1] == 1:
                    cerca += 1
                if state[fila_rey - 1, col_rey - 1] == 1:
                    cerca += 1
            if cerca <= 1:
                acciones.append(state[fila_rey - 1][col_rey])
            cerca = 0
            if state[fila_rey + 1][col_rey] != 0:  # si el lugar esta vacio, y podria moverme
                if fila_rey + 1 != 9:  # si no esta en un borde
                    if state[fila_rey + 2, col_rey] == 1:
                        cerca += 1
                if state[fila_rey + 1, col_rey + 1] == 1:
                    cerca += 1
                if state[fila_rey + 1, col_rey - 1] == 1:
                    cerca += 1
            if cerca <= 1:
                acciones.append(state[fila_rey + 1][col_rey])
            #----------------------------ahora voy a ver si puedo moverme a derecha o a izquierda----------------------------
            cerca = 0
            if state[fila_rey][col_rey - 1] != 0:  # si el lugar esta vacio, y podria moverme
                if col_rey - 1 != 0:  # si no esta en un borde
                    if state[fila_rey, col_rey - 2] == 1:
                        cerca += 1
                if state[fila_rey + 1, col_rey - 1] == 1:
                    cerca += 1
                if state[fila_rey - 1, col_rey - 1] == 1:
                    cerca += 1
            if cerca <= 1:
                acciones.append(state[fila_rey][col_rey - 1])
            cerca = 0
            if state[fila_rey][col_rey + 1] != 0:  # si el lugar esta vacio, y podria moverme
                if col_rey + 1 != 9:  # si no esta en un borde
                    if state[fila_rey, col_rey + 2] == 1:
                        cerca += 1
                if state[fila_rey + 1, col_rey + 1] == 1:
                    cerca += 1
                if state[fila_rey - 1, col_rey + 1] == 1:
                    cerca += 1
            if cerca <= 1:
                acciones.append(state[fila_rey][col_rey + 1])

        return acciones

    def result(self, state, action):
        fila_rey, col_rey = donde_esta(state, 2)
        fila_otro, col_otro = donde_esta(state, action)

        state = t2l(state)
        state[fila_rey][col_rey] = action
        state[fila_otro][col_otro] = 2
        state = l2t(state)

        return state

    '''def heuristico(self, state):
        total = 0
        for pieza in range[100]:
            pieza += 1
            fila_pieza, col_pieza = donde_esta(state, pieza)
            fila_meta, col_meta = donde_esta(META, pieza)
            distancia = abs(col_pieza - col_meta) + abs(fila_pieza - fila_meta)
            
        return total'''

if __name__ == '__main__': #para que cunado lo importo no se mejecute.

    problema = HnefataflProblem(INICIAL)

    resultado = astar(problema)

    print 'Estado meta:'    
    print resultado.state
    print 'Camino:'
    for accion, estado in resultado.path():
        print 'Movi', accion
        print 'Llegue a', estado







