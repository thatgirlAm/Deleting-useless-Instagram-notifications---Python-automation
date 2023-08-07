#python automation project 1 : effacer les notifications contenant le mot "liked".

#ici l'on se connectera avec l'appareil à travers l'interface ADB téléchargée au préalable

#import de la bibliothèque python subprocess qui nous permet de fouiller l'appareil avec l'application ADB (Android Debug Bridge)

import subprocess

#Etape 1:  Connexion à l'appareil avec ADB
def connexion():
    # Exécute la commande adb pour connecter l'appareil
    subprocess.call(["adb", "devices"])


#Etape 2: Fonction pour supprimer les notifications contenant le mot "liked"
def suppression_notifications_specifiques():
	
    # Génération de la liste des notifications
    notifications = subprocess.check_output(["adb", "shell", "dumpsys", "notification", "--noredact"]).decode("utf-8")
    
    # Itération sur le nombre de lignes 
    for line in notifications.split("\n"):
    	
        # Test condition
        if "liked" in line:
        	
            # Exécute la commande adb pour supprimer la notification 
            notification_id = line.split(" ")[1].split(":")[1]
            subprocess.call(["adb", "shell", "service", "call", "notification", notification_id])


#Appel des fonctions
connexion()
suppression_notifications_specifiques()
