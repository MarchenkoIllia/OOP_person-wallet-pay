# Создать класс Wallet (кошелек).
# Создать класс Pay с методом оплаты с аргументом объекта Person и суммой покупки. 
# При недостаточном количестве средств в кошельке его значение не меняется и выводится соответствующее сообщение. 
# Если средств достаточно, то эта сумма списывается с кошелька пользователя  

class Wallet:
    def __init__(self, wallet_cash) -> None:
        self.__wallet_cash = wallet_cash
    
    def Get_Cash(self):
        return self.__wallet_cash
    
    def Set_Cash(self, val):
        self.__wallet_cash = val

    def __str__(self) -> str:
        return f'Балланс счёта: {self.__wallet_cash}'

class Pay:
    def __init__(self, value) -> None:
        self.value = value
    
    def toPay(self, wallet: Wallet):
        if self.value <= wallet.Get_Cash():
            wallet.Set_Cash(wallet.Get_Cash() - self.value)
            print(f'Вы купили товар за {self.value}')
        else:
            print('Недостаток средств')

wal1 = Wallet(100)
pay1 = Pay(20)

print(wal1)
pay1.toPay(wal1)
print(wal1)

