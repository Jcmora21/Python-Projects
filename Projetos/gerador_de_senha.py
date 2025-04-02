import random
import string

def gerar_senha():
    while True:
        try:
            tamanho = int(input("Tamanho da senha? (4-12) : "))
            if 4 <= tamanho <= 12:
                break
            else:
                print("Coloque um número de 4 a 12.")
        except ValueError:
            print("Valor inserido é inválido.")
    
    incluir_numeros = input("Tem números? (S/N): ").strip().lower() == 's'
    incluir_simbolos = input("Tem símbolos? (S/N): ").strip().lower() == 's'

    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    gerar_senha()
