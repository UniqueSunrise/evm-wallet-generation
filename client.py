import random

from web3 import Web3
from eth_account.signers.local import LocalAccount

from networks import Network, Networks


class Client:
    network: Network
    account: LocalAccount | None
    w3: Web3

    def __init__(
            self,
            private_key: str | None = None,
            network: Network = Networks.Goerli
    ):
        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri=network.rpc))

        if private_key:
            self.account = self.w3.eth.account.from_key(private_key=private_key)
        elif private_key is None:
            self.account = self.w3.eth.account.create(extra_entropy=str(random.randint(1, 999_999_999)))
        else:
            self.account = None
