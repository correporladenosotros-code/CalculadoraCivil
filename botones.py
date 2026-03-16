# ============================================================
# BOTONES.PY - Crea y organiza todos los botones de la calculadora
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE - Colores (cambia estos valores para cambiar toda la paleta)
COLOR_NUMERO_FONDO = "#CFD8DC"    # ← Fondo botones numéricos (gris claro)
COLOR_NUMERO_TEXTO = "#000000"    # ← Texto botones numéricos (negro)
COLOR_OPERADOR_FONDO = "#90CAF9"  # ← Fondo botones operadores (+, -, *, /)
COLOR_OPERADOR_TEXTO = "#FFFFFF"  # ← Texto botones operadores (blanco)
COLOR_IGUAL_FONDO = "#4CAF50"     # ← Fondo botón "=" (verde)
COLOR_IGUAL_TEXTO = "#FFFFFF"     # ← Texto botón "=" (blanco)
COLOR_BORRAR_FONDO = "#F48FB1"    # ← Fondo botones "C" y "←" (rosa)
COLOR_BORRAR_TEXTO = "#FFFFFF"    # ← Texto botones "C" y "←" (blanco)

# ✏️ CONFIGURACIÓN EDITABLE - Tamaños y espaciado
ANCHO_BOTON = 72                  # ← Ancho de cada botón (px)
ALTO_BOTON = 72                   # ← Altura de botones normales (px)
ALTO_BOTON_IGUAL = 155            # ← Altura del botón "=" (ocupa 2 filas)
BORDER_RADIUS_BOTON = 16          # ← Redondeo de esquinas de los botones (px)
ESPACIADO_ENTRE_BOTONES = 10      # ← Espacio horizontal entre botones (px)
ESPACIADO_ENTRE_FILAS = 5        # ← Espacio vertical entre filas de botones (px)

# ✏️ CONFIGURACIÓN EDITABLE - Layout (posición de botones)
# Modifica el orden dentro de cada fila para reorganizar botones
# Fila 1: Botones de la primera fila (arriba)
FILA1_BOTONES = ["C", "←", "/", "*"]
# Fila 2: Botones de la segunda fila
FILA2_BOTONES = ["7", "8", "9", "-"]
# Fila 3: Botones de la tercera fila
FILA3_BOTONES = ["4", "5", "6", "+"]
# Fila 4: Botones de la cuarta fila (el "=" ocupa 2 filas verticalmente)
FILA4_BOTONES = ["1", "2", "3", "="]
# Fila 5: Botones de la quinta fila (el espacio vacío permite que "=" sobresalga)
FILA5_BOTONES = ["ESPACIO", "0", ".", "ESPACIO"]


import flet as ft  # ← Importar librería Flet


