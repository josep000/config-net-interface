
valor = "255.255.1"




def validateAddress(value):
    separador = "."

    separadorCount = value.count(separador)
    listValue = value.split(separador)
    countSub = 0

    for i in listValue:
        if int(i) <= 255 and int(i) >= 0:
            print (i)
            countSub = countSub + 1

    print (listValue)
    # print (len(valorSeparado))
    print (countSub)
    print (separadorCount)
    
    if countSub == 4 and separadorCount == 3:
        return True
    else:
        return False
    
print (validateAddress(valor))