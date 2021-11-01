# Create this file under brownie_fund_me/scripts
# refer video 2.solidity time 0:45:23
from brownie import network, config, accounts

def get_account():
  if network.show_active()=="development":
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])