def crear_botones(page, al_presionar):
    # --------------------------------------------------------
    # ESTILOS REUTILIZABLES (diccionarios para evitar repetir código)
    # Cada estilo define apariencia para un tipo de botón
    # --------------------------------------------------------
    
    # Estilo para botones numéricos (0-9)
    ESTILO_NUMERO = {
        "bgcolor": COLOR_NUMERO_FONDO,   # ← Fondo desde configuración
        "color": COLOR_NUMERO_TEXTO,     # ← Texto desde configuración
        "width": ANCHO_BOTON,            # ← Ancho desde configuración
        "height": ALTO_BOTON,            # ← Altura desde configuración
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    # Estilo para botones de operadores (+, -, *, /)
    ESTILO_OPERADOR = {
        "bgcolor": COLOR_OPERADOR_FONDO,
        "color": COLOR_OPERADOR_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    # Estilo especial para botón "=" (más alto, color diferente)
    ESTILO_IGUAL = {
        "bgcolor": COLOR_IGUAL_FONDO,
        "color": COLOR_IGUAL_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON_IGUAL,  # ← Altura doble para ocupar 2 filas
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    # Estilo para botones de borrado ("C" y "←")
    ESTILO_BORRAR = {
        "bgcolor": COLOR_BORRAR_FONDO,
        "color": COLOR_BORRAR_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    # --------------------------------------------------------
    # FUNCIÓN AUXILIAR: Crea un botón reutilizable
    # texto: str → texto visible en el botón ("5", "+", "C", etc.)
    # valor: str → valor que se envía al callback (por defecto = texto)
    # estilo: dict → diccionario de estilo a aplicar
    # Retorna: ft.ElevatedButton → botón listo para usar
    # --------------------------------------------------------
    def boton(texto, valor=None, estilo=None):
        # Si no se especifica valor, usar el texto como valor
        if valor is None:
            valor = texto
        
        # Crear botón con ElevatedButton (botón elevado con sombra)
        return ft.ElevatedButton(
            text=texto,  # ← Texto visible en el botón
            on_click=lambda e: al_presionar(valor),  # ← Al hacer clic, llamar al callback con el valor
            **estilo  # ← Desempaquetar diccionario de estilo (bgcolor, color, width, etc.)
        )
    
    # --------------------------------------------------------
    # CREAR ESPACIO VACÍO (para mantener alineación cuando "=" ocupa 2 filas)
    # --------------------------------------------------------
    ESPACIO_VACIO = ft.Container(
        width=ANCHO_BOTON,   # ← Mismo ancho que un botón normal
        height=ALTO_BOTON,   # ← Misma altura que un botón normal
        opacity=0            # ← Totalmente transparente (invisible)
    )
    
    # --------------------------------------------------------
    # CREAR FILA 1: Botones "C", "←", "/", "*"
    # --------------------------------------------------------
    fila1_botones = []
    for btn_texto in FILA1_BOTONES:
        if btn_texto == "C" or btn_texto == "←":
            fila1_botones.append(boton(btn_texto, "C" if btn_texto == "C" else "borrar", ESTILO_BORRAR))
        elif btn_texto == "/" or btn_texto == "*":
            fila1_botones.append(boton(btn_texto, btn_texto, ESTILO_OPERADOR))
    
    fila1 = ft.Row(
        controls=fila1_botones,  # ← Lista de botones creados
        spacing=ESPACIADO_ENTRE_BOTONES,  # ← Espacio horizontal entre botones
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # ← Distribuir uniformemente
    )
    
    # --------------------------------------------------------
    # CREAR FILA 2: Botones "7", "8", "9", "-"
    # --------------------------------------------------------
    fila2_botones = []
    for btn_texto in FILA2_BOTONES:
        if btn_texto in ["7", "8", "9"]:
            fila2_botones.append(boton(btn_texto, btn_texto, ESTILO_NUMERO))
        elif btn_texto == "-":
            fila2_botones.append(boton(btn_texto, btn_texto, ESTILO_OPERADOR))
    
    fila2 = ft.Row(
        controls=fila2_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    # --------------------------------------------------------
    # CREAR FILA 3: Botones "4", "5", "6", "+"
    # --------------------------------------------------------
    fila3_botones = []
    for btn_texto in FILA3_BOTONES:
        if btn_texto in ["4", "5", "6"]:
            fila3_botones.append(boton(btn_texto, btn_texto, ESTILO_NUMERO))
        elif btn_texto == "+":
            fila3_botones.append(boton(btn_texto, btn_texto, ESTILO_OPERADOR))
    
    fila3 = ft.Row(
        controls=fila3_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    # --------------------------------------------------------
    # CREAR FILA 4: Botones "1", "2", "3", "="
    # --------------------------------------------------------
    fila4_botones = []
    for btn_texto in FILA4_BOTONES:
        if btn_texto in ["1", "2", "3"]:
            fila4_botones.append(boton(btn_texto, btn_texto, ESTILO_NUMERO))
        elif btn_texto == "=":
            fila4_botones.append(boton("=", "calcular", ESTILO_IGUAL))  # ← "=" ocupa 2 filas
    
    fila4 = ft.Row(
        controls=fila4_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    # --------------------------------------------------------
    # CREAR FILA 5: Botones "ESPACIO", "0", ".", "ESPACIO"
    # --------------------------------------------------------
    fila5_botones = []
    for btn_texto in FILA5_BOTONES:
        if btn_texto == "ESPACIO":
            fila5_botones.append(ESPACIO_VACIO)  # ← Espacio invisible
        elif btn_texto == "0":
            fila5_botones.append(boton("0", "0", ESTILO_NUMERO))
        elif btn_texto == ".":
            fila5_botones.append(boton(".", ".", ESTILO_NUMERO))
    
    fila5 = ft.Row(
        controls=fila5_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    # --------------------------------------------------------
    # DEVOLVER LISTA DE FILAS PARA QUE main.py LAS ENSAMBLE
    # --------------------------------------------------------
    return [fila1, fila2, fila3, fila4, fila5]