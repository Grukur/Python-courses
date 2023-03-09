

class Treu(TypeError): #se sugiere usar Exception en vez de TypeError, ya que es mas basico
    """
    Se puede usar para explcar de que trata la clase o funciones, etc
    """
    def __init__(self, message, code):
        super().__init__(f'error testing {code}: {message}')
        self.code = code

#raise ('Este es un error falso, jejeje', 500)


error_01 = Treu('Error grave, ayuda', 200)

print(error_01.__doc__)




