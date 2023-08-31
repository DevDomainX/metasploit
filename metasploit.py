#!/usr/bin/env python3
import os
from time import sleep
from colorama import init, Fore, Style 

title = Fore.BLUE+Style.BRIGHT+"""
    #############################
    ||     Created by : 1LugarParaProgramar  ||
    ||                                                                   ||
    ||    Author : Hans Saldias                          ||
    ||                                                                   ||
    ||   Script :  Intalar metasploit in termux  ||
    ||                                                                   ||
    ############################  
    """
    
for i in title:
   print(i, end='', flush= True)
   sleep(0.1)
   
op = input("Desea Intalar METASPLOIT (s/n): => ")
if op == "y" :
    print("Dando permiso de almacenamiento")
    sleep(3)
    os.system("termux-setup-stotage")
    print("Actualizando...")
    sleep(3)
    os.system("apt update && apt upgrade")
    print("Intalando wget ...")
    sleep(2)
    os.system("pkg install wget")
    print("Intalando metasploit....")
    sleep(3)
    os.system("wget http://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
    os.system("cd metasploit-framework")
    print("Dando permiso de ejecucion...")
    sleep(2)
    os.system("chmod +x metasploit.sh")
    print("Abriendo ...")
    sleep(3)
    os.system("./metasploit.sh")
    print("Abriendo msfconsole...")
    sleep(3)
    os.system("msfconsole")
else:
    print("Gracias 1LugarParaProgramar")