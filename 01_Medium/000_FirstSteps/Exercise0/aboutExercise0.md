## Flask 1 : fournir une page avec "Keep Calm and Code"


Consignes :
- ouvrir un terminal,
- installer Flask : dans le terminal, taper la commande `C:/Users/trouilhe/AppData/Local/Microsoft/WindowsApps/python3.11.exe -m pip install flask`
NB : si python n'est pas accessible depuis le répertoire courant, donner le chemin complet. IL doit ressembler à `C:/Users/prenom.nom/AppData/Local/Microsoft/WindowsApps/python3.11.exe`
- se positionner dans le répoertoire contenant le fichier app.py : taper la commande  `cd .\000_FirstSteps\Exercise0\`
- lancer le programme "serveur" : taper la commande `python -m flask run` 

Les indications suivantes s'affichent :

 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

- ouvrir un navigateur et demander l'URL http://127.0.0.1:5000/  (ou http://localhost:5000/)
- regarder ce qui se passe dans le terminal : vous devez voir les requêtes de la forme  `127.0.0.1 - - [21/Nov/2023 08:24:05] "GET / HTTP/1.1" 200`
- arrêter le programme "serveur" (qui doit s'appeler app.py) : taper `Ctrl+C` dans le terminal