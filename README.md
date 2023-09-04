# Voiture-autonome-ELEGOO

## Introduction

Ce projet s’agit de développer un algorithme pour la conduire autonome de un modèle réduit de voiture capable de suivre un véhicule "leader" en utilisant la vision par ordinateur et l’apprentissage automatique avec des réseaux neuronaux pour le détecter. À cette fin, deux véhicules robotique ELEGOO est disponible dans les installations du laboratoire SAMOVAR et nous proposons d’utiliser YOLOv8, un outil d’analyse d’image et détection d’objets.

La méthodologie mise en œuvre pour le projet consiste à établir d’abord une détection des personnes, avec des réseaux neuronaux déjà entraînés. Par la suite, lorsque ce processus est fonctionnel, ce développement est transféré à l’identification et au suivi d’un véhicule ELEGOO, en caractérisant un réseau neuronal avec d’images de cette voiture et d’autres similaires.

Vous trouverez ici 2 versions :

1. Version configurée pour la détection de personnes où deux méthodes sont indiquées :
   
- Pas à pas pour télécharger tous les programmes dans tous les appareils et plus tard, sa configuration et ses spécifications pour avoir l'option d'éventuelles modifications ou améliorations.
- Téléchargeable pour Raspberry, arduino et pc avec les configurations préalablement effectuées et toutes prêtes à être exécutées.

2. Version configurée pour la détection des véhicules ELEGOO. Les mêmes étapes sont suivies pour la configuration du programme comme indiqué dans le [readme de la version 1](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0%20-%20Personnes/README.md). Dans cette section, vous trouverez les étapes pour l'apprentissage du modèle.

   
Aqui se encontraran 2 versiones descargables:
1. Paso a paso para descargar todos los programas en todos los dispositivos y posteriormente, su configuracion y especificaciones para tener la opcion de posibles modificaciones o mejoras.
2. Descargables para Raspberry, arduino y pc con las configuraciones previamente realizadas y todo listo para la ejecucion.

Materiales utilizados:
- ELEGOO Smart Robot Car Kit V3.0 plus
- Raspberry pi 3 Model B+
- Raspberry pi Camera V2.1
- Memoria SD 8 GB
- Memoria externa 5V - 2A (max 2.4A)
- Baterias 18650
- Lector Micro SD
- Point d'access

<img width="2080" alt="wire connect rasp gitversion" src="https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/assets/123451768/bdf2722c-8abb-46f6-b5c6-439c4d281423">

## Areas de oportunidad 

- Voir ce qui est faisable concernant la partie asservissement (PID, ...).
- Mettre sur la voiture une carte GPU (telle que la Nvidia Jetson Nano) afin d'exécuter le réseau Yolo. La voiture serait ainsi autonome vis-à-vis du PC, du WiFi, ...

