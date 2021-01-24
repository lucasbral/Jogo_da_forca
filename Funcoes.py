def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

def gerapalavra ():

    import random
    v=[]
    a=""
    file = open("palavras.txt", "r")
    for linha in file:
        a+=str(linha)
    file.close()
    v = a.split("\n")
    return (random.choice(v))

def transformastr (x):

    string=""
    for i in range(len(x)):
       string += x[i]
       string += " "
    return string