from web3 import Web3

# You can use a free public RPC like this (slow) or Infura if you create an account
INFURA_URL = "https://mainnet.infura.io/v3/2a3c8ca0387d4e348d8d42fe32c914c8"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

wallet_address = "0xB02700198273c5a044cDa5F433f8dB8689B34Eff"  # Example: Bitfinex wallet
#ens_name = "vitalik.eth"

def get_balance(address):
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    return balance_eth

def main():
    if w3.is_connected():
        print("Connected to Ethereum Mainnet.")
        latest_block = w3.eth.block_number
        print("Latest block number:", latest_block)

        wallet = "0xB02700198273c5a044cDa5F433f8dB8689B34Eff"  # Example: Bitfinex wallet
        balance = get_balance(wallet)
        print(f"ETH balance for {wallet}: {balance} ETH")
    else:
        print("Connection failed.")

if __name__ == "__main__":
    main()