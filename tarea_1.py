#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tarea_1.py
------------

Tarea de desarrollo de entornos y agentes
==========================================

1. Desarrolla un entorno similar al de los dos cuartos (el cual se
   encuentra en el módulo doscuartos_o.py), pero con tres cuartos en
   el primer piso, y tres cuartos en el segundo piso.
   
   El entorno se llamará `SeisCuartos`.

   Las acciones totales serán
   
   ```
   ["ir_Derecha", "ir_Izquierda", "subir", "bajar", "limpiar", "nada"]
   ``` 
    
   La acción de `"subir"` solo es legal en el piso de abajo, en los cuartos de los extremos, 
   mientras que la acción de `"bajar"` solo es legal en el piso de arriba y en el cuarto de el centro (dos
   escaleras para subir, una escalera para bajar).

   Las acciones de subir y bajar son mas costosas en término de
   energía que ir a la derecha y a la izquierda, por lo que la función
   de desempeño debe de ser de tener limpios todos los cuartos, con el
   menor numero de acciones posibles, y minimizando subir y bajar en
   relación a ir a los lados. El costo de limpiar es menor a los costos
   de cualquier acción.

2. Diseña un Agente reactivo basado en modelo para este entorno y
   compara su desempeño con un agente aleatorio despues de 100 pasos
   de simulación.

3. Al ejemplo original de los dos cuartos, modificalo de manera que el
   agente solo pueda saber en que cuarto se encuentra pero no sabe si
   está limpio o sucio.

   A este nuevo entorno llamalo `DosCuartosCiego`.

   Diseña un agente racional para este problema, pruebalo y comparalo
   con el agente aleatorio.

4. Reconsidera el problema original de los dos cuartos, pero ahora
   modificalo para que cuando el agente decida aspirar, el 80% de las
   veces limpie pero el 20% (aleatorio) deje sucio el cuarto. Igualmente, 
   cuando el agente decida cambiar de cuarto, se cambie correctamente de cuarto el 90% de la veces
   y el 10% se queda en su lugar. Diseña
   un agente racional para este problema, pruebalo y comparalo con el
   agente aleatorio.

   A este entorno llámalo `DosCuartosEstocástico`.

Todos los incisos tienen un valor de 25 puntos sobre la calificación de
la tarea.

"""
__author__ = 'Irving Francisco Borboa Gradias'

import entornos_o
from random import choice

class NueveCuartos(entornos_o.Entorno):
    
    def __init__(self, x0=["A", "primer_piso" ,"sucio", "sucio", "sucio"]):
        """
        Por default inicialmente el robot está en A y los tres cuartos
        están sucios

        """
        self.x = x0[:]
        self.desempeño = 0
        
    def acción_legal(self, acción):
        return acción in ("ir_Derecha", "ir_Izquierda",
                          "subir", "bajar", "limpiar", "nada")
        
    def transición(self, acción):
        if not self.acción_legal(acción):
            raise ValueError("La acción no es legal para este estado")
            
        robot, piso, a, b, c = self.x
        if acción is not "nada" or a is "sucio" or b is "sucio" or c is "sucio":
            self.desempeño -= 1
        if acción is "limpiar":
            self.x["  ABC".find(self.x[0])] = "limpio"
        elif acción is "ir_Derecha" and robot is "A" and piso is "primer_piso":
            self.x[0] = "B"
            self.desempeño -= 1
        elif acción is "ir_Derecha" and robot is "B" and piso is "primer_piso":
            self.x[0] = "C"
            self.desempeño -= 1
        elif acción is "subir" and robot is "C" and piso is "primer_piso":
            self.x[1] = "segundo_piso"
            self.desempeño -= 2
        
            
class AgenteAleatorio(entornos_o.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, percepcion):
        return choice(self.acciones)
            
    

# Requiere el modulo entornos_o.py
# Usa el modulo doscuartos_o.py para reutilizar código
# Agrega los modulos que requieras de python
