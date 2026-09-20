import math

#Primera parte, la nutricion

def calcular_bmr(peso, estatura, edad, sexo):
    #Calcular tasa metabolica basal
    #Formula en hombres: TMB = (10 * peso) + (6.25 * estatura) - (5 * edad) + 5
    if sexo == "M" or sexo == "m":
        bmr = (10 * peso) + (6.25 * estatura) - (5 * edad) + 5
    #Formula en mujeres: TMB = bmr = (10 * peso) + (6.25 * estatura) - (5 * edad) - 161
    else:
        bmr = bmr = (10 * peso) + (6.25 * estatura) - (5 * edad) - 161
    return bmr   
    
def calcular_tdee(bmr, nivel_actividad):
    #Calcula el Gasto Energético Total Diario (TDEE)
    #Formula BMR * nivel de actividad
    return bmr * nivel_actividad

def calcular_calorias_objetivo(tdee, objetivo):
    """
    Ajusta el consumo calórico diario según la meta física seleccionada:
    1: Definición (déficit calórico)
    2: Mantenimiento
    3: Volumen (superávit calórico)
    """
    if objetivo == 1:
        calorias = tdee - 500
    elif objetivo == 3:
        calorias = tdee + 300
    else:
        calorias = tdee
    return calorias

def calcular_macronutrientes(peso, calorias_objetivo):

    #Calcula la distribución recomendada de proteínas, grasas y carbohidratos en gramos.

    proteina_g = peso * 2.0
    grasas_g = peso * 0.9
    
    # Las calorías restantes se asignan a carbohidratos (4 kcal por gramo)
    calorias_restantes = calorias_objetivo - ((proteina_g * 4) + (grasas_g * 9))
    carbohidratos_g = calorias_restantes / 4
    
    return proteina_g, carbohidratos_g, grasas_g

#Parte 2 fuerza y rendimiento

def calcular_1rm(peso_cargado, repeticiones):
    """
    Estima la fuerza máxima teórica (1RM) utilizando la Fórmula de Epley.
    """
    if repeticiones == 1:
        return peso_cargado
    else:
        return peso_cargado * (1 + (repeticiones / 30))
    
def clasificar_fuerza():
    pass

#parte 3 funciones pendientes
def guardar_historial_entrenamiento():
    
    """
    Función pendiente: Guardará los registros diarios en un archivo local.
    """
    
def grafico_de_progreso():
    """
    Función pendiente: Generará reportes visuales del progreso del usuario.
    """

#Paete 4: Almacenamiento de datos
def main():
    nombre = ""
    peso = 0.0
    opcion = 0
    
    while opcion != 5:
        print("GESTOR DE RENDIMIENTO FÍSICO")
        print("1. Registrar datos de perfil y calcular nutrición")
        print("2. Calcular estimación de fuerza (1RM)")
        print("3. Ver historial de progreso (Pendiente)")
        print("4. Generar reporte gráfico (Pendiente)")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción (1-5): "))
        
        match opcion:
            case 1:
                print("REGISTRO DE DATOS Y NUTRICIÓN")
                nombre = input("Ingrese su nombre: ")
                edad = int(input("Ingrese su edad en años: "))
                peso_usuario = float(input("Ingrese su peso actual en kg: "))
                estatura = float(input("Ingrese su estatura en cm: "))
                sexo = input("Ingrese su sexo biológico (M/F): ")

                print()
                print("Seleccione su nivel de actividad diaria:")
                print("1.2: Sedentario")
                print("1.375: Ligero")
                print("1.55: Moderado")
                print("1.725: Alto")
                actividad = float(input("Opción: "))

                print("\nSeleccione su objetivo principal:")
                print("1: Definición")
                print("2: Mantenimiento")
                print("3: Volumen")
                objetivo = int(input("Opción: "))
                
               