# Check the avaibility of crypto indirection #

print("Bonjour, bienvenue sur ParamsCheck")

list1 = ["1234567890B", "0987654321A", "2345678765C"]

def check():
    
    a = str(input("Importez votre chaine crypto : "))
    b = False
    l = []
    val = a in list1
    if val == False :
        print("Votre chaine est disponible !")
    else :
        print("Votre chaine est indisponible, vous devez en creer une nouvelle !")
        
    print(a)
    print("Fin de test, exit")
    return(a)

check()



