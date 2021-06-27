# PasswordManager
# Installation:
Auf das grüne Feld klicken (wo Code steht) und als ZIP herunterladen. In dem heruntergeladenen Ordner ein Powershell-Fenster öffnen und requirements.txt installieren: **pip install -r requirements.txt**. Der Passwort Manager ist nun einsatzbereit.

# Anmerkung:
Um den Passwort Manager als Program auszuführen, gebe in der Konsole folgendes ein: **python main.py**.
Um den Passwort Manager als Kommandozeilen Program auszuführen, muss in den **cli** Ordner navigiert werden. Dort musst dann ein Powershell-Fenster geöffnet werden, indem folgende Befehle eingeben werden:<br><br>

Um Einträge zu erstellen (mit storePassword.py):<br>
**python storePassword.py -username <NAME> -title <Titel>**<br><br>
  
Um Einträge zu löschen (mit deleteEntries.py)<br>
**python deleteEntries.py -entry <ID>**<br><br>
  
Um Einträge einzusehen (mit showEntries.py)<br>
**python showEntries.py**<br><br>
  
Um Passwörter zu erhalten, die in den Einträgen gespeichert sind (mit retrievePasssword.py):<br>
**python retrievePassword.py -entry <ID>**<br><br>
  
Um das Master Passwort zu ändern (mit changeMasterPassword.py)<br>
**python chnageMasterPassword.py**<br><br>
