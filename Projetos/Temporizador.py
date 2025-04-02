def tabuada():
    
    while True:
        try:
            numero = int(input("Qual a tabuada?: "))
            break
        except ValueError:
            print("Valor inválido. Tem de ser um número inteiro.")
            
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
if __name__ == "__main__":
    tabuada()
