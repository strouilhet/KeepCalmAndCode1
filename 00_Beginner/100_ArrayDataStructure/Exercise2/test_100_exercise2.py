from exercise100_2 import exercise2

def test_exercise2():
   assert exercise2(0)==[0]
   assert exercise2(2)==[1,0]
   assert exercise2(7)==[1,1,1]
   assert exercise2(128)==[1,0,0,0,0,0,0]
   assert exercise2(127)==[1,1,1,1,1,1]