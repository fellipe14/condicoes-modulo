a = input("Digite a idade da pessoa: ")
idade = int (a)

if idade <=1:
    print ("Recém nascido")
else:
    if idade < 13:
        print ("Criança")
    else:
        if idade < 18:
            print ("Adolescente")
        else:
            if idade < 60:
                print ("Adulto")
            else:
                if idade < 80:
                    print ("Idoso")
                else:
                    print ("Longevo")


print ("Acabou.")