# Création d'un environnement virtuel

python<version> -m venv nom_env_virtuel
source nom_env_virtuel/bin/activate

# Installation des packages

pip<version> install -r requirements.txt


# Exécution du script

# Image
Concernant le téléchargement des images Pensez a créer un repertoire <Images> dans le répertoire d'exécution du script 
pour le bon fonctionnement du programme

Où pour une exécution sans repertoire au niveau de cette ligne [with open("Images/"+filename,'wb') as f ] du script des images

Enlevez le répertoire Images et sauvegardez le fichier comme ceci  [with open(filename,'wb') as f]
ainsi les images seront téléchargées dans le répertoire courant

Merci de votre compréhension



