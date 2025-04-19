import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import math

def probabilidade_binomial(n, p, k):
    """
    Calcula a probabilidade de exatamente k sucessos em n tentativas
    com probabilidade de sucesso p.
    
    Parâmetros:
    n - número de tentativas
    p - probabilidade de sucesso em cada tentativa (0 <= p <= 1)
    k - número de sucessos desejado
    
    Retorna:
    Probabilidade P(X = k)
    """
    combinacao = math.comb(n, k)
    return combinacao * (p ** k) * ((1 - p) ** (n - k))

def distribuicao_binomial(n, p):
    """
    Gera e plota a distribuição binomial para n tentativas e probabilidade p.
    
    Parâmetros:
    n - número de tentativas
    p - probabilidade de sucesso
    """
    # Valores possíveis de k (0 a n)
    k_values = np.arange(0, n+1)
    
    # Calcula as probabilidades para cada k
    probabilidades = [probabilidade_binomial(n, p, k) for k in k_values]
    
    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(k_values, probabilidades, color='skyblue', edgecolor='black')
    
    # Configurações do gráfico
    plt.title(f'Distribuição Binomial (n={n}, p={p})')
    plt.xlabel('Número de Sucessos (k)')
    plt.ylabel('Probabilidade')
    plt.xticks(k_values)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

def probabilidade_acumulada(n, p, k_min, k_max=None):
    """
    Calcula a probabilidade acumulada entre k_min e k_max.
    Se k_max não for fornecido, calcula P(X <= k_min).
    
    Parâmetros:
    n - número de tentativas
    p - probabilidade de sucesso
    k_min - mínimo número de sucessos
    k_max - máximo número de sucessos (opcional)
    
    Retorna:
    Probabilidade acumulada
    """
    if k_max is None:
        return sum(probabilidade_binomial(n, p, k) for k in range(0, k_min + 1))
    else:
        return sum(probabilidade_binomial(n, p, k) for k in range(k_min, k_max + 1))

def simular_binomial(n, p, num_simulacoes=1000):
    """
    Simula experimentos binomiais e plota um histograma dos resultados.
    
    Parâmetros:
    n - número de tentativas por experimento
    p - probabilidade de sucesso
    num_simulacoes - número de experimentos a simular
    """
    # Simula os experimentos
    resultados = np.random.binomial(n, p, num_simulacoes)
    
    # Cria o histograma
    plt.figure(figsize=(10, 6))
    plt.hist(resultados, bins=np.arange(-0.5, n+1.5, 1), density=True, 
             color='lightgreen', edgecolor='black', alpha=0.7)
    
    # Adiciona a distribuição teórica para comparação
    k_values = np.arange(0, n+1)
    prob_teorica = [probabilidade_binomial(n, p, k) for k in k_values]
    plt.plot(k_values, prob_teorica, 'ro-', label='Distribuição Teórica')
    
    # Configurações do gráfico
    plt.title(f'Simulação Binomial (n={n}, p={p}, {num_simulacoes} simulações)')
    plt.xlabel('Número de Sucessos')
    plt.ylabel('Frequência Relativa')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

# Exemplo de uso:
if __name__ == "__main__":
    n = 20  # Número de tentativas
    p = 0.3  # Probabilidade de sucesso
    
    # 1. Mostrar a distribuição binomial
    print("Distribuição Binomial:")
    distribuicao_binomial(n, p)
    
    # 2. Calcular probabilidade específica
    k = 5
    prob = probabilidade_binomial(n, p, k)
    print(f"\nProbabilidade de exatamente {k} sucessos: {prob:.4f} ou {prob*100:.2f}%")
    
    # 3. Calcular probabilidade acumulada
    k_min, k_max = 3, 7
    prob_acum = probabilidade_acumulada(n, p, k_min, k_max)
    print(f"\nProbabilidade de entre {k_min} e {k_max} sucessos: {prob_acum:.4f} ou {prob_acum*100:.2f}%")
    
    # 4. Simulação
    print("\nExecutando simulação...")
    simular_binomial(n, p, 5000)