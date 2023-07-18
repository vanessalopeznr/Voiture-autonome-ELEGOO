# Paso a paso de descarga, configuracion y ejecucion del programa.

1. Descargar official supported operating system para Raspberry
   
   Se utiliza un sistema operativo [Raspberry Pi OS (64-bit) with desktop](https://www.raspberrypi.com/software/operating-systems/) de codigo abierto basado en Linux: Debian version 11 (bullseye) para un sistema de 64-bit de peso 818MB, con un nucleo Kernel version 6.1 que actúa como intermediario entre el hardware y el software. Es responsable de administrar los recursos del sistema, proporcionar servicios a los programas y facilitar la comunicación entre el hardware y el software.
   
   Para optimizacion de la memoria SD, es posible descargar el sistema operativo de version Lite.

   **Especificar si hay que descomprimir el archivo zip o se monta asi directamente a Balena**

   Para la instalacion de este sistema operativo en la raspberry, se utilizo una memoria Micro SD en un lector para ser lecteur USB Micro SD y con ayuda del programa [Balena Etcher](https://etcher.balena.io/) se realizo la instalacion del sistema operativo en la memoria Micro SD.

2. Instalacion de librerias necesarias
   
   Le fichier requirements.txt contient tous les packages Python à installer pour faire fonctionner le travail. Pour tout installer, executez la commande suivante:
   ```
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

3. Configuracion de especificaciones en el archivo config.txt [[Documentacion]](https://www.raspberrypi.com/documentation/computers/config_txt.html)
   
   La configuracion utilizada se encuentra en el archivo [config.txt](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/config.txt) especificamente utilizada para Raspberry camara V2.1 **Poner ruta del archivo config.txt**
   
   Si se desea utilizar otra camara, se puede consultar la siguiente tabla en la [[Documentacion]](https://www.raspberrypi.com/documentation/computers/camera_software.html)
   | Camera Module  | In /boot/config.txt |
   | ------------- | ------------- |
   | V1 camera (OV5647) | dtoverlay=ov5647 |
   | V2 camera (IMX219) | dtoverlay=imx219 |
   | HQ camera (IMX477) | dtoverlay=imx477 |
   | GS camera (IMX296) | dtoverlay=imx296 |
   | Camera Module 3 (IMX708) | dtoverlay=imx708 |
   | IMX290 and IMX327 | dtoverlay=imx290,clock-frequency=74250000 or dtoverlay=imx290 |
   | IMX378 | dtoverlay=imx378 |
   | OV9281 | dtoverlay=ov9281 |
   
   Pour activer la détection automatique de la caméra, les utilisateurs doivent ajouter l'entrée camera_auto_detect=1 dans le fichier config.txt. **Votre Raspberry Pi devra être redémarré après avoir modifié ce fichier**

   Para verificar que la Raspberry esta detectando correctamente la camara, se debe utilizar el siguiente comando, confirmando la respuesta indicada:
   ```
   vcgencmd get_camera
   ```

   Donde su respuesta debe ser: _**supported=1 detected=1**_

   


