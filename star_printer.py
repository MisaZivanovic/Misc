u_lista="*"*5
for num in range(len(u_lista)):
    if num==2:      
        k_lista=[]
        for i in range(1,len(u_lista)+1):
            if i%2 == 0:
                k_lista.append(u_lista[i-1].replace("*", "_"))
            else:
                k_lista.append(u_lista[i-1])
        print("".join(k_lista))
    elif num ==1 or num ==3:
        j_lista=list(u_lista)
        j_lista[len(u_lista)-int(len(u_lista)/2+1)]="_"
        j_lista[num]="_"
        print("".join(j_lista))    
    else:
        print(u_lista)

    
