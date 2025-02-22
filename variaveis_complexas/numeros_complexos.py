import cmath
import math

class NumeroComplexo:
    def __init__(self, real, imaginario):
        """Inicializa um número complexo da forma a + bi"""
        self.real = real
        self.imaginario = imaginario
        self.numero = complex(real, imaginario)  # Usando a classe complex do Python

    def __str__(self):
        """Representação do número complexo em formato a + bi"""
        return f"{self.real} + {self.imaginario}i"

    def modulo(self):
        """Retorna o módulo (magnitude) do número complexo"""
        return abs(self.numero)

    def argumento(self):
        """Retorna o argumento (ângulo) do número complexo"""
        return math.atan2(self.imaginario, self.real)

    def forma_polar(self):
        """Retorna o número complexo na forma polar r * e^(iθ)"""
        r = self.modulo()
        theta = self.argumento()
        return f"{r} * e^(i{theta})"

    def soma(self, outro):
        """Soma dois números complexos"""
        return NumeroComplexo(self.real + outro.real, self.imaginario + outro.imaginario)

    def subtracao(self, outro):
        """Subtrai dois números complexos"""
        return NumeroComplexo(self.real - outro.real, self.imaginario - outro.imaginario)

    def multiplicacao(self, outro):
        """Multiplica dois números complexos"""
        resultado = self.numero * outro.numero
        return NumeroComplexo(resultado.real, resultado.imag)

    def divisao(self, outro):
        """Divide dois números complexos"""
        if outro.numero == 0:
            raise ValueError("Não é possível dividir por zero.")
        resultado = self.numero / outro.numero
        return NumeroComplexo(resultado.real, resultado.imag)

    def raiz_quadrada(self):
        """Retorna a raiz quadrada do número complexo"""
        resultado = cmath.sqrt(self.numero)
        return NumeroComplexo(resultado.real, resultado.imag)

# Exemplo de uso
z1 = NumeroComplexo(3, 4)
z2 = NumeroComplexo(1, 2)

# Operações
print(f"z1: {z1}")
print(f"z2: {z2}")
print(f"Módulo de z1: {z1.modulo()}")
print(f"Argumento de z1: {z1.argumento()} rad")
print(f"Forma polar de z1: {z1.forma_polar()}")
print(f"Soma de z1 e z2: {z1.soma(z2)}")
print(f"Subtração de z1 e z2: {z1.subtracao(z2)}")
print(f"Multiplicação de z1 e z2: {z1.multiplicacao(z2)}")
print(f"Divisão de z1 e z2: {z1.divisao(z2)}")
print(f"Raiz quadrada de z1: {z1.raiz_quadrada()}")
