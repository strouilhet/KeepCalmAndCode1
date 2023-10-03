from exercise1_3 import exercise3

def test_exercise3():
   assert exercise3("mmi", "web")=="Authorized"
   assert exercise3("tc", "web")=="Denied"
   assert exercise3("mmi", "http")=="Denied"
   assert exercise3("tc", "http")=="Denied"

# amélioration : 3 tentatives autorisées