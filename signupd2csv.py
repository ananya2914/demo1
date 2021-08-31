# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:40:08 2021

@author: ADMIN
"""

import csv
import os
import login1 as l
os.chdir("C://Users//ADMIN//Desktop//Pranaya//open at your own risk//Computer//majorstuff")
def display():
    print("---------SIGN UP-------------")
    e=input("Mobile number or email\n")
    name=input("Full name\n")
    un=input("username\n")
    password=input("password\n")
    phoneno=email=''
    with open("logind2.csv","a") as f:
        s=csv.writer(f)    
        # s.writerow(["phone number","email","name","username","password"])
        
    if(l.checkpassword(password) and (l.checkno(e)==1 or l.checkemail(e)==1)):
                
        if(l.checkno(e)==1):
            phoneno=e
            # print("phone no was entered")
            # with open("logind2.csv","a",newline="") as f:
            #     s=csv.writer(f)
            #     s.writerow([e,'\t'])
                
            
        elif(l.checkemail(e)==1):
            email=e
            # print("email was entered")
            # with open("logind2.csv","a",newline='') as f:                
            #     s=csv.writer(f)               
            #     s.writerow(["\t",e])
                             
                
        with open("logind2.csv","a",newline="") as f:
            s=csv.writer(f)  
            
            s.writerow([phoneno,email,name,un,password])                  
            
              
    else:
        print("Enter valid data")
    f.close()
  

display()
