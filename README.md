# Création d'un environnement virtuel

python<version> -m venv nom_env_virtuel
source nom_env_virtuel/bin/activate

# Installation des packages

pip<version> install -r requirements.txt


# Exécution du script
Pour executer les differents scripts veuillez créer puis activer votre environnement de travail ainsi que les requirements comme indiqué ci dessous 
Placez vous dans le repertoire ou se trouve le fichier puis suivez les consignes suivantes:
  
Execution du script pour un livre tapez en ligne de commande: 
  python one_Book.py    
  
Execution du script de l'ensemble des livres tapez en ligne de commande :
python allBooksOK.py  
  
Execution du script pour les catégories tapez en ligne de commande :
python testcategory.py
  
 Execution du script pour extraire les images tapez en ligne de commande :
 python images_book.py
  
  

  
  
# Image
  Execution du script pour extraire les images tapez en ligne de commande :
  python images_book.py
  
Concernant le téléchargement des images Pensez a créer un repertoire <Images> dans le répertoire d'exécution du script 
pour le bon fonctionnement du programme

Où pour une exécution sans repertoire au niveau de cette ligne [with open("Images/"+filename,'wb') as f ] du script des images

Enlevez le répertoire Images et sauvegardez le fichier comme ceci  [with open(filename,'wb') as f]
ainsi les images seront téléchargées dans le répertoire courant

Merci de votre compréhension



