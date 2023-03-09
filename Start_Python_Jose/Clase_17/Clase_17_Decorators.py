import functools

user = {'username': 'Jose123', 'access_level': 'admin'}

#########  CREANDO UN DECORADOR SIMPLE #####################

"""
def user_has_permission(func): # creamos un decorador propio
    @functools.wraps(func) # con esto, le aclaramos al decorador donde aplicar y asi conservamos las caracteristicas de la funcion donde usamos el decorador
    def secure_func():
        if user.get('access_level') == "admin":
            return func()
        raise RuntimeError
    return secure_func


@user_has_permission
def my_function():
    return 'Password for admin panel is 1234'
"""

#########  CREANDO UN DECORADOR CON VARIABLE #####################

def user_has_permission(acces_level):
    def my_decorator(func): # creamos un decorador propio
        @functools.wraps(func) # con esto, le aclaramos al decorador donde aplicar y asi conservamos las caracteristicas de la funcion donde usamos el decorador
        def secure_func(*args, **kwargs):
            if user.get('access_level') == acces_level:
                return func(*args, **kwargs)
            raise RuntimeError
        return secure_func
    return my_decorator


@user_has_permission('admin') # este tipo de decorador nos permite agregar detalle a la operacion, en este caso, difinir el access level
def my_function(panel):
    return f'Password for {panel} panel is 1234'




# my_secure_function = user_has_permission(my_function) # esto ya no se necesita, ya que lo llamamos con @

print(my_function('Movies'))
print(my_function.__name__)