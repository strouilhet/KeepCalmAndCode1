from exercise101_1 import exercise1

def test_exercise1():
   assert exercise1(100, [0,0,0])=="impossible"
   assert exercise1(100, [0,0,5])=="voila 5 billets de 20, 0 billets de 10 et 0 pièces de 1"
   assert exercise1(100, [0,8,2])=="voila 2 billets de 20, 6 billets de 10 et 0 pièces de 1"
   assert exercise1(100, [20,5,2])=="voila 2 billets de 20, 5 billets de 10 et 10 pièces de 1"
   assert exercise1(100, [10,5,2])=="voila 2 billets de 20, 5 billets de 10 et 10 pièces de 1"
   assert exercise1(100, [8,5,2])=="impossible"