from cliente import Cliente

class Conta(Cliente):
    def __init__(self, nome, CPF, idade, saldo, limite):
        super().__init__(nome, CPF, idade)
        self.saldo = saldo
        self.limite = limite

    def sacar(self, quantidade):
       if quantidade > self.saldo or quantidade == 0:
           print('\033[31mSaque inválido!\033[0m')
       else:
            confirm = input(f'Têm certeza que deseja sacar \033[31mR$ {quantidade:.2f}\033[0m? ').strip().lower()
            if confirm == '' or confirm[0] in 'ys':
                self.saldo -= quantidade
                print(f'\n\033[31mVocê sacou R$ {quantidade:.2f}\033[0m\nAgora seu saldo atual é \033[34mR$ {self.saldo:.2f}.\033[0m')
    
    def depositar(self, quantidade):
        confirm = input(f'Têm certeza que deseja depositar \033[32mR$ {quantidade:.2f}\033[0m em sua conta? ').strip().lower()
        if confirm == '' or confirm[0] in 'ys':
            if self.saldo + quantidade <= self.limite:
                self.saldo += quantidade
                print(f'\n\033[32mR$ {quantidade:.2f} depositados!\033[0m\nSeu saldo agora é \033[34mR$ {self.saldo:.2f}\033[0m')
            else:
                print(f'Você possuí um limite de {self.limite}, por isso será impossível completar este deposíto!')
        else:
            print('\033[31mDeposito cancelado.\033[0m')

    def consultar(self):
        print(f'\n--------------\nSeu saldo atual é \033[34mR$ {self.saldo:.2f}\033[0m\n--------------\n')