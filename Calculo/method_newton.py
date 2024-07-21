def newton_method(f, df, x0, tol=1e-7, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar as raízes de uma equação.
    
    Parâmetros:
    f: Função da qual queremos encontrar a raiz.
    df: Derivada da função f.
    x0: Valor inicial para o método.
    tol: Tolerância para o critério de parada.
    max_iter: Número máximo de iterações.
    
    Retorna:
    A raiz encontrada ou uma mensagem de erro se o método não convergir.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            raise ValueError("Derivada zero. O método de Newton falhou.")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    raise ValueError("Máximo de iterações alcançado. O método de Newton não convergiu.")

# Exemplo de uso
if __name__ == "__main__":
    # Definindo a função e sua derivada
    def f(x):
        return x**2 - 2
    
    def df(x):
        return 2 * x
    
    # Valor inicial
    x0 = 1.0
    
    # Calculando a raiz
    try:
        raiz = newton_method(f, df, x0)
        print(f"A raiz encontrada é: {raiz}")
    except ValueError as e:
        print(e)
