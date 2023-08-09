#python automation project 1 : deleting "liked" notifications.

#-------------------------------Explanations----------------------------------------
#here's how we'll proceed : we'll access the phone through ADB and read notifications, 
#when "liked" is encountered, the whole line (which is the whole notification is deleted)
#we'll use an infinite loop + the sleep feature of the time library to add an interval
#which will result in running the script every two hours (every 7200 seconds)

#-------------------------------Coding----------------------------------------------

#importing subprocess to connect through ADB (Android Debug Bridge) 
import subprocess, time

#Step 1 : connecting to the phone with adb 
def connecting():
    #Executing the connecting command to connect to the phone through ADB
    subprocess.call(["adb", "devices"])


#Estep 2 : deleting the "liked" notifications every 2 hours 
def deleting_notifications():
	
   #generating notifications list
   #infinite loop 
            notifications = subprocess.check_output(["adb", "shell", "dumpsys", "notification", "--noredact"]).decode("utf-8")
            
                #lines itérations (notifications)
                for line in notifications.split("\n"):
                    
                    #condition testing 
                    if "liked" in line:
                        
                        #deleting the notification through ADB 
                        notification_id = line.split(" ")[1].split(":")[1]
                        subprocess.call(["adb", "shell", "service", "call", "notification", notification_id])


#-------------------------------Running the scripts-----------------------------------------------------------

#connecting 
    connecting()

#avoiding hiccups   
   while (True):
        #avoiding hiccups 
        try : 
            deleting_notifications()
            time.sleep(7200)
        except:
        print ("Script error or human intervention")

