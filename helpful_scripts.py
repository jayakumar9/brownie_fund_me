# Create this file under brownie_fund_me/scripts
# refer video 2.solidity time 0:45:23
from brownie import network, config, accounts
from web3 import web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]

DECIMALS=18
STARTING_PRICE=2000
# refer video 2.solidity time 1:08:52

def get_account():
  if network.show_active()=="development":
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])
def deploy_mocks():
  print(f"The active network is {network.show_active()}")
  print(f"Deploying Mocks...")
  if len(MockV3Aggregator)<=0:
     MockV3Aggregator.deploy(DECIMALS,web3.towei(STARTING_PRICE,"ether"),{"from":get_account})
  print("Mocks Deployed!")     
