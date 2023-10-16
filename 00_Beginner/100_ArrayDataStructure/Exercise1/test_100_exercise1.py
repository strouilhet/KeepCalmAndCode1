from exercise100_1 import exercise1

def test_exercise1():
   assert exercise1(0)==[]
   assert exercise1(1)==[1]
   assert exercise1(12)==[2,1]
   assert exercise1(123)==[3,2,1]
   assert exercise1(1234)==[4,3,2,1]