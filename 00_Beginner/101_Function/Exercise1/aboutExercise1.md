Soit un porte-monnaie contenant un certain nombre de pièces de 1€, de billets de 10€ et de 20€. <BR>
Écrire un fonction qui reçoit en paramètre la somme des achats d’un client (en euros – pas de centimes) et le porte-monnaie du client (une liste (nb pièces de 1€, nb billets de 10€, nb billets de 20€)).
La fonction retourne :
 - `montant insuffisant` si le montant du porte-monnaie est inférieur à la somme à payer
 - sinon, le rendu de monnaie sous la forme : `voila X billets de 20, Y billets de 10 et Z pièces de 1`.

Vous écrirez une première fonction `rendu(somme, tuple)` qui retourne le tuple `(nbBillets, resteARendre)` où nbBillets est le nombre de billets à rendre et resteARendre la somme qu'il reste à rendre. `tuple` contient la valeur des billets/pièces que l'on va rendre (20, 10 ou 1) et le nombre de billets/pièces disponibles dans le porte-monnaie.
Vous appellerez `rendu()` 3 fois dans la fonction `exercise2()` (pour les billets de 20€ puis pour les billets de 10€ et enfin pour les pièces de 1€).

