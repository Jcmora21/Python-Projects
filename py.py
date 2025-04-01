def formatar_resultado(resultado):
    """ Retorna um número inteiro se possível, senão arredonda para 5 casas decimais """
    return int(resultado) if resultado == int(resultado) else round(resultado, 5)

def calcular():
    print("Selecione a operação:")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. :")
    print("5. ^2")
    
    escolha = input("Operação: ")
    
    if escolha in ('1', '2', '3', '4', '5', '+', '-', 'x', ':', '^2'):
        if escolha in ('5', '^2'):
            num = int(input("Digite um número: "))
            resultado = num * num
        else:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if escolha in ('1', '+'):
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
