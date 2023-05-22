from conta import Conta
import os
import time
from cryptography.fernet import Fernet
os.system('cls' if os.name == 'nt' else 'clear')

# Defining - 
acountDataList = []

# Encripting acount info - 
def writeKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

if os.path.isfile('key.key'):
    with open('key.key', 'rb') as acountData:
        acountData.seek(0, os.SEEK_END)
        isempty = acountData.tell() == 0
        acountData.seek(0)
    if isempty == False:
        key = load_key()
else:
    writeKey()
    key = load_key()

fer = key
fer = Fernet(key)

# Functions -
def checkAcount():
    if os.path.isfile('acount.txt'):
        with open('acount.txt', 'r') as acountData:
            acountData.seek(0, os.SEEK_END)
            isempty = acountData.tell() == 0
            acountData.seek(0)
        if isempty == False:
            with open("acount.txt", "r", encoding='utf=8') as data:
                for lines in data.readlines():
                    acountData, space = lines.split('\n')
                    acountDataList.append(acountData)
                return createAcountFromData(acountDataList)
    else:
        return createAcount()

def createAcountFromData(dataList):
    nome = dataList[0]
    CPF = int(fer.decrypt(dataList[1].encode()).decode())
    idade = int(dataList[2])
    saldo = int(fer.decrypt(dataList[3].encode()).decode())
    limite = int(fer.decrypt(dataList[4].encode()).decode())

    return Conta(nome, CPF, idade, saldo, limite)

def createAcount():
    print('Seja bem-vindo novo cliente!\n\nJá criaremos sua conta, primeiro precisamos de alguns dados pessoais:\n')
    nome = validateName()
    CPF = validateCPF()
    idade = validateAge()

    clearTerminal()
    return Conta(nome, CPF, idade, 150, 1000)

def clearTerminal():
    input('\nEnter continua...')
    os.system('cls' if os.name == 'nt' else 'clear')

def validateName():
    while True:
        nome = input(f'Nome completo: ').strip().title()
        if nome == '' or len(nome) < 8 or ' ' not in nome:
            print('\033[31mInsira seu nome completo!\033[0m')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            return nome

def validateCPF():
    while True:
        CPF = input(f'CPF \033[31m(APENAS NÚMEROS!)\033[0m: ')
        if CPF.isdigit and len(CPF) == 11:
            return CPF
        else:
            print('\033[31mCPF inválido!\033[0m')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

def validateAge():
    while True:
        idade = input('Idade: ')
        if idade.isdigit and len(idade) < 3:
            return idade
        elif int(idade) < 18:
            print('Você é muito novo para criar conta!')
            exit()
        else:
            print('\033[31mIdade inválida!\033[0m')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

def firstName():
    nomes = conta.nome.split(' ')
    return nomes[0]

def depositMoney():
    while True:
        print('\nQuanto você deseja depositar em sua conta?')
        quantidade = input('R$ ')
        if quantidade.isdigit():
            conta.depositar(int(quantidade))
            break
        else:
            print('\033[31mQuantidade inserida inválida!\033[0m')
            os.system('cls' if os.name == 'nt' else 'clear')

def withdrawMoney():
    while True:
        print('\nQuanto você deseja sacar?')
        quantidade = input('R$ ')
        if quantidade.isdigit():
            conta.sacar(int(quantidade))
            break
        else:
            print('\033[31mQuantidade inserida inválida!\033[0m')
            os.system('cls' if os.name == 'nt' else 'clear')

def exitProgram():
    print('\n\033[32mObrigado por utilizar nosso aplicativo!\033[0m\nVolte sempre 😁')
    time.sleep(2)
    acountDataList = []
    acountDataList.append(conta.nome)
    acountDataList.append(fer.encrypt(str(conta.CPF).encode()).decode())
    acountDataList.append(conta.idade)
    acountDataList.append(fer.encrypt(str(conta.saldo).encode()).decode())
    acountDataList.append(fer.encrypt(str(conta.limite).encode()).decode())
    with open('acount.txt', 'w', encoding='utf=8') as acountData:
        for data in acountDataList:
            acountData.write(str(data) + '\n')
    exit()

# Main -
print('\033[35mGerenciamento bancário\n\033[0m')

conta = checkAcount()

print(f'\033[32mBem-vindo\033[0m a sua conta \033[35m{firstName()}!\033[0m\n')

while True:
    print(
        'O que você deseja fazer?\n\n\033[34m[1] Consultar saldo.\n\033[32m[2] Depositar dinheiro.\n\033[31m[3] Sacar dinheiro.\n\033[1;30m[4] Sair do programa.\033[0m')
    modo = input('> ')

    match(modo):
        case '1':
            conta.consultar()
        case '2':
            depositMoney()
        case '3':
            withdrawMoney()
        case '4':
            exitProgram()
        case _:
            print('\033[31mModo inválido!\033[0m\nTente novamente.')

    clearTerminal()