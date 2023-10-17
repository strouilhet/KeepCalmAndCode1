from exercise101_2 import *

def test_exercise2():
   assert motADecouvrir(["algo"])=="algo"
   assert crypterMot("algo")==['-','-','-','-']
   assert estDans("a","algo")==True
   assert estDans("b","algo")==False
   assert actualiserMotCrypte("a", "algo", ['-','-','-','-'])== ['a','-','-','-']
   assert motComplet(['a','l','g','o'])==True
   assert motComplet(['a','l','g','-'])==False
