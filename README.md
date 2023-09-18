# Exercice de workflow collaboratif Gitlab/Github

Cet exercise se déroule en binôme et consiste à mettre en ligne sur un répertoire git un tweet à l'aide d'une pull request.

La première étape consiste à fork (fourcher) ce répertoire, puis ajour un fichier `annonceN.py` ou N est le numéro de votre groupe, par exemple `annonce7.py`.

Le fichier doit contenir une fonction s'appelant `annonce()` qui retourne une chaîne de caractères, comme ceci:

```python
def annonce():
	return "Après de longues heures d'attentes, j'ai l'immense honneur de vous annoncer que les chaussettes de l'archiduchesse sont sèches, archisèches."
```

Le fichier `main.py` appelle automatiquement toutes les fonctions `annonce` définies dans les fichiers `annonceN.py`. Vous ne devez pas modifier `main.py`

Pour le tester:
```
python3 main.py
```

Une fois que vous voyez votre phrase s'afficher correctement, commitez et pushez. Puis faites une pull request vers le répertoire depuis lequelle vous avez fork (en l'occurence https://gitlab.com/gbrochar/exercice-forge-git )

Attendez que nous ayons tous fini d'intégrer les pull requests dans le répertoire central ensemble.

Une fois cela fait, mettez à jour votre repo avec les changement en upstream et vérifier que vous avez bien reçu les fichiers créés par les autres groupes:

```
python3 main.py
```
