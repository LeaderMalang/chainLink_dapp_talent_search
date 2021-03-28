import os
from brownie import  network,accounts,config,Hello


def main():
    my_account=accounts.add(os.genenv(config['wallets']['from_key']))
    print(my_account)

