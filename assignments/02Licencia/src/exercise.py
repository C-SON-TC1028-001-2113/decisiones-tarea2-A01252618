def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    a = edad >= 18
    b = edad > 0
    if a and b : 
        ine = str(input("¿Tienes identificación oficial? (s/n): "))
        if ine == "s" :
            print ("Trámite de licencia concecido")
        elif ine == "n" : 
            print ("No cumples requisitos")
        else:
            print ("Respuesta incorrecta")
    if not a and b :
        print ("No cumples requisitos")
    if not b : 
        print ("Respuesta incorrecta")
   

if __name__=='__main__':
    main()
