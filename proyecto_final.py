import math
import random

# ==============================================================================
# SECCIÓN 1: NUTRICIÓN Y CÁLCULOS BIOMÉTRICOS
# ==============================================================================

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

# ==============================================================================
# SECCIÓN 2: FUERZA, RENDIMIENTO Y GENERACIÓN DE RUTINAS
# ==============================================================================

def calcular_1rm(peso_cargado, repeticiones):
    """
    Estima la fuerza máxima teórica (1RM) utilizando la Fórmula de Epley.
    """
    if repeticiones == 1:
        return peso_cargado
    else:
        return peso_cargado * (1 + (repeticiones / 30))
    
def clasificar_fuerza():
    """
    Evalúa el nivel de fuerza relativa 
    comparando el 1RM estimado contra el peso corporal del usuario.
    """
    if peso_corporal <= 0:
        return "Sin clasificar (Registre su peso en la Opción 1)"
    
    ratio = rm_estimado / peso_corporal
    if ratio < 0.75:
        return "Principiante"
    elif ratio < 1.25:
        return "Intermedio"
    elif ratio < 1.75:
        return "Avanzado"
    else:
        return "Élite"
    
def generar_rutina_aleatoria():
    """
    Utiliza listas, random.shuffle() y manejo de cadenas 
    (.split() y .join()) para crear una rutina sugerida de entrenamiento.
    """
    ejercicios_base = "Press de Banca,Sentadilla Libre,Peso Muerto,Dominadas,Press Militar,Remo con Barra"
    # Convertimos la cadena separada por comas en una lista usando .split()
    lista_ejercicios = ejercicios_base.split(",")
    
    # Mezclamos aleatoriamente el orden de los ejercicios con shuffle()
    random.shuffle(lista_ejercicios)
    
    # Seleccionamos los primeros 4 ejercicios y los unimos con formato usando .join()
    rutina_del_dia = " -> ".join(lista_ejercicios[:4])
    print("\n--- RUTINA SUGERIDA DEL DÍA ---")
    print(f"Orden de ejecución: {rutina_del_dia}")

# ==============================================================================
# SECCIÓN 3: GESTIÓN DE HISTORIAL (LISTAS DE LISTAS) Y FUNCIONES PENDIENTES
# ==============================================================================
def mostrar_historial(historial):
    """
    Nueva funcionalidad (Avance 3): Recorre la lista de listas 'historial' 
    usando enumerate() para desplegar cada entrenamiento registrado.
    """
    print("\n--- HISTORIAL DE ENTRENAMIENTOS (SESIÓN ACTUAL) ---")
    if len(historial) == 0:
        print("Aún no hay entrenamientos registrados en esta sesión.")
        return

    # Cada elemento 'registro' es una sublista: [ejercicio, peso, reps, 1rm, nivel]
    for indice, registro in enumerate(historial):
        print(f"{indice + 1}. Ejercicio: {registro[0]} | Peso: {registro[1]} kg | "
              f"Reps: {registro[2]} | 1RM Est.: {registro[3]} kg ({registro[4]})")


def guardar_historial_entrenamiento():
    
    """
    Función pendiente: Guardará los registros diarios en un archivo local.
    """
    
def grafico_de_progreso():
    """
    Función pendiente: Generará reportes visuales del progreso del usuario.
    """

