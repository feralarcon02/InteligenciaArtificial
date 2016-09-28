from simpleai.search import SearchProblem, hill_climbing, hill_climbing_stochastic, beam, hill_climbing_random_restarts, simulated_annealing
import random, datetime, itertools

INICIAL = []
for fila in range(3):
    for columna in range(10):
        INICIAL.append((fila,columna))
INICIAL = tuple(INICIAL)


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

    print '\n'
    print chr(27) + "[1;0m" + 'Inteligencia Artificial' + chr(27) + "[0m"
    Mayor = 0
    for i in range(10):
        print '\n'
        print chr(27) + "[1;0m" + 'Prueba' + chr(27) + "[0m", i + 1
        print 'Hora de inicio: ', datetime.datetime.now().time()
        inicio = datetime.datetime.now()
        problem = resolver('hill_climbing', 200)
        puntaje = problem.value
        print 'Puntaje obtenido:', chr(27) + "[1;42m", puntaje, chr(27) + "[0m"
        print 'Hora de finalizacion: ', datetime.datetime.now().time()
        fila = ' _ _ _ _ _ _ _ _ _ _'
        for f in range(10):
            print fila
            fila = '|'
            for c in range(10):
                if (f,c) in problem.state:
                    fila = fila + 'X|'
                else:
                    fila = fila + '_|'
        print fila
        fin = datetime.datetime.now()
        tiempo = fin - inicio
        print '\n'
        print chr(27) + "[4;0m" + 'Tiempo de procesamiento:' + chr(27) + "[0m", tiempo
        if puntaje > Mayor:
            Mayor = puntaje
    print '\n'
    print chr(27) + "[1;103m" + "La maxima puntuacion es: " + chr(27) + "[0m", Mayor