# create this file under brownie_fund_me/scripts
#refer vedio 2.solidity time 0:44:22
from brownie import FundMe
from scripts.helpful_scripts import get_account


def deploy_fund_me():
  account=get_account()
  # pass the price feed address to our fundme contract
  fund_me=FundMe.deploy({"from":account},publish_source=True)
  print(f"Contract deployed to {fund_me.address}"


def main():
  deploy_fund_me()
  
