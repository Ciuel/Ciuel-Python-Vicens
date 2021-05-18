import unittest
from pila import Pila


class TestPila(unittest.TestCase):

    def test_push(self):
        "Chequea que el elemento pusheado sea efectivamente el tope de la pila"
        y="2"
        x=1
        pila1=Pila()
        pila1.push(x)
        pila1.push(y)
        self.assertEqual(pila1.body[0],y)

    def test_pop(self):
        "Chequea que el elemento popeado sea efectivamente el tope anterior de la pila"
        pila1=Pila()
        pila1.body=[1,2,3]
        tope=pila1.body[0]
        salida=pila1.pop()
        self.assertEqual(tope,salida)
        
        pila1.body=[]
        salida=pila1.pop()
        self.assertEqual(None,salida)

    def test_array(self):
        "Chequea que el array de la pila solo puede tener listas"
        pila1 = Pila()
        pila1.body="aaaa"
        self.assertTrue(type(pila1.body)==list)
        pila1.body=(1,2,3)
        self.assertTrue(type(pila1.body)==list)
        pila1.body=[1,2,3]
        self.assertTrue(type(pila1.body)==list)
        

if __name__=="__main__":
    unittest.main()