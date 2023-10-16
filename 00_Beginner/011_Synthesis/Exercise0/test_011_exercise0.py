from exercise11_0 import exercise0

def test_exercise0():
   assert exercise0(1,1,2020)=="10 ans 0 mois 0 jours"
   assert exercise0(2,1,2020)=="9 ans 11 mois 30 jours"
   assert exercise0(31,12,2020)=="9 ans 0 mois 1 jours"
   assert exercise0(31,12,2019)=="10 ans 0 mois 1 jours"
   assert exercise0(31,11,2019)=="10 ans 1 mois 1 jours"