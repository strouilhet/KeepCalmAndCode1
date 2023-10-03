from exercise1_1 import exercise1

def test_exercise1():
   assert exercise1(1,2,3)=="all different"
   assert exercise1(2,2,1)=="two equal"   
   assert exercise1(2,1,2)=="two equal" 
   assert exercise1(1,2,2)=="two equal" 
   assert exercise1(1,1,1)=="three equal"