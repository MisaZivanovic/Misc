import random
import time

misc = [
    "Ko je sa mnom u studiju?",
    "Sta cemo sad?", #(ovo moze da ti bude centralni deo petlje. I conversation starter i escape exit
    
]

predkraj = "Javite nam kad bude nesto novo da to ispromovisemo"

odg = "Znaci imate kilometrazu" 

vladina_lista = [
    "Sta vi svirate?",
    "Koliko dugo bend postoji?",
    "Na kom jeziku pevate?", 
    "A je l' mora bas na engleskom?",
    "Je l ovaj singl uvod u album?",
    "Da li planirate video-prezentaciju?",
    "Je l svirate u-zivo?",
    "Kako publika reaguje na autorske pesme?",
    "Da li planirate promotivni koncert?",
    "Kako ide promocija preko inter-neta i drustvenih mreza?"
]

j=0
gost=""

print(random.choice(misc))

rnd=""


while gost != predkraj:
    input()
    
    if j in range(9,11):
        print(random.choice(misc))
        input()
        
    elif j == 20:
        print(misc[1])
        input()
        print(predkraj)
        input()
        gost=predkraj
        break
        
    else:
        pass
    if rnd =="":
        pass
    
    elif rnd == vladina_lista[2]:
        print(vladina_lista[3])
        print()
        #time.sleep(2)
        input()
        
    elif rnd == vladina_lista[1]:
        print(odg)
        print()
        time.sleep(1)
        
    j+=1    
    
    rnd=random.choice(vladina_lista)
    
    print(rnd)
