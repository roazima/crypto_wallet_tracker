from web3 import Web3
import json, os
from dotenv import load_dotenv

load_dotenv()
provider_url = os.getenv("WEB3_PROVIDER_URL", "")
if not provider_url:
    raise SystemExit("Set WEB3_PROVIDER_URL, e.g. export WEB3_PROVIDER_URL='https://mainnet.infura.io/v3/YOUR_KEY'")
w3 = Web3(Web3.HTTPProvider(provider_url))

def load_wallets(path="data/wallets.json"):
    with open(path) as f:
        return json.load(f)["wallets"]

def get_balance(address):
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    return balance_eth

def main():
    if w3.is_connected():
        print("Connected to Ethereum Mainnet.")
        latest_block = w3.eth.block_number
        print("Latest block number:", latest_block)

        wallets = load_wallets()
        for address in wallets:
            balance = get_balance(address)
            if balance is not None:
                print(f"ETH balance for {address}: {balance} ETH") 
            


if __name__ == "__main__":
    main()
>>>>>>> 1fe00c6 (update tracker)
