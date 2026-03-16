# ============================================================
# MAIN.PY - Punto de entrada de la aplicación
# Conecta todos los módulos y gestiona el flujo de la app
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE - Dimensiones y estilo general
ANCHO_VENTANA = 360               # ← Ancho de la ventana/app (px)
ALTO_VENTANA = 150                # ← Altura total de la ventana/app (px)
TITULO_APP = "Calculadora Flet"   # ← Título que aparece en la barra de la ventana
COLOR_FONDO_APP = "#ECEFF1"       # ← Color de fondo general de la app
PADDING_GENERAL = 15              # ← Espacio alrededor de todo el contenido (px)
ESPACIO_SUPERIOR = 10             # ← Espacio entre borde superior y pantalla (px)
ESPACIO_ENTRE_PANTALLA_BOTONES = 15  # ← Espacio vertical entre pantalla y primer fila de botones


import flet as ft  # ← Importar librería Flet (interfaz gráfica)
from logica import Calculadora  # ← Importar motor matemático
from pantalla import crear_pantalla  # ← Importar creador de pantalla
from botones import crear_botones  # ← Importar creador de botones
from historial import Historial  # ← Importar gestor de historial


def main(page: ft.Page):
    # --------------------------------------------------------
    # CONFIGURAR PROPIEDADES DE LA PÁGINA (ventana/app)
    # --------------------------------------------------------
    page.title = TITULO_APP  # ← Establecer título de la ventana
    page.window_width = ANCHO_VENTANA  # ← Establecer ancho fijo
    page.window_height = ALTO_VENTANA  # ← Establecer altura fija
    page.window_resizable = False  # ← Bloquear redimensionamiento (diseño consistente)
    page.padding = PADDING_GENERAL  # ← Espacio alrededor del contenido principal
    page.bgcolor = COLOR_FONDO_APP  # ← Color de fondo de toda la ventana
    
    # --------------------------------------------------------
    # CREAR INSTANCIAS DE LOS MÓDULOS (el "cerebro" de la app)
    # --------------------------------------------------------
    calc = Calculadora()  # ← Crear instancia del motor matemático
    historial = Historial()  # ← Crear instancia del gestor de historial (usa límite por defecto)
    
    # --------------------------------------------------------
    # CREAR PANTALLA Y OBTENER REFERENCIAS PARA ACTUALIZARLA
    # crear_pantalla() devuelve 3 valores: contenedor, expresion, resultado
    # --------------------------------------------------------
    contenedor_pantalla, txt_expresion, txt_resultado = crear_pantalla(page)
    
    # --------------------------------------------------------
    # DEFINIR CALLBACK: Función que responde a presionar botones
    # valor: str → valor enviado por el botón ("5", "+", "calcular", etc.)
    # --------------------------------------------------------
    def al_presionar(valor):
        # CASO 1: Usuario presionó "=" (calcular resultado)
        if valor == "calcular":
            res = calc.calcular()  # ← Pedir resultado al motor matemático
            txt_expresion.value = ""  # ← Limpiar expresión después de calcular
            txt_resultado.value = res  # ← Mostrar resultado en pantalla
            
            # Guardar en historial SOLO si no es un error
            if not res.startswith("Error"):
                # Si expresión está vacía, usar resultado como expresión guardada
                expr_guardar = txt_resultado.value if txt_expresion.value == "" else calc.obtener_expresion()
                historial.agregar(expr_guardar, res)  # ← Guardar en historial
        
        # CASO 2: Usuario presionó "←" (borrar último carácter)
        elif valor == "borrar":
            calc.borrar_ultimo()  # ← Pedir al motor que borre último carácter
            txt_expresion.value = calc.obtener_expresion()  # ← Actualizar expresión en pantalla
            # Si quedó vacía, mostrar "0" en resultado
            if not txt_expresion.value:
                txt_resultado.value = "0"
        
        # CASO 3: Usuario presionó "C" (limpiar todo)
        elif valor == "C":
            calc.limpiar()  # ← Pedir al motor que limpie todo
            txt_expresion.value = ""  # ← Limpiar expresión visual
            txt_resultado.value = "0"  # ← Resetear resultado a "0"
        
        # CASO 4: Usuario presionó número u operador ("5", "+", ".", etc.)
        else:
            calc.agregar(valor)  # ← Pedir al motor que agregue el valor
            txt_expresion.value = calc.obtener_expresion()  # ← Actualizar expresión
            # Si expresión está vacía, mostrar "0"; si no, dejar resultado vacío temporalmente
            txt_resultado.value = "0" if calc.obtener_expresion() == "" else ""
        
        # REFRESCAR INTERFAZ: Sin esto, los cambios no se ven visualmente
        page.update()
    
    # --------------------------------------------------------
    # CREAR BOTONES Y PASARLES EL CALLBACK
    # crear_botones() recibe page y la función al_presionar
    # --------------------------------------------------------
    filas_botones = crear_botones(page, al_presionar)
    
    # --------------------------------------------------------
    # ENSAMBLAR LAYOUT COMPLETO (estructura vertical de la app)
    # ft.Column apila elementos verticalmente
    # --------------------------------------------------------
    layout = ft.Column(
        # Lista de controles a apilar: espacios + pantalla + más espacios + filas de botones
        controls=[
            ft.Container(height=ESPACIO_SUPERIOR),  # ← Espacio superior configurable
            contenedor_pantalla,  # ← La pantalla con expresión y resultado
            ft.Container(height=ESPACIO_ENTRE_PANTALLA_BOTONES),  # ← Espacio entre pantalla y botones
        ] + filas_botones,  # ← Concatenar las 5 filas de botones
        spacing=ESPACIADO_ENTRE_FILAS if 'ESPACIADO_ENTRE_FILAS' in globals() else 10,  # ← Espacio entre filas (fallback si no existe)
        alignment=ft.MainAxisAlignment.START,  # ← Alinear contenido desde arriba
        expand=True  # ← Expandirse para ocupar toda la ventana
    )
    
    # --------------------------------------------------------
    # AGREGAR LAYOUT A LA PÁGINA (¡hacer visible la app!)
    # --------------------------------------------------------
    page.add(layout)
    
    # --------------------------------------------------------
    # ESTADO INICIAL: Mostrar "0" al iniciar la app
    # --------------------------------------------------------
    txt_resultado.value = "0"  # ← Establecer valor inicial del resultado
    page.update()  # ← Refrescar interfaz para que se vea el "0"


# --------------------------------------------------------
# PUNTO DE ENTRADA: Ejecutar la app cuando se llama directamente
# --------------------------------------------------------
if __name__ == "__main__":
    ft.app(target=main)  # ← Iniciar aplicación Flet con la función main como punto de entrada