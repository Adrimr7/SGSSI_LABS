if __name__ == '__main__':
    mat = []
    i = ord('A')
    j = 0
    equi = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x']

    while i<=ord('A')+26:
        mat.append([j,i])
        i+=1
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            for letra in linea:
                if ord(letra)<92 and ord(letra)>65:
                    var = ord(letra)-65
                    mat[var] = [mat[var][0]+1, mat[var][1]]
    
    mat.sort(reverse=True, key=lambda x: x[0])
    a_y_e = [chr(mat[0][1]), chr(mat[1][1])]
    print(a_y_e)
    mat = [[sublista[1], sublista[0]] for sublista in mat]
    h = 0
    while h<len(equi):
        mat[h][1]= equi[h]
        h = h+1
    mat.sort(key=lambda x: x[0])
    print(mat)
    espec = ['J', 'Ñ', 'Z', 'X']
    val = ""
    texto = ""
    with open("archivo.txt", "r") as archivo:
                for linea in archivo:
                    for letra in linea:
                        if letra == a_y_e[0]:
                            texto = texto + 'e'
                        elif letra == a_y_e[1]:
                            texto = texto + 'a'
                        else:
                            texto = texto + letra


    print(texto)
    while val!="salir":
        print("Si quiere salir escriba :   salir   , en caso contrario, escriba una letra MAYÚSCULA.")
        val = str(input())
        if val != "salir":
            print("Introduzca otra letra MAYÚSCULA.")
            val2 = str(input())
            
            if val.isalpha() and val2.isalpha() and val2!= "salir":
                texto = texto.replace(val,val2)
                print("Texto NUEVO:" , "\n")
                print(texto)
        else:
            print("Acabando el programa")

