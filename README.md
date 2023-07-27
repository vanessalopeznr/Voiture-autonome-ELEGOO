# Voiture-autonome-ELEGOO
Voiture qui envoie un flux vidéo à un ordinateur pour compiler le détecteur de personnes Yolo V8 et envoyer une commande pour prendre des décisions concernant les mouvements.

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

<img width="1312" alt="wire connect rasp" src="https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/assets/123451768/ce6a7315-382b-42d2-8a7e-e2b670df5ce6">

## Areas de oportunidad 

- Gérer la détection de plusieurs personnes.
- Entrainer la réseau de neurones pour qu'il reconnaisse la voiture de devant (ou autre chose), sous différents angles.
- Voir ce qui est faisable concernant la partie asservissement (PID, ...).
- Mettre sur la voiture une carte GPU (telle que la Nvidia Jetson Nano) afin d'exécuter le réseau Yolo. La voiture serait ainsi autonome vis-à-vis du PC, du WiFi, ...

