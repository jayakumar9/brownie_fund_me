# create this file under brownie_fund_me/scripts
# refer video 2.solidity time 1:15:11

from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
  fund_me=FundMe[-1]
  account=get_account()
  entrance_fee=fund_me.getEntranceFee()
  print(entrance_fee)
  print(f""The current entry fee is {entrance_fee}")
  print("Funding")
  fund_me.fund({"from": account,"value":entrance_fee})
        
def withdraw():
    fund_me=FundMe[-1]
    account=get_account()
    fund_me.withdraw({"from":account})
    # refer video 2.solidity time 1:19:00        
        
        
def main():
    fund()
    withdraw()    
        
        
  
