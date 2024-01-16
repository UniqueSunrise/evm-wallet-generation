import sys

import questionary
from questionary import Choice

from networks import Networks
from client import Client


def create_wallet(amount, param):
    for _ in range(amount):
        client = Client(network=Networks.Arbitrum)

        with open('success_wallets.txt', 'a') as f:
            if param == 1:
                f.write(f'{client.account.key.hex()}\n')
            elif param == 2:
                f.write(f'address - {client.account.address} | private key - {client.account.key.hex()}\n')

    print('Успешно!')


def get_module():

    result = questionary.select(
        "Выберите формат сохранения кошельков",
        choices=[
            Choice("1) Вывести только приватный ключ", 1),
            Choice("2) Вывести приватный ключ и адрес", 2),
            Choice("3) Выход / Exit", "exit"),
        ],
        qmark="🧐 ",
        pointer="🐸 "
    ).ask()
    if result == "exit":
        print("\n❤️Выход из программы\n")
        sys.exit()
    return result


def main(param):
    amount = int(input('Введите количество кошельков - '))
    create_wallet(amount, param)


if __name__ == '__main__':
    module = get_module()
    main(module)
