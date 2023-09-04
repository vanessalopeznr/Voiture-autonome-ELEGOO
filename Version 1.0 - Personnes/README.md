# Detection des personnes

Dans cette version, vous pouvez mettre en œuvre 2 utilisations du référentiel, l'exécution directe et le pas à pas.

## Exécution directe du projet

Dans cette **section directe**, les téléchargements et les configurations nécessaires pour exécuter le projet seront effectués uniquement en configurant la communication entre le Raspberry et le PC (Saisir l'adresse IP du Raspberry utilisé dans l'ordinateur). Les configurations sont déjà effectuées dans le système d'exploitation à télécharger.

   Les étapes de la configuration du Raspberry, l'ordinateur et l'aduino doivent être réalisées jusqu'à l'étape 8.

   Enfin, il faut brancher une alimentation au Raspberry, attendre quelques secondes que le Raspberry démarre et simplement exécuter la commande sur l'ordinateur :

   ```
   python3 People_detection.py
   ```

## Paso a paso de descarga, configuracion y ejecucion del programa.

En esta **Seccion Paso a Paso** se realizara una descripcion detallada de los pasos a seguir para replicar el proyecto, con el fin de orientar aquellos que quisieran replicar el programa realizando modificaciones o usando versiones diferentes en los dispositivos utilizados. **Poner enlace de los dispositivos utilizados**

