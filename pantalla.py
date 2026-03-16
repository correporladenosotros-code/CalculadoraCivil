# ============================================================
# PANTALLA.PY - Crea y gestiona la pantalla de la calculadora
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE (cambia estos valores para ajustar la pantalla)
COLOR_FONDO_PANTALLA = "#81C4F1"        # ← Color de fondo de la pantalla (gris claro)
COLOR_TEXTO_EXPRESION = "#455A64"       # ← Color del texto de la expresión (gris azulado)
COLOR_TEXTO_RESULTADO = "#000000"       # ← Color del texto del resultado (negro)
TAMANO_FUENTE_EXPRESION = 40            # ← Tamaño de fuente de la expresión (px)
TAMANO_FUENTE_RESULTADO = 40            # ← Tamaño de fuente del resultado (px)
ALTURA_PANTALLA = 150                   # ← Altura fija de la pantalla (px)
PADDING_INTERNO_PANTALLA = 25           # ← Espacio interior de la pantalla (px)
BORDER_RADIUS_PANTALLA = 24             # ← Redondeo de esquinas (px)
ESPACIO_ENTRE_TEXTOS = 5                # ← Espacio vertical entre expresión y resultado (px)


import flet as ft  # ← Importar librería Flet para crear componentes visuales


def crear_pantalla(page):
    # --------------------------------------------------------
    # CREAR TEXTO PARA LA EXPRESIÓN (ej: "5+3*2")
    # --------------------------------------------------------
    expresion = ft.Text(
        value="",  # ← Valor inicial vacío (se actualizará al presionar botones)
        size=TAMANO_FUENTE_EXPRESION,  # ← Tamaño de fuente editable desde configuración
        color=COLOR_TEXTO_EXPRESION,   # ← Color editable desde configuración
        text_align=ft.TextAlign.RIGHT,  # ← Alinear texto a la derecha (como calculadora real)
        expand=True,  # ← Expandirse para ocupar espacio disponible horizontalmente
        max_lines=1,  # ← Forzar una sola línea (evitar saltos de línea)
        overflow=ft.TextOverflow.FADE  # ← Si texto es muy largo, desvanecer suavemente (no cortar)
    )
    
    # --------------------------------------------------------
    # CREAR TEXTO PARA EL RESULTADO (ej: "16.0")
    # --------------------------------------------------------
    resultado = ft.Text(
        value="0",  # ← Valor inicial "0" (como calculadora física al encender)
        size=TAMANO_FUENTE_RESULTADO,  # ← Tamaño grande para mejor legibilidad
        weight=ft.FontWeight.BOLD,     # ← Negrita para destacar el resultado
        color=COLOR_TEXTO_RESULTADO,   # ← Color negro para máximo contraste
        text_align=ft.TextAlign.RIGHT,  # ← Alinear a la derecha
        expand=True,  # ← Expandirse horizontalmente
        max_lines=1,  # ← Una sola línea
        overflow=ft.TextOverflow.FADE  # ← Desvanecer si es muy largo
    )
    
    # --------------------------------------------------------
    # CREAR CONTENEDOR QUE ENVUELVE AMBOS TEXTOS (la "pantalla física")
    # --------------------------------------------------------
    contenedor = ft.Container(
        # Columna vertical que apila expresión arriba y resultado abajo
        content=ft.Column(
            controls=[expresion, resultado],  # ← Lista de controles a apilar
            spacing=ESPACIO_ENTRE_TEXTOS,    # ← Espacio vertical entre los dos textos
            alignment=ft.MainAxisAlignment.END,  # ← Empujar contenido hacia la parte inferior
            expand=True  # ← Expandirse verticalmente dentro del contenedor
        ),
        bgcolor=COLOR_FONDO_PANTALLA,  # ← Fondo gris claro (editable desde configuración)
        border_radius=BORDER_RADIUS_PANTALLA,  # ← Esquinas redondeadas (look moderno)
        padding=PADDING_INTERNO_PANTALLA,      # ← Espacio interior para que el texto "respire"
        height=ALTURA_PANTALLA,                # ← Altura fija controlada (no depende de expand)
        alignment=ft.alignment.center_right    # ← Alinear contenido a la derecha dentro del contenedor
    )
    
    # --------------------------------------------------------
    # DEVOLVER REFERENCIAS PARA QUE main.py PUEDA ACTUALIZARLOS
    # contenedor → para insertar en el layout
    # expresion → para cambiar su valor desde main.py
    # resultado → para cambiar su valor desde main.py
    # --------------------------------------------------------
    return contenedor, expresion, resultado