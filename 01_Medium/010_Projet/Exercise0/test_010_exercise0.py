from exercise0 import exercise0
import pytest

def test_exercise0():
   assert exercise0(-1)==0
   assert exercise0(0)==0
   assert exercise0(1)==1
   assert exercise0(10)==1+2+3+4+5+6+7+8+9+10