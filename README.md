# Lol Chat Analyzer

Dans ce projet, nous allons utiliser un modèle pour déterminer si un message dans la messagerie du jeu League of Legends peut être potentiellement banni. Cela pourra servir au service des signalement du jeu d’avoir un filtre sur les signalements effectué pour message offensant/négatif.

# Analyse des données

Afin de savoir si le modèle que nous allons utiliser est compatible avec les messages signalés, nous allons effectuer des analyses de données. Nous allons tester le modèle VADER ainsi que ROBERTA afin de les comparer et voir lequel sera le plus utilisable dans notre projet.

L’analyse des données est disponible dans le fichier [LolTribunalTreatment.ipynb](https://github.com/MelvinCRNR/lolchat-analyzer/blob/main/LolTribunalTreatment.ipynb).

Pour lancer les cellules du Notebook, vous devez télécharger le fichier .csv du lien suivant : [https://www.kaggle.com/simshengxue/league-of-legends-tribunal-chatlogs](https://www.kaggle.com/simshengxue/league-of-legends-tribunal-chatlogs).

Vous devez le mettre dans le même fichier que le Notebook et le renommer **chatlogs.csv.**

# Déploiement de l’application Flask en local via Docker

Lancer la commande suivante pour build :

```bash
sudo docker build --tag flask-ban-rate-lol .
```

Lancer la commande pour run :

```bash
sudo docker run --name flask-ban-rate-lol -p 5002:5002 flask-ban-rate-lol
```

#