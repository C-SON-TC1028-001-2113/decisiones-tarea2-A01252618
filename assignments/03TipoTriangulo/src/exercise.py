def main():
    #escribe tu código abajo de esta línea
    a =int(input('Ingresa la medida del lado 1: '))
    b =int(input('Ingresa la medida del lado 2: '))
    c =int(input('Ingresa la medida del lado 3: '))
    if a > 0 and b > 0 and c > 0: 
        if a + b > c and a + c > b and b + c > a : 
            if a == b and a == c :
                print('ES UN TRIANGULO EQUILATERO')
            elif a == b or a == c or b == c : 
                print ('ES UN TRIANGULO ISOSCELES')
            else : 
                print ('ES UN TRIANGULO ESCALENO')
        else : 
            print ('NO ES TRIANGULO')
    else:
        print ('NO ES TRIANGULO')
    
if __name__=='__main__':
    main()
