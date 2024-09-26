# Import libraries to work with web3

import string
from web3 import Web3
from eth_account.messages import encode_defunct
import json
import os
import time
import secrets


# Connect to Ethereum node (you can use Infura or a local node)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

def generate_nonce():
    return secrets.token_hex(16)

def generate_message():
    nonce = generate_nonce()
    message = f"Logging in to Canaanite Chronicles v0.1\n\n{nonce}"
    return message

def extract_account(original, signature):
    print(original)
    encoded = encode_defunct(text=original)
    print(encoded)
    return w3.eth.account.recover_message(encoded, signature=signature).upper()
