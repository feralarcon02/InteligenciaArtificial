from simpleai.search import SearchProblem, hill_climbing, hill_climbing_stochastic, beam, hill_climbing_random_restarts, simulated_annealing
from simpleai.search.viewers import BaseViewer
import random, datetime, itertools

INICIAL = []
for fila in range(3):
    for columna in range(10):
        INICIAL.append((fila,columna))
INICIAL = tuple(INICIAL)

visor = BaseViewer()

# def colocar_rey(Estado_Inicial, posicion):
#     Estado_Inicial = t2l(Estado_Inicial)
#     Estado_Inicial[posicion[0]][posicion[1]] = 2
#     Estado_Inicial = l2t(Estado_Inicial)
#     return Estado_Inicial

def resolver(metodo_busqueda, iteraciones = None, haz=None, reinicios=None):

    diccionario_metodos_busqueda = {
        'hill_climbing': hill_climbing,
        'hill_climbing_stochastic': hill_climbing_stochastic,
        'beam': beam,
        'hill_climbing_random_restarts': hill_climbing_random_restarts,
        'simulated_annealing': simulated_annealing}

    if metodo_busqueda == 'beam':
        result = diccionario_metodos_busqueda[metodo_busqueda](HnefataflProblem(INICIAL), haz, iteraciones)
    elif metodo_busqueda == 'hill_climbing_random_restarts':
        result = diccionario_metodos_busqueda[metodo_busqueda](HnefataflProblem(INICIAL), reinicios, iteraciones)
    else:
        result = diccionario_metodos_busqueda[metodo_busqueda](HnefataflProblem(INICIAL),iterations_limit=iteraciones)
    return result




# def t2l(t):
#     return list(list(r) for r in t)
#
# def l2t(l):
#     return tuple(tuple(r) for r in l)

def CuantoSuma(posicion):
    punt = 0
    fila, columna = posicion
    if (fila == 0) or (columna == 0) or (fila == 9) or (columna == 9):
        punt = 3
    else:
        punt = 1
    return punt

class HnefataflProblem(SearchProblem):

    def actions(self, state):
        acciones = []
        estado = list(state)
        EstadosDesocupados = []
        for fila in range(10):
            for columna in range(10):
                if (fila,columna) not in estado:
                    EstadosDesocupados.append((fila,columna))
        for soldado in estado:
            for hueco in EstadosDesocupados:
                acciones.append((soldado,hueco))

        return tuple(acciones)

    def result(self, state, action):
        soldado, hueco = action[0], action[1]
        estado = list(state)
        estado.remove(soldado)
        estado.append(hueco)
        return tuple(estado)

    def value(self, state):
        puntaje = 0
        sumados = []
        estado = list(state)
        for sold1, sold2 in itertools.combinations(estado,2): #Todas las combinaciones
            f1, c1 = sold1
            f2, c2 = sold2
            if (abs(f1 - f2) + abs(c1 - c2)) == 2:
                if ((f1 == f2) | (c1 == c2)):
                    if f1 == f2:
                        porSumar = ((f1, ((c1 + c2) / 2)))
                    else:
                        porSumar = ((((f1 + f2) / 2), c2))
                else:
                    porSumar = (f1, c2)
                    porSumar2 = (f2, c1)
                    if porSumar2 not in sumados and porSumar2 not in estado:
                        sumados.append(porSumar2)
                if porSumar not in sumados and porSumar not in estado:
                    sumados.append(porSumar)
        for sold in sumados:
            puntaje += CuantoSuma(sold)
        return puntaje

    def generate_random_state(self):
        estado = []
        for soldado in range(30):
            posicion = ((random.randint(0, 9)),(random.randint(0, 9)))
            while posicion in estado:
                posicion = ((random.randint(0, 9)), (random.randint(0, 9)))
            estado.append(posicion)

        return tuple(estado)

    # def initial_state(self):
    #     state = []
    #     for fila in range(3):
    #         for columna in range(10):
    #             state.append((fila,columna))
    #     return tuple(state)


