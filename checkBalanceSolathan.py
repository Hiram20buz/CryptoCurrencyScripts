#pip install solathon
from solathon import Client, PublicKey

client = Client("https://api.devnet.solana.com")
public_key = PublicKey("Your wallet address")
balance = client.get_balance(public_key)

print(balance)
