hotel = [[100,'livre'], 
         [101,'livre'], 
         [102,'livre'],  
         [103,'livre']]


def listar_quartos():


    print("=" *20)
    print ("Listagem dos quatos : \n" )
    for quartos in hotel:
        print (*quartos)
        print ()
    print ("=" * 20)
    return

def check_in():

    try:
        reserva = int(input("Digite o numero do quarto que deseja realizar o check-in: "))
    except ValueError:
        print ("Digite apenas numereos")
        return
    encontrado = False
    for quartos in hotel:
         
         if reserva == quartos[0]:
             
             encontrado = True
             if quartos[1] == 'livre':
                 
                 nome = input("Digite o nome do hóspede: ")
                 quartos[1] = nome.strip()

                 print (f"Check- in de {nome} realizado com sucesso!")
                 break
             
             else:
                 
                 print (f" O quarto Nr{reserva}, infelizmente se encontra ocupado!")
            
    if not encontrado:
        print ("Não encontrado!")
    return hotel
       
    
def check_out():
    
    nome = input("digite o nome do hóspede que deseja realizar Checkout: ").strip()

    
    encontrado = False 
    
    for quartos in hotel:
        if nome == quartos[1]:

            encontrado = True

            print("hospede encontrado")
            print ("Check-out realizado com sucesso!")
            
            quartos[1] = "livre"
            break

    
    if not encontrado:
        print("hospede não encontrado!")
    return hotel
    
        
def buscar():
    nome = input ("Qual hospede voce deseja procurar?  :").strip()
    
    encontrado = False
    
    for quarto in hotel:


        if nome == quarto[1]:
          print (f" O hospede {quarto[1]} esta hospedado no apartamento {quarto[0]} ")
          encontrado = True
          break
    if not encontrado:
        print ("Hospede não encontrado, tente novamente")

        

    

  



while True:
    menu = '''  
[1] Listar quartos
[2] Check-in 
[3] Check-out
[4] Buscar hóspede
[5] Sair
==>'''
   
    escolha = input (menu).strip()



    if escolha == "1":
        listar_quartos()
    elif escolha == "2":
        check_in()
    elif escolha == "3":
        check_out()
    elif escolha == "4":
        buscar()
    elif escolha == "5":
        break
    else:
        print("Opção ivalida")    
     


