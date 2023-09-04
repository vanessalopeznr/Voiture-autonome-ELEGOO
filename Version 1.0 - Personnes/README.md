# Detection des personnes

Dans cette version, vous pouvez mettre en œuvre 2 utilisations du référentiel, l'exécution directe et le pas à pas.

## Exécution directe du projet

Dans cette **section directe**, les téléchargements et les configurations nécessaires pour exécuter le projet seront effectués uniquement en configurant la communication entre le Raspberry et le PC (Saisir l'adresse IP du Raspberry utilisé dans l'ordinateur). Les configurations sont déjà effectuées dans le système d'exploitation à télécharger.

   Les étapes de la configuration du Raspberry, l'ordinateur et l'aduino doivent être réalisées jusqu'à l'étape 8.

   Enfin, il faut brancher une alimentation au Raspberry, attendre quelques secondes que le Raspberry démarre et simplement exécuter la commande sur l'ordinateur :

   ```
   python3 People_detection.py
   ```

## Étape par étape du téléchargement, de la configuration et de l'exécution du programme.

Dans cette section **Pas à Pas** nous ferons une description détaillée des étapes à suivre pour répliquer le projet, afin de guider ceux qui voudraient répliquer le programme en faisant des modifications ou en utilisant des versions différentes dans les appareils utilisés. 