### Configuracion Raspberry Pi 3 (Servidor)
1. Descargar official supported operating system para Raspberry
   | ⚠️ Paso para Seccion Paso a Paso |
   |------------------------------------------|
   | Se utiliza un sistema operativo [Raspberry Pi OS (64-bit) with desktop](https://www.raspberrypi.com/software/operating-systems/) de codigo abierto basado en Linux: Debian version 11 (bullseye) para un sistema de 64-bit de peso 818MB, con un nucleo Kernel version 6.1 que actúa como intermediario entre el hardware y el software. Es responsable de administrar los recursos del sistema, proporcionar servicios a los programas y facilitar la comunicación entre el hardware y el software.
   Para optimizacion de la memoria SD, es posible descargar el sistema operativo de version Lite. |
   
   | ⚠️ Paso para Seccion directa |
   |------------------------------------------|
   | Se realiza la descarga del [sistema operativo del proyecto](https://drive.google.com/file/d/16MZGht5VuJNM8DZ3qeuCO1S89kebPjpr/view?usp=drive_link)  |



## Étape par étape du téléchargement, de la configuration et de l'exécution du programme.

Dans cette section **Pas à Pas** nous ferons une description détaillée des étapes à suivre pour répliquer le projet, afin de guider ceux qui voudraient répliquer le programme en faisant des modifications ou en utilisant des versions différentes dans les appareils utilisés. 

### Configuration Raspberry Pi 3 (Serveur)
1. Télécharger le système d'exploitation officiel pour Raspberry Pi 3
   | ⚠️ Section étape par étape
   |------------------------------------------|
   | Un système d'exploitation open source basé sur Linux [Raspberry Pi OS (64-bit) with desktop] (https://www.raspberrypi.com/software/operating-systems/) est utilisé : Debian version 11 (bullseye) pour un système 64 bits pesant 818MB, avec un noyau version 6.1 qui agit comme un intermédiaire entre le matériel et le logiciel. Il est chargé de gérer les ressources du système, de fournir des services aux programmes et de faciliter la communication entre le matériel et les logiciels.
   Pour optimiser la mémoire SD, il est possible de télécharger la version Lite du système d'exploitation. |
   
   | ⚠️ Step to Direct Section
   |------------------------------------------|
   Téléchargement du [système d'exploitation du projet] (https://drive.google.com/file/d/16MZGht5VuJNM8DZ3qeuCO1S89kebPjpr/view?usp=drive_link) |
   
- Opcion 1: Para la instalacion de este sistema operativo en la raspberry, se utilizo una memoria Micro SD con su respectivo lecteur USB Micro SD y con ayuda del programa [Balena Etcher](https://etcher.balena.io/) se realizo la instalacion del sistema operativo directamente con el archivo comprimido en la memoria Micro SD.

- Opcion 2: Tambien es posible realizar la instalacion del sistema operativo en la memoria SD sin aplicaciones externas para linux, siguiendo este [video](https://www.youtube.com/watch?v=xSxNJSkSgpk).
   
3. Configuraciones iniciales de Raspberry

   Despues de instalar el sistema operativo, es necesario ingresar la Micro SD a la Raspberry, conectar una fuente de alimentacion, una pantalla, mouse, teclado y camara para la correcta ejecucion y configuracion del programa.
   
   | ⚠️ Paso para seccion Paso a Paso |
   |------------------------------------------|
   | Se realizan algunas configuraciones como idioma, usuario y contrasena. Finalmente, retirar nuevamente la Micro SD e ingresar el programa [intermediary.py](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/Intermediary.py). En este proyecto se ingreso el programa en la siguiente ruta: _/media/user/rootfs/home/vehicle2/Desktop/_ |

5. Recursos necesarios para correr programa de Raspberry Pi

   Solo es necesario Python3 y ya viene instalado por defecto. Version de python utilizada para este proyecto: 3.9.2

   Realizar la conexion de la camara en la tarjeta Raspberry Pi.
   
6. Realizar comunicacion mediante un punto de acceso wifi.

   Se conecta el punto de acceso a una fuente de alimentacion (Power) y se realiza un reset para posteriormente conectarse a este dispositivo wifi mediante el usuario de red y la contrasena, generalmente indicadas en el dispositivo.
   
   Dispositivo utilizado para este proyecto: TP-LINK TL-MR3020 en modo 3G/4G.

7. Identificar direccion IP de la raspberry.

   Posterior a la conexion de la raspberry al punto de acceso, la direccion IP del dispositivo se puede encontrar utilizando el siguiente comando:
   ```
   hostname -I
   ```
### Configuracion de computador (Cliente)
6. Realizar las correcciones necesarias de los archivos como cambios de direcciones IP
    
    En el programa [People_detection.py](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Computer/People_detection.py) modificar la variable _address_ y sustituir por la direccion IP de la raspberry identidficada en el paso anterior.

7. Recursos necesarios para correr programa de PC
   
   Solo es necesario python3. La version utilizada en este proyecto fue: python 3.8.10
   
   Le fichier requirements.txt contient tous les packages Python à installer pour faire fonctionner le travail. Pour tout installer, executez la commande suivante:
   ```
   pip install -r requirements.txt
   ```
   
   Algunas especificaciones son (Las librerias estan incluidas en requirements.txt para su descarga):
   
   - Opencv version 4.7.0.72
   - YOLO from ultralytics version 8.0.117:  [Documentacion](https://docs.ultralytics.com/quickstart/) para descarga de la libreria. 
   - socket: Este modulo forma parte de la biblioteca estándar de Python

8. Realizar comunicacion mediante un punto de acceso wifi con el computador (Ver paso 4).

### Configuracion del arduino
9. Para la descarga del programa tipo _.ino_ al dispositivo arduino, es necesario descargar el [Softare Arduino](https://www.arduino.cc/en/software) en cualquier disposotivo ya que el programa solo es para descargar el codigo en el arduino, de la siguiente manera:
    ```
    sudo apt install arduino
    ```
    Cuando la descarga finalice, abrir el [programa](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/Arduino/ArduinoConnectionRaspberry.ino), conectar por puerto serial USB el arduino al computador, verificar en "Outils" que le type de carte soit _Arduino Uno_ et le port soit (generalment) _/dev/ttyACMO (Arduino Uno)_ y Téléverser le code.

    Finalmente, se desconecta el arduino del computador y se conecta con el mismo cable USB a la Raspberry.
    
### Integracion PC - Raspberry - Arduino
10. Cuando se encuentren conectados los dos dispositivos (Raspberry y computador) al punto de acceso wifi y el arduino por puerto serial a la raspberry, se ejecuta estos comandos en los respectivos dispositivos:

    Ejecutar el siguiente comando en la raspberry:

    ```
    python3 intermediary.py
    ```

    Esperar que la terminal imprima _"Waiting for command..."_ y ejecutar el siguiente comando en el computador:
    ```
    python3 People_detection.py
    ```

    Finalmente, el programa debe mostrar la deteccion de las personas mediante la camara Raspberry y rotar el carro en direccion de la misma.

    El programa se detiene, apoyando sobre las teclas `Ctr + C`.
   
12. Loop en Raspberry para realizar ejecucion del programa de manera automatica al encendido del dispositivo.

    Este paso se realiza para evitar conectar las periferias a la raspberry y ella pueda operar automaticamente sin escribir el comando de ejecucion del programa.

    Cuando el paso anterior se haya ejecutado de manera exitosa. Ejecutar los siguientes comandos para realizar la configuracion.

    Abrir el archivo ejecutable que administra las configuraciones al encender el dispositivo:
    ```
    sudo nano /etc/rc.local
    ```

    Se escribe el comando que se desea ejecutar en la inicializacion del dispositivo antes de la ultima linea _exit 0_. En la configuracion de este proyecto se utilizo el comando _python3 home/vehicle2/Desktop/connectionhttp.py_
    ```
    python3 <ruta del archivo ejecutable>
    ```

    Por ultimo, reinicializar la Raspberry para ejecutar los cambios de configuracion y ahora, solo se debe ejecutar el comando del computador:
    ```
    python3 People_detection.py
    ```

> **⚠️ Warning** **: Paso necesario solo si se encuentran problemas al detectar la camara**
> 
> Configuracion de especificaciones en el archivo config.txt [[Documentacion]](https://www.raspberrypi.com/documentation/computers/config_txt.html)
> 
> La configuracion utilizada es especificamente para Raspberry camara V2.1 y se encuentra en el archivo [config.txt](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/config.txt) où ce fichier est normalement accessible sous _/boot/config.txt_
> 
> Si se desea utilizar otra camara, se puede consultar la siguiente tabla en la [[Documentacion]](https://www.raspberrypi.com/documentation/computers/camera_software.html)
> | Camera Module  | In /boot/config.txt |
> | ------------- | ------------- |
> | V1 camera (OV5647) | dtoverlay=ov5647 |
> | V2 camera (IMX219) | dtoverlay=imx219 |
> | HQ camera (IMX477) | dtoverlay=imx477 |
> | GS camera (IMX296) | dtoverlay=imx296 |
> | Camera Module 3 (IMX708) | dtoverlay=imx708 |
> | IMX290 and IMX327 | dtoverlay=imx290,clock-frequency=74250000 or dtoverlay=imx290 |
> | IMX378 | dtoverlay=imx378 |
> | OV9281 | dtoverlay=ov9281 |
> 
> Pour activer la détection automatique de la caméra, les utilisateurs doivent ajouter l'entrée camera_auto_detect=1 dans le fichier config.txt. **Votre Raspberry Pi devra être redémarré après avoir modifié ce fichier**
> 
> Para verificar que la Raspberry esta detectando correctamente la camara, se debe utilizar el siguiente comando, confirmando la respuesta indicada:
> ```
> vcgencmd get_camera
> ```
> 
> Donde su respuesta debe ser: _supported=1 detected=1

   

   


