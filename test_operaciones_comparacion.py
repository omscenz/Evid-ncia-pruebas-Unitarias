import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales, no_son_iguales

class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor(self):
        self.assertTrue(es_mayor_que(5,3)) 
        
    def test_es_mayor2(self):
        self.assertFalse(es_mayor_que(3,9))

    def test_es_menor(self):
        self.assertTrue(es_menor_que(-2,6))
        #Probando un numero negativo.

    def test_es_menor2(self):
        self.assertFalse(es_menor_que(6,0))  
        #Probando el numero cero.  

    def test_mayor_igual(self):
        self.assertTrue(es_mayor_o_igual_que(0,-2))  

    def test_mayor_igual2(self):
        self.assertFalse(es_mayor_o_igual_que(4445623,4648566))

    def test_mayor_igual3(self):
        self.assertGreaterEqual(es_mayor_o_igual_que(1,1), 0)
        #Caso donde "a" y "b" son iguales. 

    def test_menor_igual4(self):
        self.assertFalse(es_mayor_o_igual_que(1.5, -1.4))   
        #Colocando intencionalmente un error.
        # self.assertFalse(es_mayor_o_igual_que(1.5, -1.4)) AssertionError: True is not false   
        #Identifico correctamente el error ya que esperaba un False y recibio un True.    

    def test_menor_igual(self):
        self.assertTrue(es_menor_o_igual_que(-6,-1)) 
        #Probando ambos numeros negativos.

    def test_menor_igual2(self):
        self.assertTrue(es_menor_o_igual_que(45, 5))
        #Otro error intencionado, probando que identifica correctamente la instancia dada
        #self.assertTrue(es_menor_o_igual_que(45, 5)) AssertionError: False is not true
        # Esto es correcto ya que 45 no es menor o igual que 5. 

    def test_menor_igual3(self):
        self.assertLessEqual(es_menor_o_igual_que(5,5), 1)

    def test_son_ig(self):
        self.assertEqual(3.3434,3.3434)

    def test_son_iguales_f(self):
        self.assertFalse(son_iguales(4, 5))       

    def test_no_son_ig(self):
        self.assertTrue(no_son_iguales(3,5))
        #Comprobando caso contrario, ambos numeros distintos.

    def test_no_son_iguales_f(self):
        self.assertFalse(no_son_iguales(7, 7))    


if __name__ == '__main__':
    unittest.main()
