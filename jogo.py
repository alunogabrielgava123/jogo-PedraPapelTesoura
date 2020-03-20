import random
#instrucoes para que haja o jogo pedra papel tesoura 

name = input("jogo (pedra papel e tisoura) vc escolhe?")

def number_to_name(number):
    if(number == 0):
        return  "pedra"
    elif (number == 1):
        return "papel"
    elif number == 2 :
        return "tesoura"
   
def name_to_number(name):
    if(  name == "pedra"):
        return 0
    elif ( name == "papel"):
        return 1
    elif name == "tesoura":
        return 2

def jogo_pedra_papel_tesoura(name):
    player_number = name_to_number(name)
    print("player escolheu:",name)
    
    comp_number = random.randrange(0,3)
    comp_number_view = number_to_name(comp_number)
    print("Computador escolheu:" , comp_number_view)
    
 
    if(comp_number + 1) % 3 == player_number:
        print("player ganhou")
    elif (comp_number == player_number):
        print("empate")
    else:
        print('Computador ganhou')

print(jogo_pedra_papel_tesoura(name))















        
    

    





