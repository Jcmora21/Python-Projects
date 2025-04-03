import os
import time

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def contador_regressivo():
    print("Escolha a unidade de tempo:")
    print("1. Segundos")
    print("2. Minutos")
    print("3. Horas")
    
    unidade = input("Escolha a unidade de tempo (1/2/3): ")
    
    if unidade == '1':
        tempo = int(input("Digite o tempo em segundos: "))
    elif unidade == '2':
        tempo = int(input("Digite o tempo em minutos: ")) * 60
    elif unidade == '3':
        tempo = int(input("Digite o tempo em horas: ")) * 3600
    else:
        print("Opção inválida. Tente novamente.")
        return
    
    limpar_console()  # Limpa o console antes de iniciar a contagem

    while tempo > 0:
        horas, resto = divmod(tempo, 3600)
        mins, segs = divmod(resto, 60)
        print(f"{horas:02}:{mins:02}:{segs:02}", end="\r")  # Atualiza a mesma linha
        time.sleep(1)
        tempo -= 1

    print("\nContagem regressiva finalizada!")

if __name__ == "__main__":
    contador_regressivo()
