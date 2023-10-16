Cet exercice utilise à la fois la sélection et la répétition.

Un nombre d'Armstrong est un nombre qui est égal à la somme de ses chiffres portés à la puissance du nombre de chiffres le composant.

En python, on utilise le signe ** pour indiquer une puissance. Par exemple 3**2 signifie 3 porté à la puissance 2. Cette valeur vaut donc 3*3 = 9.

Par exemple, le nombre 153 est composé de 3 chiffres : 1, 5 et 3. On doit donc porter ces 3 chiffres à la puissance 3, c'est-à-dire 1**3, 5**3 et 3**3 et faire leur somme.
<BR>
On a donc 1**3 + 5**3 + 3**3 = 153. On retrouve le nombre original 153 donc c'est un nombre d'Armstrong.
<BR><BR>
Écrire une fonction qui renvoie `True` si un nombre nb, passé en paramètre à la fonction, est un nombre d'Amstrong, `False` sinon.