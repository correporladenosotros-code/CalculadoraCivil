# ============================================================
# LOGICA.PY - Motor matemático de la calculadora
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE (cambia estos valores para ajustar comportamiento)
MAX_LONGITUD_EXPRESION = 50  # ← Máximo de caracteres permitidos en la expresión


class Calculadora:
    # --------------------------------------------------------
    # __init__: Constructor de la clase Calculadora
    # Crea una nueva instancia con expresión y resultado vacíos
    # --------------------------------------------------------
    def __init__(self):
        self.expresion = ""      # ← Almacena lo que el usuario va escribiendo (ej: "5+3*2")
        self.resultado = ""      # ← Almacena el resultado final después de calcular
    
    # --------------------------------------------------------
    # agregar: Añade un valor (número u operador) a la expresión actual
    # valor: str → valor a agregar ("5", "+", ".", etc.)
    # Retorna: str → expresión actualizada para mostrar en pantalla
    # --------------------------------------------------------
    def agregar(self, valor):
        # Convertir valor a texto por seguridad (aunque ya debería ser str)
        valor_str = str(valor)
        
        # Limitar longitud máxima para evitar expresiones infinitas
        if len(self.expresion) < MAX_LONGITUD_EXPRESION:
            self.expresion += valor_str  # ← Concatenar nuevo valor al final
        
        return self.expresion  # ← Devolver expresión actualizada
    
    # --------------------------------------------------------
    # calcular: Evalúa la expresión matemática y devuelve el resultado
    # Retorna: str → resultado como texto ("8.0") o mensaje de error
    # --------------------------------------------------------
    def calcular(self):
        try:
            # eval() interpreta texto como código Python (ej: "5+3" → 8)
            # ¡CUIDADO! Solo seguro aquí porque es app privada sin entrada externa
            resultado_numerico = eval(self.expresion)
            
            # Convertir resultado a texto para mostrar
            self.resultado = str(resultado_numerico)
            
            # La expresión actual se convierte en el resultado (para continuar operando)
            self.expresion = self.resultado
            
            return self.resultado  # ← Devolver resultado
        
        except ZeroDivisionError:
            # Capturar división entre cero específicamente
            self.resultado = "Error: Div/0"
            self.expresion = ""  # ← Limpiar expresión tras error
            return self.resultado
        
        except:
            # Capturar cualquier otro error (sintaxis inválida, etc.)
            self.resultado = "Error"
            self.expresion = ""  # ← Limpiar expresión tras error
            return self.resultado
    
    # --------------------------------------------------------
    # borrar_ultimo: Elimina el último carácter de la expresión
    # Retorna: str → expresión actualizada después de borrar
    # --------------------------------------------------------
    def borrar_ultimo(self):
        # Verificar que haya algo que borrar (evitar error en cadena vacía)
        if self.expresion:
            # [:-1] toma toda la cadena excepto el último carácter
            self.expresion = self.expresion[:-1]
        
        return self.expresion  # ← Devolver expresión actualizada
    
    # --------------------------------------------------------
    # limpiar: Borra TODO (expresión y resultado)
    # Retorna: str → expresión vacía ("")
    # --------------------------------------------------------
    def limpiar(self):
        self.expresion = ""    # ← Resetear expresión
        self.resultado = ""    # ← Resetear resultado
        return self.expresion  # ← Devolver cadena vacía
    
    # --------------------------------------------------------
    # obtener_expresion: Devuelve la expresión actual SIN modificarla
    # Retorna: str → expresión actual
    # --------------------------------------------------------
    def obtener_expresion(self):
        return self.expresion  # ← Solo lectura, no modifica nada
    
    # --------------------------------------------------------
    # obtener_resultado: Devuelve el resultado actual SIN modificarlo
    # Retorna: str → resultado actual
    # --------------------------------------------------------
    def obtener_resultado(self):
        return self.resultado  # ← Solo lectura, no modifica nada