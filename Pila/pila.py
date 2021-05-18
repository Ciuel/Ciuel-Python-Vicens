class Pila:
    def __init__(self):
        """Inicia una lisa vacia para usarse como el cuerpo de la pila"""
        self._body=[]

    def push(self,x):
        """Toma un elemento y lo inserta en el primer lugar de la pila 
    Args:
        x (AnyType): x puede ser de cualquier tipo, ya que la pila usa una lista que es heterogenea
    """
        self._body.insert(0,x)

    def pop(self):
        """Devuelve el elemento de la cabecera de la pila osea el primero de la lista
    Returns:
        [AnyType]: [Puede ser de cualquier tipo, ya que la pila usa una lista que es heterogenea]
    """
        try:
            return self._body.pop(0)
        except IndexError:
            print("La pila está vacia, devuelvo un None")
            return None

    @property
    def body(self):
        """getter del body

      Returns:
          [list]: body, la lista que compone la pila
      """
        return self._body

    @body.setter
    def body(self, stack_in):
        """setter del body

      Args:
          stack_in ([list]): La lista que se almacenará  en body
      """
        if type(stack_in)==list:
            self._body=stack_in
        else:
            print("No es una pila, no se asigna")
