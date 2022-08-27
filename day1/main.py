#!/usr/bin/env python3
def step1(liste) :
  

    # print(datable)

    value = 0
    lastvalue = 0
    increased_counter = 0 

    for line in liste :
        
        value = int(line)
        
        if (lastvalue != 0) & (value > lastvalue) : 
        
            increased_counter += 1 
        
        
        lastvalue = value 
    return increased_counter
    # print(f"There's {increased_counter} increments")

def step2(liste) :
    
    increased_counter = 0

    for i in range(len(liste)-3) :
        A = int(liste[i]) + int(liste[i+1]) + int(liste[i+2])
        B = int(liste[i+1]) + int(liste[i+2]) + int(liste[i+3])

        if B > A :
            increased_counter += 1
    
    return increased_counter




with open("data.txt","r") as lesdatas :
        datable = lesdatas.read().split()

# step2(datable)

print(step2(datable))

