'''
Juego de piedra, papel o tijera

Integrantes:
Vicente Garay
Vicente Garcia
Felipe Gonzales
Andres Guerra
Tomas Loyola
'''


#Librerias importadas
import random

import os, sys

#Variables globales
acciones_posibles = ["piedra", "papel", "tijera"]

def cleaning():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')

#Procedimiento para saber el ganador

def ganador(accion_usuario,accion_computadora):
  
  if accion_usuario=="piedra":
    if accion_computadora=="piedra":
      print("Es un empate")
    if accion_computadora =="papel":
      print("La computadora ha ganado")
    if accion_computadora=="tijera":
      print("Usted ha ganado")

  if accion_usuario=="papel":
    if accion_computadora=="papel":
      print("Es un empate")
    if accion_computadora =="tijera":
      print("La computadora ha ganado")
    if accion_computadora=="piedra":
      print("Usted ha ganado")

  if accion_usuario=="tijera":
    if accion_computadora=="tijera":
      print("Es un empate")
    if accion_computadora =="piedra":
      print("La computadora ha ganado")
    if accion_computadora=="papel":
      print("Usted ha ganado")


#Procedimiento para comparar ambas opciones
def comparacion_resultados(accion_usuario,accion_computadora):
  print("")
  print("Resultados")
  print("")
  print(f"Tu escogiste {accion_usuario}, la computadora eligio {accion_computadora}.\n")
  ganador(accion_usuario,accion_computadora)

#Funcion (ya que esta si retorna algo) para saber la opcion del computador
def eleccion_computadora():
  accion_computadora = random.choice(acciones_posibles)
  return accion_computadora

#Procedimiento para elegir la opcion con la que se jugara
def elegir_opcion():
  accion_usuario = input("Ingresa una opción: (piedra, papel, tijera):")
  accion_computadora=eleccion_computadora()
  comparacion_resultados(accion_usuario,accion_computadora)


#Procedimiento para preguntarle el nombre al usuario
def preguntar_nombre():
  print("")
  nombre = input("Primero ingresa tu nombre: ")
  cleaning()
  print("")
  print(f"Hola {nombre}!, bienvenido al juego de piedra, papel o tijera \n")

#Procedimiento que inicia el juego
def iniciar_juego():
  elegir_opcion()

#Procedimiento para el menu
def menu():
  Bandera=False
  while (Bandera!=True):
    print("")
    print("\033[;36m"+"Bienvenido al juego de piedra, papel o tijera")
    print("")
    print("1. Iniciar juego")
    print("2. Salir del juego")
    print("")
    opcion=int(input("Seleccione una opcion:"))
    if opcion==1:
      cleaning()
      jugar="si"
      preguntar_nombre()
      while jugar=="si":
        iniciar_juego()
        print("")
        jugar=input("jugar otra ? (si/no): ")
        cleaning()

    if opcion==2:
      Bandera=True

#Aqui empieza todo
menu()


