from exercise10_1 import exercise1

def test_exercise1():
   assert exercise1(1)=="pas assez"
   assert exercise1(6)=="1 boîtes et 0 oeufs" or "1 boites et 0 oeufs"
   assert exercise1(14)=="2 boîtes et 2 oeufs" or "2 boites et 2 oeufs"
