# Hasch Code 2019
 
<p align="center">
<img  src="images\logo.png" alt="Hash Code Logo" width="400" height="">
</p>

## Introduction :pencil:
Concours organisé par Google en 2019. L’objectif est de répondre à une problématique donnée, sur le thème du traitement de donné.
Le script est fait en Python V3. Aucune bibliothèque externe n’est nécessaire.
Les résultats sont calculés et affiché directement dans le terminal. Les fichiers à traiter sont dans Haschcode 2019\qualification_round_2019.in. 

## [Problématique 📷](hashcode2019_qualification_task.pdf)

Comme le dit le proverbe, "une image est un millier de mots".
Nous sommes d'accord, les photos sont une importante part de la vie numérique et culturelle contemporaine. Environ 2,5 milliards dans le monde entier, les gens portent un appareil photo, sous forme de smartphone, dans leur de poche tous les jours. Nous en faisons aussi bon usage, en prenant plus de photos que jamais (en 2017, Google Photos a annoncé qu'il soutenait plus de 1,2 milliard de photos et des vidéos par jour). 
L'essor de la photographie numérique crée un défi intéressant : que devons-nous faire avec toutes ces photos ? Dans cette problématique de concours, nous allons explorer l'idée de composer un diaporama à partir d'une collection de photos.

### Objectif ✔️
En fonction de la liste des photos et des balises associées à chacune d'entre elles, classez les photos en un diaporama aussi intéressant que possible.

Une photo est décrite par un ensemble de balises. Par exemple, une photo avec un chat sur une plage, pendant un après-midi ensoleillé, peut être avec les balises suivantes : [chat, plage, soleil]. L'orientation de chaque photo est soit horizontale, soit verticale.

Un diaporama est une liste ordonnée de diapositives. Chaque diapositive contient l'une ou l'autre :
- Une seule photo horizontale
- Deux photos verticale côte à côte

### Calcul du Score 🏅
Le diaporama est noté en fonction de l'intérêt des transitions entre chaque paire de ses diapositives suivantes ont.
Nous voulons que les transitions aient quelque chose en commun pour préserver la continuité (les deux diapositives ne doivent pas être totalement différentes).
La similitude de deux photos verticales sur une même diapositive n'est pas prise en compte pour la notation.
Cela signifie que deux photos peuvent, mais ne doivent pas nécessairement, avoir des tags en commun.

Pour les deux diapositives suivantes S i et S i+1 , le facteur d'intérêt est le minimum (le plus petit numéro des trois):
- Le nombre de balises communes entre S i et S i+1
- Le nombre de balises dans S i mais pas dans S i+1
- Le nombre de balises dans S i+1 mais pas dans S i .
