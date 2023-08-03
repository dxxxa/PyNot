import codecs
import hashlib
import base58
import ecdsa
import requests
from Crypto.Hash import keccak  # pip install pycryptodome
from colorama import Fore


class EthereumBrainWallet:
    @staticmethod
    def generate_address_from_passphrase(passphrase):
        private_key = str(hashlib.sha256(passphrase.encode('utf-8')).hexdigest())
        return private_key

    @staticmethod
    def generate_address_from_private_key(private_key):
        public_key = EthereumBrainWallet.__private_to_public(private_key)
        address = EthereumBrainWallet.__public_to_address(public_key)
        return address







    @staticmethod
    def checksum_address(address):
        checksum = '0x'
        # Remove '0x' from the address
        address = address[2:]
        address_byte_array = address.encode('utf-8')
        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update(address_byte_array)
        keccak_digest = keccak_hash.hexdigest()
        for i in range(len(address)):
            address_char = address[i]
            keccak_char = keccak_digest[i]
            if int(keccak_char, 16) >= 10:
                checksum += address_char.upper()
            else:
                checksum += str(address_char)
        return checksum

    @staticmethod
    def __private_to_public(private_key):
        private_key_bytes = codecs.decode(private_key, 'hex')
        # Get ECDSA public key
        key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
        key_bytes = key.to_string()
        public_key = codecs.encode(key_bytes, 'hex')
        return public_key

    @staticmethod
    def __public_to_address(public_key):
        public_key_bytes = codecs.decode(public_key, 'hex')
        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update(public_key_bytes)
        keccak_digest = keccak_hash.hexdigest()
        # Take last 20 bytes
        wallet_len = 40
        wallet = '0x' + keccak_digest[-wallet_len:]
        return wallet