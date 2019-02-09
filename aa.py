import time
inicio = time.time()

arq = open('dataset-1-c.csv', 'r')
arq1 = arq.read()
g = open('filec.txt', 'a')
n = 10
cont = 0
for arq in arq1[0]:    
    linha = arq1.split()    
    if str(n) in linha:
        g.writelines(" True" + "\n" )        
    else:
        g.writelines(" False" + "\n" )


    
arq2 = arq1.split()
for i in range(len(arq2)):
    #print(i)
    if int(n) == int(arq2[i]):            
        g.writelines(str(cont) + "\n" )
        break
    elif int(n) != int(arq2[i]):
        cont+=1
        if cont + 1 > len(arq2):
            g.writelines(str(-1) + "\n" )                   

fim = time.time()
g.writelines(str(fim - inicio) + "\n" )                   
g.close()


