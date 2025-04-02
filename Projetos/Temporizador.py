import time

def contador_regressivo():
    print("Escolha a unidade de tempo:")
    print("1. Segundos")
    print("2. Minutos")
    print("3. Horas")
    
    unidade = input("Escolha a unidade de tempo (1/2/3): ")
    
    if unidade == '1':
        tempo = int(input("Digite o tempo em segundos: "))
        while tempo > 0:
            mins, segs = divmod(tempo, 60)
            print(f"{mins:02}:{segs:02}")
            time.sleep(1)
            tempo -= 1
        print("Contagem regressiva finalizada!")
    
    elif unidade == '2':
        tempo = int(input("Digite o tempo em minutos: "))
        tempo = tempo * 60  # Converter minutos para segundos
        while tempo > 0:
            mins, segs = divmod(tempo, 60)
            print(f"{mins:02}:{segs:02}")
            time.sleep(1)
            tempo -= 1
        print("Contagem regressiva finalizada!")
    
    elif unidade == '3':
        tempo = int(input("Digite o tempo em horas: "))
        tempo = tempo * 3600  # Converter horas para segundos
        while tempo > 0:
            horas, resto = divmod(tempo, 3600)
            mins, segs = divmod(resto, 60)
            print(f"{horas:02}:{mins:02}:{segs:02}")
            time.sleep(1)
            tempo -= 1
        print("Contagem regressiva finalizada!")
    
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    contador_regressivo()
