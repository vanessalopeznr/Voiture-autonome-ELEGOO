# Ejecucion directa del proyecto

En esta **Seccion directa** se realizara las descargas y configuraciones necesarias para la ejecucion del proyecto sin pasar por los pasos descriptivos del proyecto. Es decir, las configuraciones ya se encuentran realizadas en el sistema operativo a descargar.

   Se realiza la descarga del [sistema operativo del proyecto](https://www.raspberrypi.com/software/operating-systems/)  y posteriormente se elige un metodo de instalacion en Micro SD como se indican las 2 opciones del paso 1. **Cambiar link cuando se suba el systema operativo .img.xz**

   Se realizan los pasos 4 y 5 de la [configuracion de Raspberry](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/tree/main/Version%201.0#configuracion-raspberry-pi-3-servidor). Y toda la [configuracion del computador](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/tree/main/Version%201.0#configuracion-de-computador-cliente) (Pasos 6, 7 y 8)

   Por ultimo, se conecta la camara y una fuente de alimentacion a la raspberry, esperar algunos segundos que la Raspberry inicie y solo se debe ejecutar el comando en el computador:

   ```
   python3 People_detection.py
   ```

# Paso a paso de descarga, configuracion y ejecucion del programa.

En esta **Seccion Paso a Paso** se realizara una descripcion detallada de los pasos a seguir para replicar el proyecto, con el fin de orientar aquellos que quisieran replicar el programa realizando modificaciones o usando versiones diferentes en los dispositivos utilizados. **Poner enlace de los dispositivos utilizados**

### Configuracion Raspberry Pi 3 (Servidor)
1. Descargar official supported operating system para Raspberry
   
   Se utiliza un sistema operativo [Raspberry Pi OS (64-bit) with desktop](https://www.raspberrypi.com/software/operating-systems/) de codigo abierto basado en Linux: Debian version 11 (bullseye) para un sistema de 64-bit de peso 818MB, con un nucleo Kernel version 6.1 que actúa como intermediario entre el hardware y el software. Es responsable de administrar los recursos del sistema, proporcionar servicios a los programas y facilitar la comunicación entre el hardware y el software.
   
   Para optimizacion de la memoria SD, es posible descargar el sistema operativo de version Lite.

   - Opcion 1: Para la instalacion de este sistema operativo en la raspberry, se utilizo una memoria Micro SD con su respectivo lecteur USB Micro SD y con ayuda del programa [Balena Etcher](https://etcher.balena.io/) se realizo la instalacion del sistema operativo Raspberry Pi OS (64-bit) with desktop directamente con el archivo comprimido que se descarga de la web en la memoria Micro SD.
     
   - Opcion 2: Tambien es posible realizar la instalacion del sistema operativo en la memoria SD sin aplicaciones externas para linux, siguiendo este [video](https://www.youtube.com/watch?v=xSxNJSkSgpk).
   
2. Configuraciones iniciales de Raspberry

   Despues de instalar el sistema operativo, es necesario ingresar la Micro SD a la Raspberry, conectar una pantalla, mouse, teclado y camara para la correcta ejecucion y configuracion del programa.

   **Warning** **[ Paso para seccion Paso a Paso ]** Se realizan algunas configuraciones como idioma, usuario y contrasena. Finalmente, retirar nuevamente la Micro SD e ingresar el programa [intermediary.py](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/Intermediary.py). En este proyecto se ingreso el programa en la siguiente ruta: _/media/user/rootfs/home/vehicle2/Desktop/_

4. Recursos necesarios para correr programa de Raspberry Pi

   Solo es necesario Python3 y ya viene instalado por defecto. Version de python utilizada para este proyecto: 3.9.2

   Realizar la conexion de la camara en la tarjeta Raspberry Pi.
   
5. Realizar comunicacion mediante un punto de acceso wifi.

   Se conecta el punto de acceso a una fuente de alimentacion (Power) y se realiza un reset para posteriormente conectarse a este dispositivo wifi mediante el usuario de red y la contrasena, generalmente indicadas en el dispositivo.
   
   Dispositivo utilizado para este proyecto: TP-LINK TL-MR3020 en modo 3G/4G.

6. Identificar direccion IP de la raspberry.

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
9. Para la descarga del programa tipo _.ino_ al dispositivo arduino, es necesario descargar el [Softare Arduino](https://www.arduino.cc/en/software):
    ```
    sudo apt install arduino
    ```
    Cuando la descarga finalice, abrir el programa, conectar por puerto serial USB el arduino al computador, verificar en "Outils" que le type de carte soit _Arduino Uno_ et le port soit (generalment) _/dev/ttyACMO (Arduino Uno)_ y Téléverser le code.

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
   
11. Loop en Raspberry para realizar ejecucion del programa de manera automatica al encendido del dispositivo.
   
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

> **Warning** **: Paso necesario solo si se encuentran problemas al detectar la camara**
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

## Fuentes
- Envio de flujo de video entre Raspberry y computador: [Source](https://github.com/raspberrypi/picamera2/blob/main/examples/mjpeg_server.py)
- Comunicacion Raspberry-Arduino: [Source](https://www.youtube.com/watch?v=jU_b8WBTUew)
- Auto Start a Program on Raspberry Pi (Opcion 4) : [Source](https://raspberrytips.com/autostart-a-program-on-boot/)

   

   