# ==============================================================================
# SECCIÓN 4: FUNCIÓN PRINCIPAL Y CONTROL DE FLUJO
# ==============================================================================
def main():
    # Lista para almacenar los datos del usuario:
    # (nombre, edad, peso, estatura, sexo, calorias_obj, lista_macros)
    perfil_usuario = []
    
    # lista de listas para almacenar varios registros de fuerza
    # (nombre_ejercicio, peso_cargado, repeticiones, rm_estimado, nivel_fuerza)
    historial_entrenamientos = []
    
    niveles_actividad = [
        ["Sedentario (poco o nada de ejercicio)", 1.2],
        ["Ligero (1-3 días/semana)", 1.375],
        ["Moderado (3-5 días/semana)", 1.55],
        ["Alto (6-7 días/semana)", 1.725]
    ]
    
    opcion = 0
    
    while opcion != 6:
        print("\n==============================================")
        print("        GESTOR DE RENDIMIENTO FÍSICO          ")
        print("==============================================")
        print("1. Registrar perfil y calcular nutrición")
        print("2. Calcular estimación de fuerza (1RM) y guardar")
        print("3. Ver historial de sesión / Eliminar último")
        print("4. Generar rutina aleatoria sugerida")
        print("5. Exportar datos / Reporte gráfico (Pendiente)")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opción (1-6): "))
        
        match opcion:
            case 1:
                print("REGISTRO DE DATOS Y NUTRICIÓN")
                nombre = input("Ingrese su nombre: ").strip().title()
                edad = int(input("Ingrese su edad en años: "))
                peso_usuario = float(input("Ingrese su peso actual en kg: "))
                estatura = float(input("Ingrese su estatura en cm: "))
                sexo = input("Ingrese su sexo biológico (M/F): ").strip().upper()

                print("\nSeleccione su nivel de actividad diaria:")
                for idx, nivel in enumerate(niveles_actividad):
                    print(f"{idx + 1}. {nivel[0]}")
                opcion_act = int(input("Opción (1-4): "))
                factor_actividad = niveles_actividad[opcion_act - 1][1]

                print("\nSeleccione su objetivo principal:")
                print("1: Definición")
                print("2: Mantenimiento")
                print("3: Volumen")
                objetivo = int(input("Opción: "))
                
                # Cálculos nutricionales
                bmr = calcular_bmr(peso_usuario, estatura, edad, sexo)
                tdee = calcular_tdee(bmr, factor_actividad)
                calorias_obj = round(calcular_calorias_objetivo(tdee, objetivo), 1)
                macros = calcular_macronutrientes(peso_usuario, calorias_obj)
                
                # Actualizamos la lista del perfil del usuario
                perfil_usuario = [nombre, edad, peso_usuario, estatura, sexo, calorias_obj, macros]
                
                print(f"\n¡Perfil actualizado para {perfil_usuario[0]}!")
                print(f"TMB: {round(bmr, 1)} kcal | TDEE: {round(tdee, 1)} kcal")
                print(f"Calorías Objetivo: {calorias_obj} kcal/día")
                print(f"Macros -> Proteína: {macros[0]}g | Carbohidratos: {macros[1]}g | Grasas: {macros[2]}g")
                
            case 2:
                print("\n--- CÁLCULO Y REGISTRO DE FUERZA (1RM) ---")
                # Uso de .strip() y .capitalize() para formatear el nombre del ejercicio
                ejercicio = input("Nombre del ejercicio (ej. Press banca): ").strip().capitalize()
                peso_cargado = float(input("Peso levantado (kg): "))
                repeticiones = int(input("Repeticiones realizadas: "))
                
                rm = calcular_1rm(peso_cargado, repeticiones)
                
                # Verificamos si existe peso registrado en perfil_usuario para clasificar fuerza
                peso_corp = perfil_usuario[2] if len(perfil_usuario) > 0 else 0.0
                nivel = clasificar_fuerza(rm, peso_corp)
                
                # Agregamos una sublista a la lista de listas 'historial_entrenamientos' con append()
                nuevo_registro = [ejercicio, peso_cargado, repeticiones, rm, nivel]
                historial_entrenamientos.append(nuevo_registro)
                
                print(f"\nResultado para {ejercicio}: 1RM estimado = {rm} kg | Nivel: {nivel}")
                print("Registro guardado en el historial de la sesión.")
                
            case 3:
                mostrar_historial(historial_entrenamientos)
                if len(historial_entrenamientos) > 0:
                    borrar = input("\n¿Desea eliminar el último registro guardado? (S/N): ").strip().upper()
                    if borrar == "S":
                        # Uso de .pop() para remover el último elemento de la lista de listas
                        eliminado = historial_entrenamientos.pop()
                        print(f"Se eliminó el registro de: {eliminado[0]} ({eliminado[3]} kg).")
            
            case 4:
                generar_rutina_aleatoria()

            case 5:
                guardar_historial_archivo(historial_entrenamientos)
                grafico_de_progreso(historial_entrenamientos)

            case 6:
                nombre_despedida = perfil_usuario[0] if len(perfil_usuario) > 0 else "Atleta"
                print(f"\nCerrando sesión. ¡Excelente entrenamiento, {nombre_despedida}!")

            case _:
                print("\nOpción no válida. Por favor intente de nuevo.")
            
main()       