### Configuration Raspberry Pi 3 (Serveur)
1. Télécharger le système d'exploitation officiel pour Raspberry Pi 3
   | ⚠️ Section étape par étape
   |------------------------------------------|
   | Un système d'exploitation open source basé sur Linux [Raspberry Pi OS (64-bit) with desktop](https://www.raspberrypi.com/software/operating-systems/) est utilisé : Debian version 11 (bullseye) pour un système 64 bits pesant 818MB, avec un noyau version 6.1 qui agit comme un intermédiaire entre le matériel et le logiciel. Il est chargé de gérer les ressources du système, de fournir des services aux programmes et de faciliter la communication entre le matériel et les logiciels.
   Pour optimiser la mémoire SD, il est possible de télécharger la version Lite du système d'exploitation. |
   
   | ⚠️ Section directe
   |------------------------------------------|
   Téléchargement du [système d'exploitation du projet](https://drive.google.com/file/d/16MZGht5VuJNM8DZ3qeuCO1S89kebPjpr/view?usp=drive_link) |

   - Option 1 : Pour l'installation de ce système d'exploitation sur le raspberry, nous avons utilisé une mémoire Micro SD avec son lecteur USB Micro SD respectif et avec l'aide du programme [Balena Etcher](https://etcher.balena.io/) nous avons installé le système d'exploitation directement avec le fichier compressé sur la mémoire Micro SD.

   - Option 2 : Il est également possible d'installer le système d'exploitation sur la mémoire SD sans applications linux externes en suivant cette [vidéo](https://www.youtube.com/watch?v=xSxNJSkSgpk).
   
3. Configuration initiale du Raspberry

   Après avoir installé le système d'exploitation, il est nécessaire d'insérer la carte Micro SD dans le Raspberry, de connecter une alimentation électrique, un écran, une souris, un clavier et une caméra pour l'exécution et la configuration correctes du programme.
   
   | Pas uniquement pour la section Étape par étape ⚠️.
   |------------------------------------------|
   | Vous effectuez quelques configurations telles que la langue, l'utilisateur et le mot de passe. Enfin, retirez à nouveau la carte Micro SD et entrez dans le programme [intermediary.py](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/Intermediary.py). Dans ce projet, le programme a été entré dans le chemin suivant : _/media/user/rootfs/home/vehicle2/Desktop/_ |
   
5. Ressources nécessaires pour exécuter les programmes Raspberry Pi

   Seul **Python3** est nécessaire et est déjà installé par défaut. Version de Python utilisée pour ce projet : 3.9.2

   Connectez la caméra à la carte Raspberry Pi.
   
6. Communication via un point d'accès wifi.

   Le point d'accès est connecté à une alimentation (Ordinateur) et une réinitialisation est effectuée pour se connecter ensuite à ce dispositif wifi en utilisant l'utilisateur et le mot de passe du réseau, généralement indiqués sur le dispositif.
   
   Appareil utilisé pour ce projet : TP-LINK TL-MR3020 en mode 3G/4G.

7. Identifier l'adresse IP du raspberry.

   Après avoir connecté le raspberry au point d'accès, l'adresse IP de l'appareil peut être trouvée en utilisant la commande suivante :
   ```
   hostname -I
   ```

### Configuration de l'ordinateur (Client)
6. Apportez les corrections nécessaires aux fichiers telles que les changements d'adresse IP.
    
    Dans le programme [People_detection.py](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Computer/People_detection.py), modifiez la variable _address_ et remplacez-la par l'adresse IP du raspberry identifié à l'étape précédente.

7. Ressources nécessaires pour exécuter le programme PC
   
   Seul python3 est nécessaire. La version utilisée dans ce projet est : python 3.8.10
   
   Le fichier requirements.txt contient tous les paquets Python à installer pour exécuter le travail. Pour l'installer, exécutez la commande suivante :
   ```
   pip install -r requirements.txt
   ```
   
   Voici quelques spécifications (les bibliothèques sont incluses dans le fichier requirements.txt pour le téléchargement) :
   
   - Opencv version 4.7.0.72
   - YOLO from ultralytics version 8.0.117 : [Documentation](https://docs.ultralytics.com/quickstart/) pour le téléchargement de la bibliothèque. 
   - Socket : ce module fait partie de la bibliothèque standard de Python.

8. Communiquer via un point d'accès wifi avec l'ordinateur (voir étape 4).

### Configuration de l'arduino
9. Pour télécharger [le programme](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/Arduino/ArduinoConnectionRaspberry.ino) de type _.ino_ sur l'appareil arduino, il est nécessaire de télécharger le [Softare Arduino](https://www.arduino.cc/en/software) sur n'importe quel appareil car le programme ne sert qu'à télécharger le code sur l'arduino, comme suit :
    ```
    sudo apt install arduino
    ```
    Lorsque le téléchargement est terminé, ouvrez le programme, connectez par port série USB l'arduino à l'ordinateur, vérifiez dans "Outils" que le type de carte est _Arduino Uno_ et que le port est (généralement) _/dev/ttyACMO (Arduino Uno)_ et Téléverser le code.

    Enfin, déconnectez l'arduino de l'ordinateur et connectez-le avec le même câble USB au Raspberry.
    
### PC - Raspberry - Intégration Arduino
10. Lorsque les deux appareils (Raspberry et ordinateur) sont connectés au point d'accès wifi et l'arduino par le port série au Raspberry, exécutez ces commandes sur les appareils respectifs :

    Exécutez la commande suivante sur le raspberry :

    ```
    python3 intermediary.py
    ```

    Attendez que le terminal affiche _"Waiting for command..."_ et exécutez la commande suivante sur l'ordinateur :
    ```
    python3 People_detection.py
    ```

    Enfin, le programme doit afficher la détection de personnes par la caméra Raspberry et faire pivoter la voiture dans la direction de la caméra.

    Le programme s'arrête en appuyant sur `Ctr + C`.
   
12. Faites une boucle dans le Raspberry pour exécuter le programme automatiquement lorsque l'appareil est allumé.

    Cette étape est réalisée pour éviter de connecter les périphériques au Raspberry afin qu'il puisse fonctionner automatiquement sans avoir à taper la commande pour exécuter le programme.

    Lorsque l'étape précédente a été exécutée avec succès. Exécutez les commandes suivantes pour effectuer la configuration.

    Ouvrez le fichier exécutable qui gère les paramètres lorsque l'appareil est mis sous tension :
    ```
    sudo nano /etc/rc.local
    ```

    Écrivez la commande que vous voulez exécuter à l'initialisation de l'appareil avant la dernière ligne _exit 0_. La commande _python3 home/vehicle2/Desktop/connectionhttp.py_ a été utilisée dans la configuration de ce projet.
    ```
    python3 <chemin du fichier exécutable>
    ```

    Enfin, redémarrez le Raspberry pour exécuter les changements de configuration et maintenant, exécutez simplement la commande sur l'ordinateur :
    ```
    python3 People_detection.py
    ```

> **⚠️ Warning** **: Étape requise uniquement en cas de problèmes lors de la détection de la caméra**
> 
> Paramètres de spécification dans le fichier config.txt  [[Documentacion]](https://www.raspberrypi.com/documentation/computers/config_txt.html)
> 
> La configuration utilisée est spécifique à la caméra Raspberry V2.1 et se trouve dans le fichier [config.txt](https://github.com/vanessalopeznr/Voiture-autonome-ELEGOO/blob/main/Version%201.0/Raspberry/config.txt) où ce fichier est normalement accessible sous _/boot/config.txt_.
> 
> Si vous souhaitez utiliser un autre appareil photo, vous pouvez consulter le tableau suivant dans la [[Documentation]].(https://www.raspberrypi.com/documentation/computers/camera_software.html)
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
> Pour vérifier que le Raspberry détecte correctement la caméra, utilisez la commande suivante, en confirmant la réponse indiquée :
> ```
> vcgencmd get_camera
> ```
> 
> La réponse devrait être la suivante : supported=1 detected=1
