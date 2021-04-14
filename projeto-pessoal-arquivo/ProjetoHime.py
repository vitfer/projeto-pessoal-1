from time import sleep
from random import randint
from datetime import datetime
import os

nome = ''
while nome != 'NOME':
    nome = str(input('Identifique-se: ')).strip().upper()

sleep(1)
os.system('cls')
print('VERIFICANDO...')
sleep(1)
os.system('cls')
sleep(1)
print('BEM - VINDO!')
sleep(1)
os.system('cls')

while True:
    print('O que deseja? \n[ 1 ] = Operações Aritméticas '
      '\n[ 2 ] = Jogos '
      '\n[ 3 ] = Data e Hora '
      '\n[ 4 ] = Conversor de Moedas '
      '\n[ 0 ] = Sair')  # Menú

    menu = int(input('Opção: '))
    os.system('cls')

    if menu == 1:
        sleep(0.5)
        print('Entendido...')
        sleep(1)
        os.system('cls')
        print('Esses são as Operações: \n[ 1 ] = Soma '
              '\n[ 2 ] = Subtração '
              '\n[ 3 ] = Multiplicação '
              '\n[ 4 ] = Divisão'
              '\n[ 5 ] = Cálculo de IMC'
              '\n[ 6 ] = Sequência de Fibonacci'
              '\n[ 7 ] = Tabuadas'
              '\n[ 0 ] = Voltar')
        menu1 = int(input('O que escolhe?: '))
        os.system('cls')
        
        while True:
            if menu1 == 1:  # Soma
                sleep(1)
                print('Vamos Somar!!!')
                sleep(1)
                num1_soma = int(input('Digite o primeiro valor: '))
                num2_soma = int(input('Digite o segundo valor: '))
                result_soma = num1_soma + num2_soma
                print(f'A soma entre {num1_soma} e {num2_soma} é igual a {result_soma}.')
                resp_soma = ' '

                while resp_soma not in 'SN':
                    resp_soma = str(input('Quer somar novamente? [S/N]: ')).strip().upper()[0]

                os.system('cls')

                if resp_soma == 'N':
                    os.system('cls')
                    print('Voltando...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 2:  # Subtração
                sleep(1)
                print('Vamos Subtrair!!!')
                sleep(1)
                num1_subt = int(input('Digite o primeiro valor: '))
                num2_subt = int(input('Digite o segundo valor: '))
                result_subt = num1_subt - num2_subt
                print(f'{num1_subt} - {num2_subt} é igual a {result_subt}.')
                resp_subt = ' '

                while resp_subt not in 'SN':
                    resp_subt = str(input('Quer subtrair novamente? [S/N]: ')).strip().upper()[0]

                os.system('cls')

                if resp_subt == 'N':
                    os.system('cls')
                    print('Voltando...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 3:  # Multiplicação
                sleep(1)
                print('Vamos Multiplicar!!!')
                sleep(1)
                num1_mult = float(input('Digite o primeiro valor: '))
                num2_mult = float(input('Digite o segundo valor: '))
                result_mult = num1_mult * num2_mult
                print(f'{num1_mult} x {num2_mult} é igual a {result_mult}.')
                resp_mult = ' '

                while resp_mult not in 'SN':
                    resp_mult = str(input('Quer multiplicar novamente? [S/N]: ')).strip().upper()[0]

                os.system('cls')

                if resp_mult == 'N':
                    os.system('cls')
                    print('Voltando...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 4:  # Divisão
                sleep(1)
                print('Vamos Dividir!!!')
                sleep(1)
                num1_div = float(input('Digite o primeiro valor: '))
                num2_div = float(input('Digite o segundo valor: '))
                resut_div = num1_div / num2_div
                print(f'{num1_div} divido por {num2_div} é igual a {resut_div:.2f}.')
                resp_div = ' '

                while resp_div not in 'SN':
                    resp_div = str(input('Quer dividir novamente? [S/N]: ')).strip().upper()[0]

                os.system('cls')

                if resp_div == 'N':
                    os.system('cls')
                    print('Voltando...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 5:  # Cálculo de IMC
                sleep(1)
                print('Cálculo de IMC!!!')
                sleep(1)
                peso = float(input('Digite seu peso em Kg: '))
                altura = float(input('Digite sua altura em metros (Ex.: 1.80): '))
                imc = peso / altura ** 2
                print(f'Seu IMC é de: {imc:.1f}.')

                if imc < 18.5:
                    print('Você está ABAIXO do seu peso ideal!')
                elif imc >= 18.5 and imc < 25:
                    print('Você está no seu PESO IDEAL!')
                elif imc >= 25 and imc < 30:
                    print('Você está com SOBREPESO!')
                elif imc >= 30 and imc < 40:
                    print('Você está com OBESIDADE!')
                else:
                    print('Você está com OBESIDADE MÓRBIDA, cuidado!')

                resp_imc = ' '

                while resp_imc not in 'SN':
                    resp_imc = str(input('Deseja consultar novamente? [S/N]: ')).strip().upper()[0]

                os.system('cls')

                if resp_imc == 'N':
                    os.system('cls')
                    print('VOLTANDO...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 6:  # Sequência de Fibonacci
                sleep(1)
                print('Sequência de Fibonacci!!!')
                sleep(1)
                print('-' * 30)
                print('Sequência de Fibonacci')
                print('-' * 30)
                qnt_termos = int(input('Quantos termos você quer mostrar?: '))
                termo1 = 0
                termo2 = 1
                print('~' * 30)
                print('{} - {}'.format(termo1, termo2), end='')
                cont = 3

                while cont <= qnt_termos:
                    termo3 = termo1 + termo2
                    print(' - {}'.format(termo3), end='')
                    termo1 = termo2
                    termo2 = termo3
                    cont += 1

                print(' - FIM')
                print('~' * 30)

                while True:
                    resp = str(input('Quer ver novamente? [S/N]: ')).upper()[0]

                    if resp in 'SN':
                        break

                os.system('cls')

                if resp == 'N':
                    os.system('cls')
                    print('Voltando...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 7:  # Tabuadas
                sleep(1)
                print('Tabuadas!!!')
                sleep(1)
                tab_num = int(input('Quer ver a tabuada de qual número?: '))
                sleep(1)
                print(f'Preparando a tabuada de {tab_num}')
                sleep(1)
                print('-' * 30)

                for c in range(1, 11):
                    print(f'{tab_num} x {c} = {tab_num * c}')

                print('-' * 30)

                while True:
                    resptab = str(input('Quer continuar? [S/N]: ')).upper()[0]
                    if resptab in 'SN':
                        break
                    
                os.system('cls')

                if resptab == 'N':
                    os.system('cls')
                    sleep(1)
                    print('FECHANDO...')
                    sleep(1)
                    os.system('cls')
                    break

            if menu1 == 0:  # Sair
                print('Voltando...')
                sleep(1)
                os.system('cls')
                break
                
    if menu == 2:
        sleep(0.5)
        print('Entendido...')
        sleep(1)
        os.system('cls')
        print('Esses são os Jogos: \n[ 1 ] = Adivinhação '
                '\n[ 2 ] = Jokenpo '
                '\n[ 3 ] = Par ou Ímpar '
                '\n[ 0 ] = Voltar')
        menu2 = int(input('O que iremos jogar? '))
        os.system('cls')
        while True:
            if menu2 == 1: # Jogo da Adivinhação
                sleep(1)
                print('Vamos jogar Adivinhação!!!')
                sleep(1)
                computador = randint(0, 10)  # Faz o computador "PENSAR"
                print('Acabei de pensar em um número entre 0 e 10.')
                print('Será que você consegue adivinhar qual foi o número que eu pensei? ')
                acertou = False
                palpites = 0
                while not acertou:
                    jogador = int(input('Qual é o seu palpite? '))
                    palpites += 1
                    sleep(1)
                    if jogador == computador:
                        acertou = True
                    else:
                        if jogador < computador:
                            print('Mais...Tente novamente.')
                        elif jogador > computador:
                            print('Menos...Tente novamente.')
                sleep(1)
                print('Acertou com {} tentativas. Parabéns!'.format(palpites))
                print('...')
                sleep(1)
                adv1 = str(input('Quer jogar novamente? [S/N] ')).strip().upper()[0]
                os.system('cls')
                if adv1 == 'N':
                    print('Saindo...')
                    sleep(1)
                    os.system('cls')
                    break
            if menu2 == 2: #Jokenpo
                sleep(1)
                print('Vamos jogar Jokenpo!!!')
                sleep(1)
                itens = ('Pedra', 'Papel', 'Tesoura')
                sleep(1)
                computadorjk = randint(0, 2)
                print('''Suas opções:
                    [ 0 ] PEDRA
                    [ 1 ] PAPEL
                    [ 2 ] TESOURA''')
                jogadorjk = int(input('Qual é a sua jogada? '))
                sleep(1)
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!!')
                print('-=' * 11)
                print('Eu joguei {}'.format(itens[computadorjk]))
                print('Você jogou {}'.format(itens[jogadorjk]))
                print('-=' * 11)
                if computadorjk == 0:  # computador jogou PEDRA
                    if jogadorjk == 0:
                        print('EMPATE!!!')
                    elif jogadorjk == 1:
                        print('VOCÊ VENCEU!!!')
                    elif jogadorjk == 2:
                        print('EU VENCI!!!')
                    else:
                        print('JOGADA INVÁLIDA')
                elif computadorjk == 1:  # computador jogou PAPEL
                    if jogadorjk == 0:
                        print('EU VENCI!!!')
                    elif jogadorjk == 1:
                        print('EMPATE!!!')
                    elif jogadorjk == 2:
                        print('VOCÊ VENCEU!!!')
                    else:
                        print('JOGADA INVÁLIDA')
                elif computadorjk == 2:  # computador jogou TESOURA
                    if jogadorjk == 0:
                        print('VOCÊ VENCEU!!!')
                    elif jogadorjk == 1:
                        print('EU VENCI!!!')
                    elif jogadorjk == 2:
                        print('EMPATE!!!')
                    else:
                        print('JOGADA INVÁLIDA')
                escolhajk = str(input('Vamos denovo? [S/N] ')).strip().upper()[0]
                os.system('cls')
                if escolhajk == 'N':
                    print('Ok! Saindo...')
                    sleep(1)
                    os.system('cls')
                    break
            if menu2 == 3: # Jogo do Par ou Ímpar
                sleep(1)
                print('Vamos jogar Par ou Ímpar!!!')
                sleep(1)
                jogadorpi = int(input('Diga um valor: '))
                computadorpi = randint(0, 10)
                totalpi = jogadorpi + computadorpi
                tipopi = ' '
                while tipopi not in 'PI':
                    tipopi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
                sleep(1)
                print(f'Você jogou {jogadorpi} e eu joguei {computadorpi}. Total de {totalpi} ', end='')
                print('DEU PAR' if totalpi % 2 == 0 else 'DEU ÍMPAR')
                if tipopi == 'P':
                    if totalpi % 2 == 0:
                        print('Você venceu! Parabéns!')
                    else:
                        print('Venci! EBAAAA!')
                elif tipopi == 'I':
                    if totalpi % 2 == 1:
                        print('Você VENCEU!')
                    else:
                        print('Você PERDEU!')
                sleep(1)
                escolhapi = str(input('Vamos jogar novamente? [S/N] ')).strip().upper()[0]
                os.system('cls')
                if escolhapi == 'N':
                    print('Tudo Bem! Saindo...')
                    sleep(1)
                    os.system('cls')
                    break
            if menu2 == 0: #Voltando ao Menu Principal
                print('Voltando...')
                sleep(1)
                os.system('cls')
                break
    if menu == 3: # Data e Hora atuais
        sleep(0.5)
        print('Entendido...')
        sleep(1)
        os.system('cls')
        print('Data e Hora!!!')
        sleep(1)
        os.system('cls')
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('Data: %d/%m/%Y \nHora: %H:%M')
        print(data_e_hora_em_texto)
        sleep(5)
        os.system('cls')
    if menu == 4: # Conversor de Moedas
        while True:
            sleep(1)
            print('Conversor...!!!')
            sleep(1)
            os.system('cls')
            print('Escolha dentre as opções qual a moeda que deseja fazer a conversão:'
                  '\n[1] Real'
                  '\n[2] Dolar'
                  '\n[3] Euro'
                  '\n[4] Iene'
                  '\n[5] Won'
                  '\n[6] Libra Esterlina'
                  '\n[0] Sair')
            escolhamoeda = int(input('Sua escolha: '))
            if escolhamoeda == 0:
                break
            if escolhamoeda == 1:
                real = float(input('\nQual o valor para conversão? R$'))
                dolar = real / 5.26
                euro = real / 6.26
                iene = real / 0.050
                won = real / 0.0047
                libra = real / 6.94
                sleep(0.5)
                print('Fazendo a conversão...')
                sleep(1)
                print('O valor em Dólar é US${:.2f}, '
                      '\nEm Euro é €{:.2f}, '
                      '\nEm Iene é ¥{:.2f}, '
                      '\nEm Won é ₩{:.2f} e '
                      '\nEm Libra Esterlina é £{:.2f}'.format(dolar, euro, iene, won, libra))
            if escolhamoeda == 2:
                dolar = float(input('\nQual o valor para conversão? US$'))
                real = dolar / 0.19
                euro = dolar / 1.19
                iene = dolar / 0.0095
                won = dolar / 0.00090
                libra = dolar / 1.32
                sleep(0.5)
                print('Fazendo a conversão...')
                sleep(1)
                print('O valor em Real é R${:.2f}, '
                      '\nEm Euro é €{:.2f}, '
                      '\nEm Iene é ¥{:.2f}, '
                      '\nEm Won é ₩{:.2f} e '
                      '\nEm Libra Esterlina é £{:.2f}'.format(real, euro, iene, won, libra))
            if escolhamoeda == 3:
                euro = float(input('\nQual o valor para conversão? €'))
                real = euro / 0.16
                dolar = euro / 0.84
                iene = euro / 0.0080
                won = euro / 0.00075
                libra = euro / 1.11
                sleep(0.5)
                print('Fazendo a conversão...')
                sleep(1)
                print('O valor em Real é R${:.2f}, '
                      '\nEm Dólar é US${:.2f}, '
                      '\nEm Iene é ¥{:.2f}, '
                      '\nEm Won é ₩{:.2f} e '
                      '\nEm Libra Esterlina é £{:.2f}'.format(real, dolar, iene, won, libra))
            if escolhamoeda == 4:
                iene = float(input('\nQual o valor para conversão? ¥'))
                real = iene / 19.86
                dolar = iene / 105.22
                euro = iene / 125.02
                won = iene / 0.094
                libra = iene / 138.67
                sleep(0.5)
                print('Fazendo a conversão...')
                sleep(1)
                print('O valor em Real é R${:.2f}, '
                      '\nEm Dólar é US${:.2f}, '
                      '\nEm Euro é €{:.2f}, '
                      '\nEm Won é ₩{:.2f} e '
                      '\nEm Libra Esterlina é £{:.2f}'.format(real, dolar, euro, won, libra))
            if escolhamoeda == 5:
                won = float(input('\nQual o valor para conversão? ₩'))
                real = won / 210.69
                dolar = won / 1117.12
                euro = won / 1325.42
                iene = won / 10.61
                libra = won / 1470.78
                sleep(0.5)
                print('Fazendo a conversão...')
                sleep(1)
                print('O valor em Real é R${:.2f}, '
                      '\nEm Dólar é US${:.2f}, '
                      '\nEm Euro é €{:.2f}, '
                      '\nEm Iene é ¥{:.2f} e '
                      '\nEm Libra Esterlina é £{:.2f}'.format(real, dolar, euro, iene, libra))
            if escolhamoeda == 6:
                libra = float(input('\nQual o valor para conversão? £'))
                real = libra / 0.14
                dolar = libra / 0.76
                euro = libra / 0.90
                iene = libra / 0.0072
                won = libra / 0.00068
                sleep(0.5)
                print('Fazendo a conversão...')
                sleep(1)
                print('O valor em Real é R${:.2f}, '
                      '\nEm Dólar é US${:.2f}, '
                      '\nEm Euro é €{:.2f}, '
                      '\nEm Iene é ¥{:.2f} e '
                      '\nEm Wom é ₩{:.2f}'.format(real, dolar, euro, iene, won))
            sleep(1)
            menu05 = str(input('\nQuer ver outro valor? [S/N} ')).strip().upper()[0]
            os.system('cls')
            while menu05 not in 'SN':
                menu05 = str(input('\nQuer ver outro valor? [S/N} ')).strip().upper()[0]
            if menu05 == 'N':
                break
        print('Saindo do Conversor...')
        sleep(1)
        os.system('cls')
    if menu == 0:
        break
sleep(1)
print('Hmmmmm...')
sleep(1)
print('Ok!')
sleep(1)
print('ATÉ MAIS!')
sleep(1)
