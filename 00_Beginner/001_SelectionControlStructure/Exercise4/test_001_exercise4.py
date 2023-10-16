from exercise1_4 import exercise4

def test_exercise4():
   assert exercise4(2100)==False
   assert exercise4(2000)==True
   assert exercise4(2016)==True  
   assert exercise4(2024)==True 

# amélioration : vérifier que an est positif