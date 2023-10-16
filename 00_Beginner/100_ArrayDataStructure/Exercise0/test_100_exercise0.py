from exercise100_0 import exercise0

def test_exercise0():
   assert exercise0([])==0
   assert exercise0([1,2,3])==1+2+3
   assert exercise0([-1, -1, -1, -1, -1])==-5