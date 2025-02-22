# main.py

# Importando o módulo de operações com números complexos
from variaveis_complexas.numeros_complexos import NumeroComplexo

def resolver_questao_1():
    """Exemplo de resolução de uma questão utilizando a classe NumeroComplexo"""
    
    z1 = NumeroComplexo(3, 4)  # número complexo z1 = 3 + 4i
    z2 = NumeroComplexo(1, 2)  # número complexo z2 = 1 + 2i
    
    # Operações entre z1 e z2
    soma = z1.soma(z2)
    subtracao = z1.subtracao(z2)
    multiplicacao = z1.multiplicacao(z2)
    divisao = z1.divisao(z2)
    
    # Exibindo os resultados
    print("Soma de z1 e z2:", soma)
    print("Subtração de z1 e z2:", subtracao)
    print("Multiplicação de z1 e z2:", multiplicacao)
    print("Divisão de z1 e z2:", divisao)
    
def resolver_questao_2():
    """Outro exemplo de resolução com a classe NumeroComplexo"""
    
    z1 = NumeroComplexo(-2, 2)  # número complexo z1 = -2 + 2i
    
    # Calculando a raiz quadrada de z1
    raiz = z1.raiz_quadrada()
    
    print(f"Raiz quadrada de {z1}: {raiz}")

if __name__ == "__main__":
    # Resolva questões e mostre resultados
    print("Resolvendo questões de Números Complexos:\n")
    
    # Exemplo de questões a serem resolvidas
    resolver_questao_1()
    print("\n---\n")
    resolver_questao_2()
