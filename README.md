# PythonMiniGameClient
This project is an online multiplayer minigame client. 
Althought the latest version doesn't include all of the minigames, all of the networking is complete and the code is open to additions of new games. 
There are 2 ways to run this program: on one computer(master control) or on two computers(normal control)

**MASTER CONTROL**
To run the project with master control, just download the whole zip on one computer and unzip. It is important that you run ```pip install pygame``` in your powershell before running this project. Then, look for the ***Master.py*** and click to run. 
**NORMAL CONTROL**
To run the project with normal control, download the zip onto two computers; one of the computers will be the host and the other one will connect to the host computer. On both computers, run ```pip install pygame``` before running the scripts in the zip. On the host computer, download the zip and unzip. You will not need to make any changes in the files. On the connecting computer, download the zip and unzip. Then open the ***network.py*** file and look for:
```
#ONLY EDIT THE NEXT LINE
self.server = socket.gethostbyname(socket.gethostname())
#DO NOT EDIT PAST THIS POINT
```
Get the IPV4 address of the host computer using ```ipconfig``` in powershell and assign self.server to it encased in quotations. It should look something like this:
```
#ONLY EDIT THE NEXT LINE
self.server = "10.123.12.34"
#DO NOT EDIT PAST THIS POINT
```
After that, save the network file and close.
To actually run the program on the two computers, run ***HostClient.py*** on the host computer and ***ConnectClient.py*** on the connecting computer. It is vital that you run the ***HostClient.py*** first because it is responsible for running the server. 
**GENERAL CONTROLS**
After running the program, DO NOT close the command prompts that open, that will close the program. 
```drg```
