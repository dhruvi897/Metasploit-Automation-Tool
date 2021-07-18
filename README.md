# Metasploit-Automation-Tool

This tool is a basic pentesting tool which aims at automating the processes of Nmap and Metasploit Framework. 

Prerequisites:

Python modules 
1. pymetasploit3

2. nmap
 
Before running the tool, run this command on the terminal:
msfrpcd -P your_password

For running the tool:
python3 ms.py

First, specify the ip address of the target machine and the script will scan through nmap and output the results in an external file. Then, the script analyses this file and asks the user what service they want to exploit. The script then outputs the options for that particular service in another file. The user has to choose and give the input, the index number of the exploit they want to use. The program will then run and give the user some choices for the type of payload to use.
The user will input the choice, after which the program can ask for additional information if required and then, the exploit is executed and if it is successful, a session is created and the user gets direct access to the target machine. 

Total three output files are generated:
1. nmap_output.csv: 
Contains information about the open ports and the services running on them

2. exploits.txt: 
Contains the exploits available for the service you select

3. logs.txt: 
This file will be generated if you are successful in gaining access to the target machine. It contains the commands ran by you on the machine and the output generated.   
