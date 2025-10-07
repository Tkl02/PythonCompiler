class Value:
    """Classe base para todos os valores em nossa linguagem."""
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

class Integer(Value):
    """Classe para representar um valor inteiro."""
    def __add__(self, other):
        if isinstance(other, Integer): return Integer(self.value + other.value), None
        if isinstance(other, Float):
            result = float(self.value) + other.value
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '+' inválido entre Inteiro e {type(other).__name__}"

    def __sub__(self, other):
        if isinstance(other, Integer): return Integer(self.value - other.value), None
        if isinstance(other, Float):
            result = float(self.value) - other.value
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '-' inválido entre Inteiro e {type(other).__name__}"

    def __mul__(self, other):
        if isinstance(other, Integer): return Integer(self.value * other.value), None
        if isinstance(other, Float):
            result = float(self.value) * other.value
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        if isinstance(other, String): return String(other.value * self.value), None
        return None, f"TypeError: Operador '*' inválido entre Inteiro e {type(other).__name__}"

    def __truediv__(self, other):
        if isinstance(other, (Integer, Float)):
            if other.value == 0: return None, "ZeroDivisionError: Divisão por zero"
            result = float(self.value) / float(other.value)
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '/' inválido entre Inteiro e {type(other).__name__}"

class Float(Value):
    """Classe para representar um valor de ponto flutuante."""
    def __add__(self, other):
        if isinstance(other, (Integer, Float)):
            result = self.value + float(other.value)
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '+' inválido entre Float e {type(other).__name__}"

    def __sub__(self, other):
        if isinstance(other, (Integer, Float)):
            result = self.value - float(other.value)
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '-' inválido entre Float e {type(other).__name__}"

    def __mul__(self, other):
        if isinstance(other, (Integer, Float)):
            result = self.value * float(other.value)
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '*' inválido entre Float e {type(other).__name__}"

    def __truediv__(self, other):
        if isinstance(other, (Integer, Float)):
            if other.value == 0: return None, "ZeroDivisionError: Divisão por zero"
            result = self.value / float(other.value)
            if result % 1 == 0:
                return Integer(int(result)), None
            return Float(result), None
        return None, f"TypeError: Operador '/' inválido entre Float e {type(other).__name__}"

class String(Value):
    """Classe para representar um valor de string."""
    def __add__(self, other):
        if isinstance(other, (Integer, Float, String, Boolean)):
            return String(self.value + repr(other)), None
        return None, f"TypeError: Operador '+' inválido entre String e {type(other).__name__}"

    def __mul__(self, other):
        if isinstance(other, Integer): return String(self.value * other.value), None
        return None, f"TypeError: Operador '*' inválido entre String e {type(other).__name__}"

    def __sub__(self, other): return None, f"TypeError: Operador '-' inválido para o tipo String"
    def __truediv__(self, other): return None, f"TypeError: Operador '/' inválido para o tipo String"

class Boolean(Value):
    """Classe para representar um valor booleano."""
    def __repr__(self): return "true" if self.value else "false"
    def __add__(self, other): return None, f"TypeError: Operador '+' inválido para o tipo Booleano"
    def __sub__(self, other): return None, f"TypeError: Operador '-' inválido para o tipo Booleano"
    def __mul__(self, other): return None, f"TypeError: Operador '*' inválido para o tipo Booleano"
    def __truediv__(self, other): return None, f"TypeError: Operador '/' inválido para o tipo Booleano"