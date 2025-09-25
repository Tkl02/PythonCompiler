class Value:
    """Classe base para todos os valores em nossa linguagem."""
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

class Integer(Value):
    """Classe para representar um valor inteiro."""
    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value), None
        if isinstance(other, Float):
            return Float(float(self.value) + other.value), None
        return None, f"TypeError: Não é possível somar Inteiro com {type(other).__name__}"

    def __sub__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value - other.value), None
        if isinstance(other, Float):
            return Float(float(self.value) - other.value), None
        return None, f"TypeError: Não é possível subtrair {type(other).__name__} de Inteiro"

    # Implemente __mul__ e __div__ de forma similar...

class Float(Value):
    """Classe para representar um valor de ponto flutuante."""
    def __add__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value + float(other.value)), None
        return None, f"TypeError: Não é possível somar Float com {type(other).__name__}"

    def __sub__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value - float(other.value)), None
        return None, f"TypeError: Não é possível subtrair {type(other).__name__} de Float"

    # Implemente __mul__ e __div__ de forma similar...

class String(Value):
    """Classe para representar um valor de string."""
    def __add__(self, other):
        if isinstance(other, String):
            return String(self.value + other.value), None
        if isinstance(other, (Integer, Float)):
            return String(self.value + str(other.value)), None
        return None, f"TypeError: Não é possível concatenar String com {type(other).__name__}"