if __name__ == '__main__': #para que cunado lo importo no se mejecute.

    print 'AI...'

    # print 'Hora de inicio: ', datetime.datetime.now().time()
    # problem = resolver('hill_climbing')
    # print hill_climbing(HnefataflProblem(INICIAL), iterations_limit=5000).value

    # for i in range(10):
    #     problem = resolver('hill_climbing', 5000)
    #     print 'Puntaje obtenido:', problem.value
    #problem = resolver('hill_climbing', 500)
    #problem = simulated_annealing(HnefataflProblem(INICIAL),iterations_limit=100)

    #print 'Puntaje obtenido:', problem.value
    # print 'Hora de finalizacion: ', datetime.datetime.now().time()

    # print 'Hora de inicio: ', datetime.datetime.now().time()
    # problem = resolver('hill_climbing', 20)
    # print 'Hora de finalizacion: ', datetime.datetime.now().time()
    # #Imprime los 3 y los 1 donde corresponde
    # fila = ' _ _ _ _ _ _ _ _ _ _'
    # for f in range(10):
    #     print fila
    #     fila = '|'
    #     for c in range(10):
    #         if (f, c) in problem.state:
    #             fila = fila + 'X|'
    #         else:
    #             sumados = []
    #             estado = list(problem.state)
    #             for sold1, sold2 in itertools.combinations(estado, 2):  # Todas las combinaciones
    #                 f1, c1 = sold1
    #                 f2, c2 = sold2
    #                 if (abs(f1 - f2) + abs(c1 - c2)) == 2:
    #                     if ((f1 == f2) | (c1 == c2)):
    #                         if f1 == f2:
    #                             porSumar = ((f1, ((c1 + c2) / 2)))
    #                         else:
    #                             porSumar = ((((f1 + f2) / 2), c2))
    #                     else:
    #                         porSumar = (f1, c2)
    #                         porSumar2 = (f2, c1)
    #                         if porSumar2 not in sumados and porSumar2 not in estado:
    #                             sumados.append(porSumar2)
    #                     if porSumar not in sumados and porSumar not in estado:
    #                         sumados.append(porSumar)
    #             if (f,c) in sumados:
    #                 fila = fila +str(CuantoSuma((f,c)))+'|'
    #             else:
    #                 fila = fila + '_|'
    # print fila

    for i in range(10):
        print 'Hora de inicio: ', datetime.datetime.now().time()
        problem = resolver('beam',10,10)
        print 'Hora de finalizacion: ', datetime.datetime.now().time()
        print 'Puntaje obtenido:', problem.value
        fila = ' _ _ _ _ _ _ _ _ _ _'
        for f in range(10):
            print fila
            fila = '|'
            for c in range(10):
                if (f,c) in problem.state:
                    fila = fila + 'X|'
                else:
                    fila = fila + '_|'


    # print 'Inteligencia Artificial'
    #
    # # problem = resolver('hill_climbing')
    # # print hill_climbing(HnefataflProblem(INICIAL), iterations_limit=5000).value
    #
    # for i in range(10):
    #     print '\n'
    #     print 'Prueba', i + 1
    #     print 'Hora de inicio: ', datetime.datetime.now().time()
    #     problem = resolver('hill_climbing',20)
    #     print 'Puntaje obtenido:', problem.value
    #     print 'Hora de finalizacion: ', datetime.datetime.now().time()
    #     sumados = []
    #     estado = list(problem.state)
    #     for sold1, sold2 in itertools.combinations(problem.state, 2):  # Todas las combinaciones
    #         f1, c1 = sold1
    #         f2, c2 = sold2
    #         if (abs(f1 - f2) + abs(c1 - c2)) == 2:
    #             if ((f1 == f2) | (c1 == c2)):
    #                 if f1 == f2:
    #                     porSumar = ((f1, ((c1 + c2) / 2)))
    #                 else:
    #                     porSumar = ((((f1 + f2) / 2), c2))
    #             else:
    #                 porSumar = (f1, c2)
    #                 porSumar2 = (f2, c1)
    #                 if porSumar2 not in sumados and porSumar2 not in estado:
    #                     sumados.append(porSumar2)
    #             if porSumar not in sumados and porSumar not in estado:
    #                 sumados.append(porSumar)
    #     fila = ' _ _ _ _ _ _ _ _ _ _'
    #     for f in range(10):
    #         print fila
    #         fila = '|'
    #         for c in range(10):
    #             if (f,c) in problem.state:
    #                 fila = fila + 'X|'
    #             else:
    #                 if (f,c) in sumados:
    #                     if (f == 0) or (c == 0) or (f == 9) or (c == 9):
    #                         fila = fila + '3|'
    #                     else:
    #                         fila = fila + '1|'
    #                 else:
    #                     fila = fila + '_|'