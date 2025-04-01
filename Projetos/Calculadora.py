def formatar_resultado(resultado):
    return int(resultado) if resultado == int(resultado) else round(resultado, 5)

def calcular():
    print("Selecione a operação:")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. :")
    print("5. ^2")
    print("6. Raiz quadrada")

    escolha = input("Operação: ")
    
    if escolha in ('1', '2', '3', '4', '5', '6', '+', '-', 'x', ':', '^2'):
        num1 = float(input("Primeiro número: "))

        if escolha == '6':  # Caso de raiz quadrada
            if num1 < 0:
                print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
                return
            resultado = num1 ** 0.5  # Raiz quadrada
        else:
            num2 = float(input("Segundo número: "))
            if escolha in ('5', '^2'):
                resultado = num1 ** num2  # Potência
            elif escolha in ('1', '+'):
                resultado = num1 + num2
            elif escolha in ('2', '-'):
                resultado = num1 - num2
            elif escolha in ('3', 'x'):
                resultado = num1 * num2
            elif escolha in ('4', ':'):
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    return

        print(f"Resultado: {formatar_resultado(resultado)}")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calcular()
