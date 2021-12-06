print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

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