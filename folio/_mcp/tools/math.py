from sympy import sympify, solve, symbols, latex

def math_solver(expression: str):
    """solve mathematical expressions, equations, calculations, and numerical problems"""
    try:
        results = sympify(expression)
        if isinstance(results, (list, tuple)):
            return {
                        "expression": expression,
                        "result" : str(results)
                    }
        
        return {
            "expression": expression,
            "result" : str(results.evalf())
        }
    except Exception as e:
        return f"> Math solver failed: {str(e)}"

