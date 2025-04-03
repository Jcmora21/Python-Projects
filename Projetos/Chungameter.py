import random

def gerar_percentagem():
    print("|Chungameter|")
    name = input("Como te chamas?: ")
    
    porcentagens = {
        'Zé': 0, 
        'zé': 0,
        'ze': 0,
        'Ze': 0,
    }

    if name in porcentagens:
        porcentagem = porcentagens[name]
        print(f"Tu és {porcentagem}% chunga.")
    else:
        porcentagem = random.randint(0, 100)
        print(f"Tu {name}, és {porcentagem}% chunga.")

if __name__ == "__main__":
    gerar_percentagem()
