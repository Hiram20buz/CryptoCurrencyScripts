import requests

# Replace 'YOUR_SOLANA_ADDRESS' with the Solana wallet address you want to check on the Devnet
solana_address = 'YOUR_SOLANA_ADDRESS'

# Solana Devnet RPC endpoint for getting account balance
rpc_url = "https://api.devnet.solana.com"  # Solana Devnet RPC endpoint

# Solana account info request
request_data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getAccountInfo",
    "params": [solana_address],
}

response = requests.post(rpc_url, json=request_data)

if response.status_code == 200:
    data = response.json()
    if "result" in data and data["result"]:
        balance_lamports = int(data["result"]["value"]["lamports"])
        balance_sol = balance_lamports / 1e9  # Convert lamports to SOL
        print(f"Balance of {solana_address} on Devnet: {balance_sol} SOL")
    else:
        print(f"No balance information found for {solana_address}")
else:
    print(f"Error fetching balance. Please check your Solana address or Devnet RPC URL.")
