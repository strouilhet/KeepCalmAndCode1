from exercise1_2 import exercise2
import pytest

def test_exercise2():
   assert exercise2(0)==0
   assert exercise2(10)==10*0.5  
   assert exercise2(11)== 10*0.5+0.30
   assert exercise2(30)== 10*0.5+20*0.30
   assert exercise2(31)== 10*0.5+20*0.30+0.20

# amélioration : photocop >=0