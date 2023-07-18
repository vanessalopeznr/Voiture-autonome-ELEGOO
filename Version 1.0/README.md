# Paso a paso de descarga, configuracion y ejecucion del programa.

1. Descargar official supported operating system para Raspberry
   
   Se utiliza un sistema operativo [Raspberry Pi OS (64-bit) with desktop](https://www.raspberrypi.com/software/operating-systems/) de codigo abierto basado en Linux: Debian version 11 (bullseye) para un sistema de 64-bit de peso 818MB, con un nucleo Kernel version 6.1 que actúa como intermediario entre el hardware y el software. Es responsable de administrar los recursos del sistema, proporcionar servicios a los programas y facilitar la comunicación entre el hardware y el software.

   pero tambien es posible realizarlo con la version Lite **Especificar si hay que descomprimir el archivo zip o se monta asi directamente a Balena**
Para la instalacion de este sistema operativo en la raspberry, se utilizo una memoria Micro SD en un lector para ser lecteur USB Micro SD y con ayuda del programa [Balena Etcher](https://etcher.balena.io/) se realizo la instalacion del sistema operativo en la memoria Micro SD.

3. Instalacion de librerias necesarias
