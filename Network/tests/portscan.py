import os 
os.system ("apt-get install figlet")
os.system("clear")
os.system("figlet PORT SCAN")
print("""
Welcome to Port Scan )

1) 1.level scan
2) 2.level scan
3) 3.level scan
  
  
"""
)

TARGET_IP_PROMPT = "Enter The Target Ip : "

ordernum =input("What level should the scan be ? ")

if(ordernum == "1"):
  targetip = input(TARGET_IP_PROMPT)
  os.system("nmap " + targetip)
  
elif(ordernum == "2"):
  targetip = input(TARGET_IP_PROMPT)
  os.system("nmap -sS -sV " + targetip)
  
elif(ordernum == "3"):
  targetip = input(TARGET_IP_PROMPT)
  os.system("nmap -o " + targetip)
  
else:
  print("There is no such command, choose one of them: 1, 2, 3")
  
  
