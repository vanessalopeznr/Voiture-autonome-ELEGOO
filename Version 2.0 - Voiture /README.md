# Detection de la voiture

Dans ce veersion, nous utilisons le même mécanisme, la même architecture et le même code pour envoyer des données entre les différents dispositifs, à la différence que nous chargeons maintenant les poids du réseau neuronal entraîné pour la détection des voitures.

La création de l’ensemble de données contient 250 illustrations stockées dans le dossier ["train"](https://drive.google.com/drive/u/2/folders/1B2gjhMdKPoxeWlDchPq-U7RaNp5DSdJj) avec des images du véhicule ELEGOO original trouvées sur internet, des images de véhicules similaires et des photos prises dans le véhicule en laboratoire. Cependant, ces images ne sont pas suffisantes pour un bon entraînement du modèle, c'est pourquoi un algorithme d'augmentation ["DataGenerator"](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%202.0%20-%20Voiture%20/Entra%C3%AEnement%20%20voiture/DataGenerator.py) a été utilisé pour disposer d'une base de données robuste. Les 25 images les plus représentatives du véhicule ont été prises et 250 images supplémentaires ont été obtenues. Au final, l'ensemble de données est composé de 500 images.

## Entraînement

Tous les entraînements de réseaux neuronaux ont été effectués sur la base du guide ["How to Train YOLOv8 Object Detection on a Custom Dataset"](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/) de Piotr Skalski. Et les étapes depuis "Preparing a custom dataset for YOLOv8" ont été fidèlement suivies. YOLOV8 a été utilisé dans [le notebook roboflow](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb?ref=blog.roboflow.com) sur google colab, où le processus à suivre pour l'entraînement réussi d'un modèle est clairement spécifié. Enfin, ce processus dans la plateforme "roboflow" est effectué pour obtenir le fichier des poids entraînés pour la détection des véhicules ELEGOO, qui se trouve dans le dossier ["Modèles"](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/tree/main/Version%202.0%20-%20Voiture%20/Mod%C3%A8les) et l'introduire dans le code du projet. Vous y trouverez 3 fichiers de poids avec un nombre différent d'images."bestV1" avec 645 images, "bestV2" avec 717 images et "bestV3" avec 1200 images.

![V2 (1)](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/assets/123451768/e2996ffb-fa18-4099-9d76-216a7194bd22)

### Quelques précisions sur la configuration des paramètres dans l'entraînement du réseau.

- Après l'étiquetage des images, un ensemble de données de 1200 images a été généré à l'aide de l'outil d'augmentation de la plateforme "Roboflow", dans lequel des rotations horizontales, du bruit et des carrés noirs ont été appliqués dans certaines sections de l'image.
- Le générateur de données "Roboflow" segmente l’ensemble de données en 87 % d’images de formation, 8 % d’images de validation et 4 % d’images de test.
- Pour l'entraînement, 50 époques ont été prises.

### Erreurs commises

Initialement, le réseau a été entraîné avec 170 images du véhicule, 100 images supplémentaires générées par l'algorithme d'augmentation Python et 375 ont été ajoutées par l'outil d'augmentation de la plateforme "roboflow". Avec cet ensemble de données de 645 images et 25 époques, le modèle ne différencie pas très bien l’environnement et le véhicule dans chaque image. En outre, il est difficile de détecter correctement les voitures et n’effectue pas l’identification dans les images où l’arrière du véhicule est situé. Enfin, le seuil de détection est trop bas pour l’identification des voitures.

![V1 (1)](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/assets/123451768/148ae198-16d4-4c1c-98f9-4850ae1da405)

Pour cette raison, la base de données a été augmentée à 1200 images et les époques à 50.

