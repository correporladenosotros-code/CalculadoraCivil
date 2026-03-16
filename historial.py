# ============================================================
# HISTORIAL.PY - Almacena y gestiona los cálculos realizados
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE (cambia estos valores para ajustar historial)
LIMITE_HISTORIAL = 20  # ← Máximo de cálculos guardados en memoria


class Historial:
    # --------------------------------------------------------
    # __init__: Constructor de la clase Historial
    # registros: list → almacena diccionarios {"expresion": "...", "resultado": "..."}
    # limite: int → máximo de registros permitidos (por defecto LIMITE_HISTORIAL)
    # --------------------------------------------------------
    def __init__(self, limite=LIMITE_HISTORIAL):
        self.registros = []  # ← Lista vacía para almacenar cálculos
        self.limite = limite  # ← Límite máximo de registros
    
    # --------------------------------------------------------
    # agregar: Guarda un nuevo cálculo en el historial
    # expresion: str → expresión matemática ("5+3")
    # resultado: str → resultado calculado ("8.0")
    # Retorna: bool → True si se agregó, False si estaba vacío
    # --------------------------------------------------------
    def agregar(self, expresion, resultado):
        # Validar que no sean cadenas vacías o solo espacios
        if expresion.strip() and resultado.strip():
            # Crear diccionario con ambos valores
            registro = {
                "expresion": expresion,   # ← Ej: "5+3"
                "resultado": resultado    # ← Ej: "8.0"
            }
            
            # Añadir registro al final de la lista
            self.registros.append(registro)
            
            # Aplicar límite automáticamente (eliminar más antiguo si excede)
            self._aplicar_limite()
            
            return True  # ← Indicar éxito
        
        return False  # ← No se agregó (datos vacíos)
    
    # --------------------------------------------------------
    # _aplicar_limite: Método PRIVADO para mantener el límite de registros
    # Elimina el registro más antiguo si se excede el límite
    # --------------------------------------------------------
    def _aplicar_limite(self):
        # Verificar si excede el límite configurado
        if len(self.registros) > self.limite:
            # pop(0) elimina el PRIMER elemento (el más antiguo) → comportamiento FIFO
            self.registros.pop(0)
    
    # --------------------------------------------------------
    # obtener_todos: Devuelve COPIA de todos los registros
    # Retorna: list → copia de self.registros (protege datos internos)
    # --------------------------------------------------------
    def obtener_todos(self):
        # copy() evita que modifiquen la lista original desde fuera
        return self.registros.copy()
    
    # --------------------------------------------------------
    # obtener_ultimo: Devuelve el cálculo más reciente
    # Retorna: dict o None → último registro o None si está vacío
    # --------------------------------------------------------
    def obtener_ultimo(self):
        # Verificar que haya registros
        if self.registros:
            # [-1] accede al último elemento de la lista
            return self.registros[-1]
        
        return None  # ← Historial vacío
    
    # --------------------------------------------------------
    # limpiar: Borra TODOS los registros del historial
    # --------------------------------------------------------
    def limpiar(self):
        # clear() vacía la lista completamente (método nativo de Python)
        self.registros.clear()
    
    # --------------------------------------------------------
    # cantidad: Devuelve el número actual de registros
    # Retorna: int → cantidad de cálculos guardados
    # --------------------------------------------------------
    def cantidad(self):
        return len(self.registros)  # ← Contar elementos en la lista
    
    # --------------------------------------------------------
    # esta_vacio: Verifica si el historial no tiene registros
    # Retorna: bool → True si está vacío, False si tiene registros
    # --------------------------------------------------------
    def esta_vacio(self):
        return len(self.registros) == 0  # ← Comparar longitud con cero