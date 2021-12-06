print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    chutou_acima = chute > numero_secreto
    chutou_abaixo = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(chutou_acima):
            print("Você errou, o número secreto é menor!")
        elif(chutou_abaixo):
            print("Você errou, o número secreto é maior!")

print("Fim do jogo")