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
        return None, f"TypeError: Operador '+' inválido entre Inteiro e {type(other).__name__}"

    def __sub__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value - other.value), None
        if isinstance(other, Float):
            return Float(float(self.value) - other.value), None
        return None, f"TypeError: Operador '-' inválido entre Inteiro e {type(other).__name__}"

    def __mul__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value * other.value), None
        if isinstance(other, Float):
            return Float(float(self.value) * other.value), None
        if isinstance(other, String): # Permite 3 * "a"
            return String(other.value * self.value), None
        return None, f"TypeError: Operador '*' inválido entre Inteiro e {type(other).__name__}"

    def __truediv__(self, other):
        if isinstance(other, (Integer, Float)):
            if other.value == 0:
                return None, "ZeroDivisionError: Divisão por zero"
            # Divisão sempre resulta em Float
            return Float(float(self.value) / float(other.value)), None
        return None, f"TypeError: Operador '/' inválido entre Inteiro e {type(other).__name__}"

class Float(Value):
    """Classe para representar um valor de ponto flutuante."""
    def __add__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value + float(other.value)), None
        return None, f"TypeError: Operador '+' inválido entre Float e {type(other).__name__}"

    def __sub__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value - float(other.value)), None
        return None, f"TypeError: Operador '-' inválido entre Float e {type(other).__name__}"

    def __mul__(self, other):
        if isinstance(other, (Integer, Float)):
            return Float(self.value * float(other.value)), None
        return None, f"TypeError: Operador '*' inválido entre Float e {type(other).__name__}"

    def __truediv__(self, other):
        if isinstance(other, (Integer, Float)):
            if other.value == 0:
                return None, "ZeroDivisionError: Divisão por zero"
            return Float(self.value / float(other.value)), None
        return None, f"TypeError: Operador '/' inválido entre Float e {type(other).__name__}"

class String(Value):
    """Classe para representar um valor de string."""
    def __add__(self, other):
        if isinstance(other, (Integer, Float, String)):
            return String(self.value + str(other.value)), None
        return None, f"TypeError: Operador '+' inválido entre String e {type(other).__name__}"

    def __mul__(self, other):
        if isinstance(other, Integer): # Permite "a" * 3
            return String(self.value * other.value), None
        return None, f"TypeError: Operador '*' inválido entre String e {type(other).__name__}"

    def __sub__(self, other):
        return None, f"TypeError: Operador '-' inválido para o tipo String"

    def __truediv__(self, other):
        return None, f"TypeError: Operador '/' inválido para o tipo String"