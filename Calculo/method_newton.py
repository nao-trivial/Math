def newton_method(f, df, x0, tol=1e-7, max_iter=1000):
    """
    Implementa o método de Newton-Raphson para encontrar as raízes de uma função.
    
    Parâmetros:
    f : função
        A função para a qual queremos encontrar a raiz.
    df : função
        A derivada da função f.
    x0 : float
        Ponto inicial para a iteração.
    tol : float, opcional
        Tolerância para o critério de parada (default é 1e-7).
    max_iter : int, opcional
        Número máximo de iterações (default é 1000).
    
    Retorna:
    float
        A aproximação da raiz.
    """
