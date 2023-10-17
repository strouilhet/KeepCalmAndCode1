# le jeu du pendu
Vous arrivez au dernier exercice de la partie Beginner.
Il s'agit d'écrire le jeu du pendu à l'aide de plusieurs fonctions. Le programme est ainsi modulaire, le code est factorisé et évolutif.

Le but du jeu est de trouver un mot en ne connaissant que le nombre de lettres.

À chaque tour de jeu, le joueur doit proposer une lettre de l'alphabet (pour simplifier on supposera que le mot ne contient que des lettres en minuscules : pas d'accent, pas d'espace, pas de tiret, ...).

Si la lettre est dans le mot, on affichera alors toutes les occurences de cette lettre à leur place respective.

Mot à trouver : \_ \_ \_ \_  (donc 4 lettres)<br>
*-Proposition : 'a' -> présent*<br>
Mot à trouver : a \_ \_ \_<br>
*-Proposition : 'b' -> pas présent*<br>
*-Proposition : 'l' -> présent*<br>
Mot à trouver : a l \_ \_<br>
*-Proposition : 'o' -> présent<br>*
Mot à trouver : a l \_ o<br>
*-Proposition : 'g' -> présent<br>*
Mot à trouver : a l g o<br>
==> trouvé !

### Choix du mot à découvrir
— Écrire la fonction `motADecouvrir` qui choisit au hasard un mot dans un tableau de mots ; la fonction doit pouvoir s'exécuter avec divers tableaux, pas toujours le même.

### Mot crypé
— Écrire la fonction `crypterMot` qui prend en paramètre un mot et renvoie un tableau de caractères contenant autant de '_' que de lettres dans le mot

*Par exemple,<br>*
  *mot = "algo" --> mot crypté = ['\_', '\_', '\_', '\_']*


### Une lettre dans un mot ?
— Écrire la fonction `estDans` qui retourne vrai si la lettre est dans le mot.

*Par exemple,<br>*
  *estDans('a',"algo") --> vrai<br>*
  *estDans('b',"algo") --> faux<br>*

### Actualiser le mot crypté
— Écrire la fonction `actualiserMotCrypte` qui modifie le mot crypté en faisant apparaître toutes les occurrences d'une lettre.

*Par exemple,<br>*
  *mot crypté = ['\_', '\_', '\_', '\_'] <br>*
  *actualiserMotCrypte( 'a', motCrypte, "algo" )<br>*
     *--> mot crypté = ['a', '\_', '\_', '\_'] <br>*

### Mot trouvé ?
— Écrire la fonction `motComplet` qui indique si le mot a été trouvé (ou encore si le mot crypté ne contient plus aucun '\_')

### Lettre au hasard
— Écrire la fonction `lettreHasard` qui renvoie une lettre de l'alphabet au hasard.

### Afficher mot crypte
— Écrire la fonction `afficherMotCrypte` qui affiche à l'écran le mot crypté.

### Jouer une partie au hasard
— Écrire la fonction `jouerPartieHasard` qui joue une partie, c'est à dire :<br>
1- choisir un mot dans un tableau de mots<br>
2- construire le mot crypté<br>
3- choisir une lettre de l'alphabet au hasard<br>
4- tester si cette lettre est dans le mot<br>
5- si oui actualiser le mot crypté<br>
6- si le mot crypté n'est pas complet alors revenir à l'étape 3<br>
7- afficher le nb d'essais qui ont été necessaires pour trouver le mot<br>

### Jouer une partie interactive
— Écrire la fonction `jouerPartieInteractive` qui joue une partie, mais en demandant à l'utilisateur de saisir les caractères un par un.
