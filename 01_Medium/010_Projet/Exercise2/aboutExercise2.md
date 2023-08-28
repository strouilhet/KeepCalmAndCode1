Ecrire une application à 2 routes :
- localhost:5000/index.html : affiche une page avec un formulaire pour demander le login et le mot de passe.
- localhost:5000/devine.html : affiche une page avec un formulaire pour deviner un nombre entre 1 et 100 (choisi aléatoirement par l'application).

Pour cela, vous écrirez et utiliserez la fonction devine(propo, nb) qui retourne 0 si propo et nb sont identiques, -1 si propo < nb et 1 sinon.
propo est le nombre proposé par l'utilisateur et nb le nombre à deviner.